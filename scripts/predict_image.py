import os
from PIL import Image
import numpy as np
import tensorflow as tf
import sys
from matplotlib import pyplot as plt
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
sys.path.append("/home/tensorflow/models/research/object_detection/")
from object_detection.utils import ops as utils_ops
import gp_utils.germ_pred_util as GR

## CHANGE PATHS ACCORDINGLY TO NEW MODELS/LABELS----------------------------------
PATH_TO_FROZEN_GRAPH = '/home/GerminationPrediction/workspace/INCRES_ZM_5/exported_graphs/frozen_inference_graph.pb'
PATH_TO_LABELS = '/home/GerminationPrediction/data/ZeaMays/configs/zm.pbtxt'
PATH_TO_TEST_IMAGES_DIR = '/home/GerminationPrediction/data/ZeaMays/test_images/'
PATH_TO_TEST_IMAGES_OUTDIR ='/home/GerminationPrediction/data/ZeaMays/test_images/'
# ---------------------------------------------------------------------------------
NUM_CLASSES = 2

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

TEST_IMAGE_PATHS = list()
for (dirpath, _, filenames) in os.walk(PATH_TO_TEST_IMAGES_DIR):
    TEST_IMAGE_PATHS += [os.path.join(dirpath, file) for file in filenames]

detection_graph = tf.compat.v1.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

with detection_graph.as_default():
    with tf.compat.v1.Session(graph=detection_graph) as sess:
        for image_path in TEST_IMAGE_PATHS:
            GR.detect_seeds_in_image(image_path,category_index, detection_graph, PATH_TO_TEST_IMAGES_OUTDIR)