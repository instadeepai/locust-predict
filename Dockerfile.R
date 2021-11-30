FROM jupyter/r-notebook:r-4.1.1
COPY requirements.R /tmp/requirements.R 
RUN Rscript /tmp/requirements.R 