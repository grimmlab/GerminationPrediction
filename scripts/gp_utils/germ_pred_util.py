import os
import io
import sys
import csv
import random
import hashlib
import pandas as pd
import numpy as np
import tensorflow as tf
from PIL import Image
import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
sys.path.append("/home/tensorflow/models/research/object_detection/")
from object_detection.utils import ops as utils_ops

from object_detection.utils import dataset_util

def save_img_as_jpg(input_record, path_to_test_img_folder):
    """
    Used to make sure that generating record files from images/annotations worked 

    """
    record_iterator = tf.python_io.tf_record_iterator(input_record)
    for string_record in record_iterator:
        example = tf.train.Example()
        example.ParseFromString(string_record)
        fname = example.features.feature["image/filename"].bytes_list.value[0].decode("utf-8")
        image = example.features.feature["image/encoded"].bytes_list.value[0]
        decoded_png =  tf.image.decode_image(image, channels=3).numpy()
        Image.fromarray(decoded_png).save(path_to_test_img_folder + fname)

# High Level Functions

def xml_path_to_filelist(xml_path):
    filename_list = tf.io.match_filenames_once(xml_path)
    init = (tf.compat.v1.global_variables_initializer(), tf.compat.v1.local_variables_initializer())
    sess = tf.compat.v1.Session()
    sess.run(init)
    files_list = sess.run(filename_list)
    files_list = sorted(files_list)
    return files_list

def split_train_val_test_praefixes_rdm(unique_praefix, SEED, TRAIN_VAL_RATIO ,TEST_RATIO):
    unique_train_val_praefix, unique_test_praefix = split_praefix(unique_praefix, SEED, TEST_RATIO)
    unique_train_praefix, unique_val_praefix = split_praefix(unique_train_val_praefix, SEED, TRAIN_VAL_RATIO)
    return unique_train_praefix, unique_val_praefix, unique_test_praefix

def filelists_from_praefixes(unique_train_praefix,unique_val_praefix, unique_test_praefix,files_list):
    train_list, _ = fileList_from_praefix(unique_train_praefix, files_list)
    eval_list, _ = fileList_from_praefix(unique_val_praefix, files_list)
    test_list, _ = fileList_from_praefix(unique_test_praefix, files_list)
    return train_list, eval_list, test_list

def write_records_from_filelists(train_list, eval_list, test_list, REC_NAME, img_path, SEED, unique_test_praefix, output_path):
    print(f"Writing {len(train_list)} Images to train_{REC_NAME}.record")
    train_arr = write_list_to_tf(train_list, "train_" + REC_NAME, img_path, SEED, output_path)
    print(f"Writing {len(eval_list)} Images to val_{REC_NAME}.record")
    eval_arr = write_list_to_tf(eval_list, "val_" + REC_NAME, img_path, SEED, output_path)
    print(f"Writing {len(test_list)} Images to test_{REC_NAME}.record")
    test_arr = write_list_to_tf(test_list, "test_" + REC_NAME, img_path, SEED, output_path)

    for test_pd in unique_test_praefix:
        test_pd_list,_ = fileList_from_praefix([test_pd], test_list)
        print(f"Writing {len(test_pd_list)} Images to PD_{test_pd}.record")
        #write_PD_to_tf(test_pd_list, "PD_" + test_pd, img_path, SEED, output_path)
        write_list_to_tf(test_pd_list, "bPD_" + test_pd, img_path, SEED, output_path + "PD/", bPD=True)
    return train_arr, eval_arr, test_arr

def write_summary(unique_train_praefix, unique_val_praefix, unique_test_praefix, train_list, eval_list, test_list, train_arr,eval_arr,test_arr,output_path, REC_NAME):
    print("Writing Summary")
    un_train, count_im_train, count_el_train, ratio_im_train, ratio_el_train = get_ratios(train_arr)
    un_val, count_im_eval, count_el_eval, ratio_im_eval, ratio_el_eval = get_ratios(eval_arr)
    un_test, count_im_test, count_el_test, ratio_im_test, ratio_el_test = get_ratios(test_arr)

    with open(output_path + 'summary_{}.txt'.format(REC_NAME), mode='w') as csv_file:
       csv_reader = csv.writer(csv_file, delimiter=',')
       csv_reader.writerow(["Summary for the generated record files"])
       csv_reader.writerow(["", "# Petri dishes", "cls_name", "# GT"])
       csv_reader.writerow(["TRAIN", len(train_list), un_train, count_im_train, count_el_train])
       csv_reader.writerow(["VAL", len(eval_list), un_val, count_im_eval, count_el_eval])
       csv_reader.writerow(["TEST", len(test_list), un_test, count_im_test, count_el_test])
       csv_reader.writerow(["TRAIN", ratio_im_train, ratio_el_train])
       csv_reader.writerow(["VAL", ratio_im_eval, ratio_el_eval])
       csv_reader.writerow(["TEST", ratio_im_test, ratio_el_test])
       csv_reader.writerow(["TRAIN_PREFIX", unique_train_praefix])
       csv_reader.writerow(["VAL_PREFIX", unique_val_praefix])
       csv_reader.writerow(["TEST_PREFIX", unique_test_praefix])

# Low Level Functions

def split_praefix(unique_train_val_praefix, SEED, RATIO):
    random.seed(SEED)
    random.shuffle(unique_train_val_praefix)
    b = int(len(unique_train_val_praefix) * RATIO)
    unique_train_praefix = unique_train_val_praefix[:b]
    unique_val_praefix = unique_train_val_praefix[b:len(unique_train_val_praefix)]
    return unique_train_praefix, unique_val_praefix

def fileList_from_praefix(unique_train_praefix, files_list):
    train_list = list()
    for _, val in enumerate(unique_train_praefix):
        # ADDED + "_" because "zm2_1" in str(s) will also mean "zm2_11" and "zm2_12"
        matching = [s for s in files_list if val + "_" in str(s)]
        train_list.append(matching)
    train_list_flat = list()
    for sublist in train_list:
        for item in sublist:
            train_list_flat.append(item)
    return train_list_flat, train_list

def get_praefix_from_fileList(files_list):

    praefix_files = list()
    for _, val in enumerate(files_list):
        praefix_files.append(str(val).split("/")[-1].split("_")
                             [0] + "_" + str(val).split("/")[-1].split("_")[1])
    unique_praefix = np.unique(praefix_files)

    return unique_praefix

def create_example(xml_file, img_path):
    # process the xml file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    image_name = root.find('filename').text
    file_name = image_name.encode('utf8')
    size = root.find('size')
    width = int(size[0].text)
    height = int(size[1].text)
    xmin = []
    ymin = []
    xmax = []
    ymax = []
    classes = []
    classes_text = []
    classes_text_str = []
    for member in root.findall('object'):
        classes_text.append(member[0].text.encode('utf8'))
        classes_text_str.append(member[0].text)
        for bnd in member.findall("bndbox"):
            xmin.append(float(bnd[0].text) / width)
            ymin.append(float(bnd[1].text) / height)
            xmax.append(float(bnd[2].text) / width)
            ymax.append(float(bnd[3].text) / height)
        classes.append(class_text_to_int(member[0].text))
    # read corresponding image
    full_path = os.path.join(img_path, '{}'.format(image_name))  # provide the path of images directory
    with tf.io.gfile.GFile(full_path, 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    if image.format != 'JPEG':
        raise ValueError('Image format not JPEG')
    key = hashlib.sha256(encoded_jpg).hexdigest()

    # create TFRecord Example
    example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(file_name),
        'image/source_id': dataset_util.bytes_feature(file_name),
        'image/key/sha256': dataset_util.bytes_feature(key.encode('utf8')),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature('jpeg'.encode('utf8')),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmin),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmax),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymin),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymax),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes)
    }))
    return classes_text_str, example

def write_list_to_tf(train_list_flat, filename, img_path, seed,output_path, bPD=False):
    train_arr = []
    writer_train = tf.io.TFRecordWriter('{}{}.record'.format(output_path, filename))
    if bPD==False:
        random.seed(seed)
        random.shuffle(train_list_flat)     # randomizes the list --> random order on how images are saved in .record
    for _, train_file in enumerate(train_list_flat):
        train_classes, example = create_example(train_file, img_path)
        writer_train.write(example.SerializeToString())
        train_arr.append(train_classes)
    writer_train.close()

    return train_arr

def write_PD_to_tf(train_file, filename, img_path, seed,output_path): #TODO: CHECK IF LOOP NECESSARY
    train_arr = []
    writer_train = tf.io.TFRecordWriter('{}{}.record'.format(output_path, filename))

    train_classes, example = create_example(train_file, img_path)
    writer_train.write(example.SerializeToString())
    train_arr.append(train_classes)
    writer_train.close()

    return train_arr

def class_text_to_int(row_label):
    if "_im" in row_label:
        return 1
    if "_el" in row_label:
        return 2

def get_ratios(train_arr):
    flat_list = []
    for sublist in train_arr:
        for item in sublist:
            flat_list.append(item)
    # if no zm_el in dataset, then train_counts[1] doesnt exist 
    unique, train_counts = np.unique(flat_list, return_counts=True)
    if train_counts.shape[0] == 1:
        train_sum = train_counts[0]
        train_zmim_ratio = 1
        train_zmel_ratio = 0
        return unique, train_counts[0], 0, train_zmim_ratio, train_zmel_ratio
    
    train_sum = train_counts[0] + train_counts[1]
    train_zmim_ratio = round(float(train_counts[0] / train_sum), 3)
    train_zmel_ratio = round(float(train_counts[1] / train_sum), 3)
    return unique, train_counts[0], train_counts[1], train_zmim_ratio, train_zmel_ratio


## Functions for "predict_image"

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def run_inference_for_single_image(image, graph):
  with graph.as_default():
    with tf.compat.v1.Session() as sess:
      # Get handles to input and output tensors
      ops = tf.compat.v1.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
      ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.compat.v1.get_default_graph().get_tensor_by_name(
              tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[0], image.shape[1])
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.compat.v1.get_default_graph().get_tensor_by_name('image_tensor:0')

      # Run inference
      output_dict = sess.run(tensor_dict,
                             feed_dict={image_tensor: np.expand_dims(image, 0)})

      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.uint8)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
  return output_dict


def detect_seeds_in_image(image_path, category_index, detection_graph, PATH_TO_TEST_IMAGES_OUTDIR):
    image = Image.open(image_path)
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    image_np = load_image_into_numpy_array(image)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    #image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
    image_np,
    output_dict['detection_boxes'],
    output_dict['detection_classes'],
    output_dict['detection_scores'],
    category_index,
    instance_masks=output_dict.get('detection_masks'),
    use_normalized_coordinates=True,
    line_thickness=2)
    plt.imsave(PATH_TO_TEST_IMAGES_OUTDIR + image_path.split("/")[-1].split(".")[0] + "_detection.jpg", image_np)