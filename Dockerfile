FROM python:3.9

WORKDIR /tmp
ADD ./setup.py /tmp/setup.py
ADD ./requirements.txt /tmp/requirements.txt
ADD ./locusts /tmp/locusts
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .