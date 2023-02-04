<div id="top"></div>

<div align="center">
  <p>
    <a href="https://https://indrap24.github.io/VORTEX/" target="_blank">
        <img src="./assets/img/vortex.png" alt="VORTEX">
    </a>
  </p>
  <h3>A Deep Learning based Tropical Cyclone Intensity Estimator featuring the INSAT-3D Infrared Image Data over the Indian subcontinent.</h3>
</div>

> **Warning**

> Work in progress. This project is still under development.

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Data Source](#data-source)
3. [Model Architecture](#system-architecture)
4. [Training and Evaluation](#training-and-evaluation)
5. [Deployment](#deployment)
6. [Contributing](#contributing)

## File Structure

```bash
├── assets
│   ├── css
│   ├── docs
│   ├── img
│   ├── js
│   └── vendor
├── darknet
│   └── yolov3.weights
├── data
│   ├── 3DIMG_01DEC2017_0300_L1B_STD_IR2 cropped.jpg
│   ├── 3DIMG_01DEC2017_0300_L1B_STD_IR2.jpg
│   ├── 3DIMG_01DEC2017_0300_L1B_STD_IR2.xml
│   ├── labels-date-ref.txt
│   ├── processed
│   └── raw
├── env.yml
├── index.html
├── LICENSE
├── Makefile
├── mobilenet_v2
├── models
│   ├── research
│   └── tensorflow_models
├── README.md
├── requirements
│   ├── req.in
│   └── req.txt
└── vortex
    ├── artifacts
    ├── hybridPredict.ipynb
    ├── hybridPred.py
    ├── notebooks
    ├── training
    └── utils

35 directories, 41 files
```

# Problem Statement

Accurately estimating the intensity of tropical cyclones is important for weather forecasting and disaster management. However, traditional methods of intensity estimation are often subjective and prone to errors. VORTEX solves this problem by leveraging the power of deep learning to provide more accurate and objective intensity estimates.

# Data Source

The INSAT-3D satellite provides infrared images of the Indian subcontinent that are used as the input to the VORTEX model. The model is trained on a large dataset of historical tropical cyclone images and corresponding intensity estimates.

```bash
├── ./data
│   ├── ./data/labels-date-ref.txt
│   ├── ./data/processed
│   │   ├── ./data/processed/crop_data
│   │   │   ├── ./data/processed/crop_data/EXTREME
│   │   │   ├── ./data/processed/crop_data/NORMAL
│   │   │   ├── ./data/processed/crop_data/SEVERE
│   │   │   ├── ./data/processed/crop_data/SUPER
│   │   │   └── ./data/processed/crop_data/VERY
│   │   ├── ./data/processed/In_Est
│   │   │   ├── ./data/processed/In_Est/EXTREME
│   │   │   ├── ./data/processed/In_Est/NORMAL
│   │   │   ├── ./data/processed/In_Est/SEVERE
│   │   │   ├── ./data/processed/In_Est/SUPER
│   │   │   └── ./data/processed/In_Est/VERY
│   │   ├── ./data/processed/Obj_Det
│   │   │   ├── ./data/processed/Obj_Det/images
│   │   │   ├── ./data/processed/Obj_Det/labels.csv
│   │   │   ├── ./data/processed/Obj_Det/test
│   │   │   ├── ./data/processed/Obj_Det/test_labels.csv
│   │   │   ├── ./data/processed/Obj_Det/test.record
│   │   │   ├── ./data/processed/Obj_Det/train
│   │   │   │   ├── ./data/processed/Obj_Det/train/f1
│   │   │   ├── ./data/processed/Obj_Det/train_labels.csv
│   │   │   └── ./data/processed/Obj_Det/train.record
│   │   └── ./data/processed/threshZero_data
│   │       ├── ./data/processed/threshZero_data/EXTREME
│   │       │   ├── ./data/processed/threshZero_data/EXTREME/f2
│   │       │   └── ./data/processed/threshZero_data/EXTREME/f3
│   │       ├── ./data/processed/threshZero_data/NORMAL
│   │       │   ├── ./data/processed/threshZero_data/NORMAL/f2
│   │       │   └── ./data/processed/threshZero_data/NORMAL/f3
│   │       ├── ./data/processed/threshZero_data/SEVERE
│   │       │   ├── ./data/processed/threshZero_data/SEVERE/Annotations
│   │       │   ├── ./data/processed/threshZero_data/SEVERE/f2
│   │       │   └── ./data/processed/threshZero_data/SEVERE/f3
│   │       ├── ./data/processed/threshZero_data/SUPER
│   │       │   ├── ./data/processed/threshZero_data/SUPER/Annotations
│   │       │   ├── ./data/processed/threshZero_data/SUPER/f2
│   │       │   └── ./data/processed/threshZero_data/SUPER/f3
│   │       └── ./data/processed/threshZero_data/VERY
│   │           ├── ./data/processed/threshZero_data/VERY/Annotations
│   │           ├── ./data/processed/threshZero_data/VERY/f2
│   │           └── ./data/processed/threshZero_data/VERY/f3
│   └── ./data/raw
│       ├── ./data/raw/APRIL_2019 Fani
│       ├── ./data/raw/final
│       ├── ./data/raw/MAY_2020 Amphan
│       ├── ./data/raw/MAY_2021 Yaas Tauktae
│       ├── ./data/raw/NOVEMBER_2020 Nivar
│       ├── ./data/raw/OCTOBER_2019 Kyarr
│       └── ./data/raw/VERY
```

# System Architecture

VORTEX is built using a Multi-Model architecture. The first model takes as input an infrared image of a Semi-Globe containing India and detects all the cyclones from a specific region. Then the detected tropical cyclone is sent to the second model and outputs a prediction of its intensity, specifically, classifies the cyclone as one of the 5 severities. The architecture is designed to use the trained models as a web service where real-time data can be fed to the model and the output can be used by weather forecasters and disaster management agencies to make informed decisions.

![Architecture](./assets/docs/SIH%20Docs/System%20Architecture%20Diagram.png)

# Training and Evaluation

The model is trained on a large dataset of historical tropical cyclone images and corresponding intensity estimates. The training process involves minimizing the mean squared error between the predicted intensity and the ground truth intensity. The model is evaluated on a hold-out test set to determine its accuracy and precision.

```bash
└── ./vortex
    ├── ./vortex/artifacts
    │   ├── ./vortex/artifacts/border_box
    │   │   ├── ./vortex/artifacts/border_box/detector.h5
    │   │   ├── ./vortex/artifacts/border_box/plot.png
    │   │   ├── ./vortex/artifacts/border_box/test_images.txt
    │   │   └── ./vortex/artifacts/border_box/tfjs
    │   │       └── ./vortex/artifacts/border_box/tfjs/detector
    │   │           └── ./vortex/artifacts/border_box/tfjs/detector/model.json
    │   ├── ./vortex/artifacts/in_estimator
    │   │   ├── ./vortex/artifacts/in_estimator/in_estimator_2.h5
    │   │   └── ./vortex/artifacts/in_estimator/in_estimator.h5
    │   ├── ./vortex/artifacts/inference_graph
    │   │   ├── ./vortex/artifacts/inference_graph/checkpoint
    │   │   ├── ./vortex/artifacts/inference_graph/pipeline.config
    │   │   └── ./vortex/artifacts/inference_graph/saved_model
    ├── ./vortex/hybridPredict.ipynb
    ├── ./vortex/hybridPred.py
    ├── ./vortex/notebooks
    │   ├── ./vortex/notebooks/border_box
    │   │   ├── ./vortex/notebooks/border_box/config.py
    │   │   ├── ./vortex/notebooks/border_box/__init__.py
    │   │   ├── ./vortex/notebooks/border_box/predict.py
    │   ├── ./vortex/notebooks/Border Box Regression.ipynb
    │   ├── ./vortex/notebooks/cropping.ipynb
    │   ├── ./vortex/notebooks/Cyclone_Detection.ipynb
    │   ├── ./vortex/notebooks/in_estimator
    │   │   ├── ./vortex/notebooks/in_estimator/__init__.py
    │   │   └── ./vortex/notebooks/in_estimator/predict.py
    │   ├── ./vortex/notebooks/inferenceutils.py
    │   ├── ./vortex/notebooks/__init__.py
    │   ├── ./vortex/notebooks/Intensity Classifier .ipynb
    ├── ./vortex/training
    │   ├── ./vortex/training/checkpoint
    │   ├── ./vortex/training/eval
    └── ./vortex/utils
        ├── ./vortex/utils/generate_tfrecord.py
        ├── ./vortex/utils/inferenceutils.py
        └── ./vortex/utils/test_train_split.py
```

# Deployment

The trained VORTEX model can be deployed as a web service or as a standalone application. The service/application takes as input an infrared image of a tropical cyclone and returns a prediction of its intensity. This information can be used by weather forecasters and disaster management agencies to make informed decisions.

# Contributing

Refer to the [Contribution Guidelines](CONTRIBUTING.md) for more information.
