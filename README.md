# Locust Prediction

Predicting locust spawning locations.

- Add notes about specific papers to [papers.md](./papers.md)

## Install

Create a virtual environment and install requirements.

```
pip install -r requirements.txt
```

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
## Download Data with DVC

Make sure the Google Cloud SDK is [installed](https://cloud.google.com/sdk/docs/install) and you are authenticated.

After downloading the sdk, authenticate: 

```
gcloud auth login
gcloud auth application-default login
```

Download data.

```
dvc pull
```

## Upload a New Version of the Dataset to GCP with DVC

```
dvc add data/locust_dataset.csv
git commit data/locust_dataset.csv.dvc -m "updating dataset"
dvc push
```

