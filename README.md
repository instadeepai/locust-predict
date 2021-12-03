![pseudo-absence image header](https://github.com/instadeepai/locust-predict/blob/main/images/readme-header.png)

# Pseudo Absence Generation and Locust Prediction

[![Arxiv](https://img.shields.io/badge/ArXiv-2111.03904-orange.svg)](https://arxiv.org/pdf/2111.03904.pdf) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/instadeepai/locust-predict/blob/main/notebooks/Colab-Tutorial.ipynb)

Predicting locust breeding ground locations from satellite data.


**[Research Paper](https://arxiv.org/abs/2111.03904)**

## Install

Create a virtual environment and install requirements.

```
pip install -r requirements.txt
```

## Notebooks and scripts

Run the notebooks with Google Colab or appropriate Docker container. 

Notebooks | Link
---      | ---
Colab Intro (Python)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/instadeepai/locust-predict/blob/main/notebooks/Colab-Tutorial.ipynb)
Pseudo-Absence Generation (R)| [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Pseudo%20Absence%20Generation.ipynb)
Pseudo-Absence Generation Viz (R)| [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Pseudo%20Absence%20Generation%20Viz.ipynb)
Add Environmental and Climate Data (Python)| [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Append%20History%20Data.ipynb)
Model Training (Python)| [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Locust-Prediction-Modelling.ipynb)
Model Interpretation (Python)| [View](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Interpretation.ipynb)
Hypothesis Testing (Python)| [View](https://github.com/instadeepai/locust-predict/blob/main/hypothesis_testing.R)

## Docker

Build the image running the following.
```
make build
```

Start a docker container in bash
```
make bash
```

To launch a notebook use `make run_notebook`.

**For the R Docker Container** add `version=r` to the build and run commands.

## Download Preprocessed Data
Download and extract the preprocessed data into `data/` directory from [here](https://drive.google.com/file/d/1rZjRooS8AzUjuuNHf5_7YX_pd1U4iuDt/view?usp=sharing)

## Preprocesse Data
To run the preprocessing workflow, the following datasets are required:
- [FAO Locust Observation Data](https://locust-hub-hqfao.hub.arcgis.com/datasets/hqfao::hoppers-1/about)
- [NASA GLDAS_NOAH025_3H Dataset](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_3H_2.1/summary)
- [ISRIC SoilGrids](https://soilgrids.org/) (Refer to this [notebook](https://github.com/instadeepai/locust-predict/blob/main/notebooks/notebooks/Download%20ISRIC%20SoilGrids%20Data.ipynb) on how to download SoilGrids data)

Run the following notebooks, to generate preprocessed data
1. [Pseudo-Absence Generation](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Pseudo%20Absence%20Generation.ipynb). You can run [Pseudo-Absence Generation Viz](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Pseudo%20Absence%20Generation%20Viz.ipynb) for visualization.
2. [Add Environmental and Climate Data](https://github.com/instadeepai/locust-predict/blob/main/notebooks/Append%20History%20Data.ipynb)

<!-- ## Download Data with DVC

Make sure the Google Cloud SDK is [installed](https://cloud.google.com/sdk/docs/install) and you are authenticated.

After downloading the sdk, authenticate:

```
gcloud auth login
gcloud auth application-default login
```

Download data:

```
dvc pull
``` -->

## Citing


If you find this project useful in your research please consider adding the following citation:

```bibtex
@proceedings{yusef2021locust,
    title     = {On pseudo-absence generation and machine learning for locust breeding ground prediction in Africa},
    author    = {Ibrahim Salihu Yusuf and
                 Kale-ab Tessera and
                 Thomas Tumiel and
                 Sella Nevo and
                 Arnu Pretorius},
    journal   = {Advances in Neural Information Processing Systems (NeurIPS) workshop, 2021, Sydney},
    year      = {2021},
    url       = {https://arxiv.org/pdf/2111.03904.pdf},
}
```
