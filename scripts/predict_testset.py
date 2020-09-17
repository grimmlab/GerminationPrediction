import os
import sys
from glob import glob
import numpy as np 
import subprocess
import getopt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
def test_model(P_MODEL_MAIN, model_name, P_CONFIG):
    print(f"Testing Model...")
    str_train = f"python {P_MODEL_MAIN} --checkpoint_dir=/home/GerminationPrediction/workspace/{model_name}/ckpt/ --pipeline_config_path={P_CONFIG} --run_once > ./workspace/{model_name}/test_results.txt"
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
            print('predict_testset.py -m <model_name> -c <config_file>')
            sys.exit()
        elif opt in ("-m", "--model_name"):
            model_name = arg
        elif opt in ("-c", "--config_file"):
            config_file = arg
    print(f"MODEL NAME: {model_name}")
    print(f"CONFIGURATION FILE: {config_file}")

    P_MODEL_MAIN = "/home/tensorflow/models/research/object_detection/model_main.py"

    test_model(P_MODEL_MAIN, model_name, config_file)


if __name__ == "__main__":
    main(sys.argv[1:])