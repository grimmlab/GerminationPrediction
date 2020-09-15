import os
import io
import sys
import glob
import hashlib
import random
import numpy as np
from PIL import Image
import csv
import xml.etree.ElementTree as ET
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from object_detection.utils import dataset_util
# OWN UTIL FUNCTIONS:
import gp_utils.germ_pred_util as GR
def main(_):
    ##### Change base_path according to folder structure #####
    base_path = "/home/GerminationPrediction/"
    REC_NAME = "zm" #suffix for generated record files
    species_name = "ZeaMays" # PennisetumGlaucum (SEED = 4) / ZeaMays (SEED = 4) / SecaleCereale (SEED = 9)
    SEED = 4
    #######################################################

    TRAIN_VAL_RATIO = 0.9
    TEST_RATIO = 0.9

    xml_path = os.path.join(base_path,f"data/{species_name}/ann/")
    xml_list = xml_path+ "*.xml"
    img_path = os.path.join(base_path,f"data/{species_name}/img/")
    output_path = os.path.join(base_path,f"data/{species_name}/records/")
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(output_path + "PD/", exist_ok=True)

    print(f"Working on {species_name} with seed: {SEED}")
    files_list = GR.xml_path_to_filelist(xml_list)
    unique_praefix = GR.get_praefix_from_fileList(files_list)
    unique_train_praefix, unique_val_praefix, unique_test_praefix = GR.split_train_val_test_praefixes_rdm(
                                                                                                       unique_praefix=unique_praefix,
                                                                                                       SEED=SEED,
                                                                                                       TRAIN_VAL_RATIO=TRAIN_VAL_RATIO,
                                                                                                       TEST_RATIO=TEST_RATIO)
    train_list, eval_list, test_list = GR.filelists_from_praefixes(unique_train_praefix=unique_train_praefix,
                                                                unique_val_praefix=unique_val_praefix, 
                                                                unique_test_praefix=unique_test_praefix,
                                                                files_list=files_list)
    train_arr,eval_arr,test_arr = GR.write_records_from_filelists(train_list, eval_list, test_list, REC_NAME, img_path, SEED, unique_test_praefix, output_path)
    GR.write_summary(unique_train_praefix, unique_val_praefix, unique_test_praefix, train_list, eval_list, test_list, train_arr,eval_arr,test_arr,output_path, REC_NAME)


if __name__ == '__main__':
    tf.compat.v1.app.run()

