![pseudo-absence image header](https://github.com/instadeepai/locust-predict/tree/main/images/readme-header.png)

# Pseudo Absence Generation and Locust Prediction

[![Arxiv](https://img.shields.io/badge/ArXiv-2111.03904-orange.svg)](https://arxiv.org/pdf/2111.03904.pdf) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/instadeepai/locust-predict/blob/main/notebooks/Colab-Tutorial.ipynb)

Predicting locust spawning locations from satellite data.


**[Research Paper](https://arxiv.org/abs/2111.03904)**

## Install

Create a virtual environment and install requirements.

```
pip install -r requirements.txt
```

## Notebooks

Run the notebooks in the browser using Google Colab.

Tutorial | Link
---      | ---
Colab Intro | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/instadeepai/locust-predict/blob/main/notebooks/Colab-Tutorial.ipynb)
Model Training | [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Locust-Prediction-Modelling.ipynb)
Model Interpretation | [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Interpretation.ipynb)

## Docker

Build the image running the following.

```
make build
```

Start a docker container

```
make run
```

To launch a notebook use `make run_notebook`.


## Download Data with DVC

Make sure the Google Cloud SDK is [installed](https://cloud.google.com/sdk/docs/install) and you are authenticated.

After downloading the sdk, authenticate:

```
gcloud auth login
gcloud auth application-default login
```

Download data:

```
dvc pull
```

## Citing


If you find this project useful in your research please consider adding the following citation:

```bibtex
@inproceedings{...
}
```
