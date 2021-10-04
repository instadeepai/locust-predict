# Locust Prediction

Predicting locust spawning locations.

- Add notes about specific papers to [papers.md](./papers.md)

## Install

Create a virtual environment and install requirements.

```
pip install -r requirements.txt
pip install -e .
```

## Download Data with DVC

Make sure the Google Cloud SDK is [installed](https://cloud.google.com/sdk/docs/install) and you are authenticated.

```
dvc pull
```

## Upload a New Version of the Dataset to GCP with DVC

```
dvc add data/locust_dataset.csv
git commit data/locust_dataset.csv.dvc -m "updating dataset"
dvc push
```
