FROM PYTHON:3-slim

RUN pip3 install kfp==1.1.1

ENV PIPELINE_ID=default
ENV EXPERIMENT_ID=default
ENV IMAGE_TAG=default

ENTRYPOINT python3 launcher.py
