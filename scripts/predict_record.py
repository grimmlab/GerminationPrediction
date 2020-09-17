import os
import sys
from glob import glob
import numpy as np 
import subprocess
import getopt
#from pytictoc import TicToc

def predict_experiment(model_name, input_record):
    P_INFER_DET = "/home/tensorflow/models/research/object_detection/inference/infer_detections.py"
    P_INF_GRAPH = f"/home/GerminationPrediction/workspace/{model_name}/exported_graphs/frozen_inference_graph.pb"
    P_PREDICTIONS = f"/home/GerminationPrediction/workspace/{model_name}/prediction/"
    os.makedirs(P_PREDICTIONS, exist_ok=True)
    # for best_models: no need for folder structure
    #P_INF_GRAPH = os.path.join(base_path,f"models/bestmodels/{model_name}/frozen_inference_graph.pb")
    #P_PREDICTIONS = os.path.join(base_path,f"models/bestmodels/{model_name}/predictions/")

    input_record_filename = input_record.split("/")[-1].split(".")[0]
    str_predict = f"python {P_INFER_DET} --inference_graph={P_INF_GRAPH} --input_tfrecord_paths={input_record} --output_tfrecord_path={P_PREDICTIONS}/{input_record_filename}_predictions.tfrecord"
    subprocess.run(str_predict, shell=True)

def main(argv):
    
    model_name = None
    input_record = None


    try:
        opts, _ = getopt.getopt(argv, "hb:m:i:", [ "model_name=", "input_record="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('predict_record.py -m <model_name> -i <input_record> ')
            sys.exit()
        elif opt in ("-m", "--model_name"):
            model_name = arg
        elif opt in ("-i", "--input_record"):
            input_record = arg


    print(f"MODEL NAME: {model_name}")
    print(f"INPUT RECORD FILE: {input_record}")

    if model_name == None:
        raise ValueError("Please specify a model name -m <foldername in workspace>")
    if input_record == None:
        raise ValueError("Please specify the path to a petri dish record file -i <path/to/petri/dish.record>")
    predict_experiment(model_name, input_record)

if __name__ == "__main__":
    main(sys.argv[1:])