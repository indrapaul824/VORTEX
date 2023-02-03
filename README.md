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
> Work in progress.

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Data Source](#data-source)
3. [Model Architecture](#model-architecture)
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

# Model Architecture

VORTEX is built using a convolutional neural network (CNN) architecture. The model takes as input an infrared image of a tropical cyclone and outputs a prediction of its intensity. The architecture is designed to extract features from the input images and make use of them in the final prediction.

# Training and Evaluation

The model is trained on a large dataset of historical tropical cyclone images and corresponding intensity estimates. The training process involves minimizing the mean squared error between the predicted intensity and the ground truth intensity. The model is evaluated on a hold-out test set to determine its accuracy and precision.

# Deployment

The trained VORTEX model can be deployed as a web service or as a standalone application. The service/application takes as input an infrared image of a tropical cyclone and returns a prediction of its intensity. This information can be used by weather forecasters and disaster management agencies to make informed decisions.

# Contributing

Refer to the [Contribution Guidelines](CONTRIBUTING.md) for more information.
