import os
import sys
from glob import glob
import numpy as np 
import subprocess
import getopt

def export_inference_graph(PATH_TO_EXPORT_INF_PY, model_name, config_path, checkpoint):
    P_MODEL_DIR = f"/home/GerminationPrediction/workspace/{model_name}/ckpt/"
    P_INF_GRAPH = f"/home/GerminationPrediction/workspace/{model_name}/exported_graphs/"

    exp_inf_string = "python " + PATH_TO_EXPORT_INF_PY + " --pipeline_config_path " + config_path + " --trained_checkpoint_prefix " + \
        P_MODEL_DIR + "model.ckpt-" + checkpoint + " --output_directory " + P_INF_GRAPH
    subprocess.run(exp_inf_string, shell=True)

def main(argv):
    model_name = None
    config_path = None
    checkpoint = None
    try:
        opts, _ = getopt.getopt(argv, "hm:c:p:", ["model_name=", "config_path=", "checkpoint="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('train_model.py -m <model_name> -c <config_path> -p <checkpoint>')
            sys.exit()
        elif opt in ("-m", "--model_name"):
            model_name = arg
        elif opt in ("-c", "--config_path"):
            config_path = arg
        elif opt in ("-p", "--checkpoint"):
            checkpoint = arg

    print(f"MODEL NAME: {model_name}")
    print(f"CONFIGURATION FILE: {config_path}")
    print(f"CHECKPOINT: {checkpoint}")


    PATH_TO_EXPORT_INF_PY = "/home/tensorflow/models/research/object_detection/export_inference_graph.py"
    export_inference_graph(PATH_TO_EXPORT_INF_PY, model_name, config_path, checkpoint)


if __name__ == "__main__":
    main(sys.argv[1:])