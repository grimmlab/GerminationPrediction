# Accurate Machine Learning Based Germination Detection, Prediction and Quality Assessment of Various Seed Cultivars

## Getting Started

### Requirements
- Python 3.x
- Tensorflow Object Detection API
- CUdnn
- CUDA


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

3. Generate training/validation/testing Record files to train the model (gen_record_by_petridish.py)
    - change Paths according to folder structure
    - run gen_record_by_petridish.py
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




## Update 18.06.2020
- storing postprocess here
- storing image generation here
