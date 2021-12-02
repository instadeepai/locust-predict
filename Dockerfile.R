FROM jupyter/r-notebook:r-4.1.1
USER root
RUN conda install -c conda-forge -c santandermetgroup r-terra r-raster udunits2  r-mopa r-rworldmap r-dismo 
RUN apt-get update -y && apt-get install -y pkg-config
COPY requirements.R /tmp/requirements.R 
RUN Rscript /tmp/requirements.R 