# Accurate Machine Learning Based Germination Detection, Prediction and Quality Assessment of Various Seed Cultivars
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![TensorFlow 1.15](https://img.shields.io/badge/TensorFlow-1.15-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.0)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)

## Description   



## Requirements
- Python 3.x
- CUdnn
- CUDA
- nvidia-docker2

## Installation via Docker

1. Download tensorflow-object-detection Image
```bash
docker pull deeone/tensorflow-object-detection
```   

2. Clone this Project
```bash
git clone https://github.com/Nischkl/GerminationPrediction
```   



## Train new Models
1. Download and Extract additional Data to PATH/TO/PROJECT/FOLDER/data

2. Download pretrained Models (on COCO dataset) for specific Architectures from [Tensorflow Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) and extract them to PATH/TO/PROJECT/FOLDER/pretrained_models

Following models were used in this project:
- faster_rcnn_inception_v2_coco
- faster_rcnn_resnet50_coco
- faster_rcnn_resnet101_coco
- faster_rcnn_inception_resnet_v2_atrous_coco

3. Run Docker Image with GPU Support
```bash
docker run -it --gpus all -p 0.0.0.0:6006:6006 -v PATH/TO/PROJECT/FOLDER:/home/GerminationPrediction od
```   
-it: Interactive Docker Shell 

--gpus: lets Docker use GPUS 

-p: opens port 6006 which is used by tensorboard to visualize the training/validation process

-v: binds the project folder to be used by Docker. 

od: name of the pulled Docker Image



or: Docker
### Usage
1. Download data from 
2. Extract to data/ 
    - Structure:
        data/
        - ZeaMays/
          - img/
          - ann/
        - PennisetumGlaucum/
          - img/
          - ann/
        - SecaleCereale/
          - img/
          - ann/
3. download finetune checkpoint from tensorflow model zoo

3. Generate training/validation/testing Record files to train the model (gen_records.py)
    - change Paths according to folder structure
    - run gen_records.py
    - output consists of:
        - summary textfile with class ratios
        - training/validation/testing record files
        - testing record files for each petri dish in /PD folder
4. Generate hyperparameters for validating the models (gen_hyperpar.py)
5. Modify Configuration (/config) and label map

6. Train Model (python3 train_model.py -b <base_path> -m "<model_name>" -c <path_to_config_file>) base_path= folder where /data is located
7. Check models performance with tensorboard (tensorboard --logdir= path_to_models_folder)
8. Export inference Graph of best performing model (export_inference_graph.py -b <base_path> -m "<model_name>" -c <path_to_config_file> -p <checkpoint_postfix>)
9. Make Predictions on test set ()
    - in models/<model_name>/ckpt/checkpoint: change model_checkpoint_path to the checkpoint that is used for testing
    - run predict_testset.py -p <path_to_ckpt_folder> -c <path_to_testing_config_file>
10. Predict Germination status on a petri dish
    - predict_record.py -b <base_path> -m "<model_name>" -i <input_petridish_record>
    - outputs in models/<model_name>/predictions/

11. Post-processing step: gen_GermCurve.py
    - creates GermCurves folder in <base_path>
    - format of csv-file:  <max_seeds>, <germ_seeds (cumulated)>

12. use R package: germinationmetrics   

12. vis_GermCurve.py: plots Figure 5 of paper
13. vis_GermMetrics.ipynb: plots Figure 6 of paper



## Util Scripts
- gen_hyperpar.py: used to uniformly sample hyperparameters that are used in this study
- extract_img_from_tfrecord.py: can be used on files that are generated with "generate_tfrecords.py" to debug it


## Custom Models


## Example Germination (Test Set)

![Example Germination](gifs/germination.gif)

GIF: Predictions on one Germination Experiment
## Post-Processing
- shows the germination curve of one seed
- Seed #8 in upper GIF (ng: not germinated, g: germinated)
- The goal is to get a germination curve for each seed, where the seed is only germinating once. 
- maybe remove Ground Truth as SAE not dependent on it. Add Title
![Germination Tracking](gifs/SAE.gif)

