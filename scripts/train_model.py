import os
import sys
from glob import glob
import numpy as np 
import subprocess
import getopt

def gen_folder_structure(model_name):
    P_MODEL_DIR = f"/home/GerminationPrediction/workspace/{model_name}/ckpt/"
    P_INF_GRAPH = f"/home/GerminationPrediction/workspace/{model_name}/exported_graphs/"
    P_PREDICTIONS = f"/home/GerminationPrediction/workspace/{model_name}/predictions/"
    os.makedirs(P_MODEL_DIR, exist_ok=True)
    os.makedirs(P_INF_GRAPH, exist_ok=True)
    os.makedirs(P_PREDICTIONS, exist_ok=True)
    return P_MODEL_DIR

def train_model(P_MODEL_MAIN, P_MODEL_DIR, P_CONFIG):
    os.makedirs(P_MODEL_DIR, exist_ok=True)
    str_train = f"python {P_MODEL_MAIN} --model_dir={P_MODEL_DIR} --pipeline_config_path={P_CONFIG}"
    subprocess.run(str_train, shell=True)

def main(argv):
    model_name = None
    config_file = None
    try:
        opts, _ = getopt.getopt(argv, "hm:c:", ["model_name=", "config_file="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('train_model.py -m <model_name> -c <config_file>')
            sys.exit()
        elif opt in ("-m", "--model_name"):
            model_name = arg
        elif opt in ("-c", "--config_file"):
            config_file = arg
    print(f"MODEL NAME: {model_name}")
    print(f"CONFIGURATION FILE: {config_file}")

    P_MODEL_MAIN = "/home/tensorflow/models/research/object_detection/model_main.py"

    P_MODEL_DIR = gen_folder_structure(model_name)
    train_model(P_MODEL_MAIN, P_MODEL_DIR, config_file)


if __name__ == "__main__":
    main(sys.argv[1:])