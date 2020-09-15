# Accurate Machine Learning Based Germination Detection, Prediction and Quality Assessment of Various Seed Cultivars
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![TensorFlow 1.15](https://img.shields.io/badge/TensorFlow-1.15-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.0)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)

## Description   

## Example Germination (Test Set)

![Example Germination](gifs/germination.gif)


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
1. Download and Extract additional Data to `PATH/TO/PROJECT/FOLDER/data`

2. Download pretrained Models (on COCO dataset) for specific Architectures from [Tensorflow Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) and extract them to `PATH/TO/PROJECT/FOLDER/pretrained_models`

Following models were used in this project:
- faster_rcnn_inception_v2_coco
- faster_rcnn_resnet50_coco
- faster_rcnn_resnet101_coco
- faster_rcnn_inception_resnet_v2_atrous_coco

3. Run Docker Image with GPU Support
```bash
docker run -it --gpus all -p 0.0.0.0:6006:6006 -v PATH/TO/PROJECT/FOLDER:/home/GerminationPrediction od
```   
- -it: Interactive Docker Shell 
- --gpus: lets Docker use GPUs
- -p: opens port 6006 which is used by tensorboard to visualize the training/validation process
- -v: binds the project folder to be used by Docker. 
- od: name of the pulled Docker Image

4. Execute Training Script inside Docker Shell (indicated by tensorflow>)
```bash
cd /home/GerminationPrediction
python scripts/train_model.py -m NEWMODELNAME -c PATH/TO/CONFIG/FILE.config
```   
- -m: Name of the new model that will be trained
- -c: Configuration File for Training

## Test Models Accuracy on a Hold-Out Test Set
1. Execute Training Script inside Docker Shell (indicated by tensorflow>)
```bash
cd /home/GerminationPrediction
python scripts/predict_testset.py -m NEWMODELNAME -c PATH/TO/CONFIG/FILE.config
```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -c: Configuration File for Testing

2. optional: Change the Checkpoint that is used for Testing
Tensorflow saves checkpoints of the Training process in `/home/GerminationPrediction/workspace/NEWMODELNAME/ckpt/`. Change the variable `model_checkpoint_path` in the file called `checkpoint` to the checkpoint that needs to be tested.

## Run Inference on the trained Model
1. Export the Inference Graph from a Checkpoint
```bash
cd /home/GerminationPrediction
python scripts/export_inference_graph.py -m NEWMODELNAME -c PATH/TO/CONFIG/FILE.config -p checkpoint
```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -c: Configuration File
- -p: Checkpoint Integer (`/home/GerminationPrediction/workspace/NEWMODELNAME/ckpt/model.ckpt-XXXX`)

2. Run Inference on Images (change paths in `predict_image.py`)
```bash
python scripts/predict_image.py
```   

3. Run Inference on a new Germination Experiment
```bash
python scripts/predict_record.py -m NEWMODELNAME -i PATH/TOPETRIDISH/FILE.record
```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -i: `.record` file with all captures of a Germination Experiment (single petri dish)  





