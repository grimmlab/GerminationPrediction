
<div align="center">    

# Accurate Machine Learning–Based Germination Detection, Prediction and Quality Assessment of Different Seed Cultivars
<!--
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
-->
[![TensorFlow 1.15](https://img.shields.io/badge/TensorFlow-1.15-FF6F00?logo=tensorflow)](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.0)
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

## Description   
We present a machine learning–based method, using modern convolutional neural networks with region proposals, for an automated and high-throughput assessment of seed germination experiments for various species.
The purpose of this study is to reduce the time-consuming and labor-intensive human visual inspections of seed germination experiments and to develop an improved germination prediction method that is (1) independent of custom color-based thresholds and thus can be applied to multiple seed cultivars and illumination settings and (2) can be used to better explore the dynamics of seed germination. 

## Example Predictions on a Germination Experiment
<div align="center"> 

![Example Germination](gifs/germination.gif)

</div>

Color-coding:
- lime: Non-germinated Prediction
- darkgreen: Non-germinated Ground Truth
- pink: Germinated Prediction
- purple: Germinated Ground Truth



## Requirements
- Python 3.6
- Compatible Graphics Card with CUDA >9 and cuDNN installed 
- [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker) [Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

## Installation via Docker

1. Download tensorflow-object-detection Image
```bash
git clone https://github.com/tensorflow/models.git
# From the root of the git repository
docker build -f research/object_detection/dockerfiles/tf1/Dockerfile -t od .
docker run -it od
```   

2. Clone this Project
```bash
git clone https://github.com/grimmlab/GerminationPrediction
```   
3. Download Version 2 of the data from http://dx.doi.org/10.17632/4wkt6thgp6.2
The Data consists of 3 zipped folders:
- GermPredDataset: Images (.jpg) and the corresponding Bounding Box Annotations (.xml) in PASCAL VOC format for Germination Experiments of 824 Zea mays, 811 Secale cereale and 814 Pennisetum glaucum seeds. This data can be used to train new models from scratch.
- GermPredRecords: In order to reproduce the results from this paper, we provide the dataset split into training, validation and hol-out test set. Aditionally, labelmaps and configuration files for the Tensorflow Object Detection API are also available.
- GermPredModels: The training checkpoint files for the model architecture and hyperparameters with the highest mean Average Precision (mAP) on the validation set and their corresponding inference graph is also published for everyone without the need of re-training the models.

4. Extract and move the subfolders into the correspoding project folder 
- GermPredRecords: move to `data/`
- GermPredModels: move to `workspace/` 

Overall, the project folder structure should look like this after importing the data:
```
GerminationPrediction
├── data
│   ├── PennisetumGlaucum   # GermPredRecords
│   ├── SecaleCereale       # GermPredRecords
│   └── ZeaMays             # GermPredRecords
│       ├── configs         # GermPredRecords
│       ├── records         # GermPredRecords
│       └── test_images     # GitHub Project
├── gifs
├── pretrained_models       # Tensorflow Model Zoo
├── scripts
└── workspace             
    ├── PennisetumGlaucum   # GermPredModels
    ├── SecaleCereale       # GermPredModels
    └── ZeaMays             # GermPredModels
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
# Example:
python scripts/train_model.py -m ZeaMays -c ./data/ZeaMays/configs/INCRES_ZM_5.config
```   
- -m: Name of the new model that will be trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -c: Configuration File for Training

## Test Models Accuracy on a Hold-Out Test Set
1. Execute Training Script inside Docker Shell (indicated by tensorflow>)
```bash
cd /home/GerminationPrediction
python scripts/predict_testset.py -m NEWMODELNAME -c PATH/TO/TEST/CONFIG/FILE.config
# Example:
python scripts/predict_testset.py -m ZeaMays -c ./data/ZeaMays/configs/INCRES_ZM_5_test.config
```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -c: Configuration File for Testing

2. optional: Change the Checkpoint that is used for Testing
Tensorflow saves checkpoints of the Training process in `/home/GerminationPrediction/workspace/NEWMODELNAME/ckpt/`. Change the variable `model_checkpoint_path` in the file called `checkpoint` to the checkpoint that needs to be tested.

## Run Inference on the Trained Models
1. Export the Inference Graph from a Checkpoint (this step has already been done if GermPredModels is downloaded)
```bash
cd /home/GerminationPrediction
python scripts/export_inference_graph.py -m NEWMODELNAME -c PATH/TO/CONFIG/FILE.config -p checkpoint
# Example:
python scripts/export_inference_graph.py -m ZeaMays -c ./data/ZeaMays/configs/INCRES_ZM_5.config -p 9000

```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -c: Configuration File
- -p: Checkpoint Integer (`/home/GerminationPrediction/workspace/NEWMODELNAME/ckpt/model.ckpt-XXXX`)

2. Run Inference on Images (change paths accordingly in `predict_image.py`)
```bash
python scripts/predict_image.py
```   

3. Run Inference on a new Germination Experiment
```bash
python scripts/predict_record.py -m NEWMODELNAME -i PATH/TOPETRIDISH/FILE.record
# Example:
python scripts/predict_record.py -m ZeaMays -i ./data/ZeaMays/records/petridishes/PD_zm1_11.record
```   
- -m: Name of the new model that has been trained, a new folder will be created in `/home/GerminationPrediction/workspace`
- -i: `.record` file with all captures of a Germination Experiment (single petri dish)  

# FAQ

## Permission Denied Error
This error occurs, because the user inside the docker image is called "tensorflow" and has an uid and gid of 1000, which might not be equal to the user who downloaded the Repository or Data. To solve issues regarding Permission Denied Errors, make sure the user with the uid/gid 1000 has Read and Write permissions to all folders and files contained in the Repository and Data. From inside the folder of the GerminationPrediction project run the following command: 
```
chmod -R 777 ./
```   
## Resource exhausted: OOM when allocating tensor with shape
This error occurs, because the memory of the GPU is large not enough to hold the model and the data. The models were trained on a RTX2080 Ti with 12 GB of VRAM. If the available GPU has less VRAM available, change the `batch_size` parameter in the config file. 



# Contributors
This best-practice pipeline is developed and maintened by members of the [Bioinformatics](www.bit.cs.tum.de) lab of [Prof. Dr. Dominik Grimm](https://bit.cs.tum.de/team/dominik-grimm/):

- M.Sc. Nikita Genze

# Citation
When using this workflow, please cite our publication:

**Accurate Machine Learning–Based Germination Detection, Prediction and Quality Assessment of Different Seed Cultivars**  

N Genze, R Bharti, M Grieb, SJ Schultheiss, DG Grimm  
Currently under Preparation


