FROM python:3.8-slim

ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD . /
RUN cat github_hook.py >> train.py

ENV GITHUB_ACCESS_TOKEN=defaultvalue

#TODO: ADD TRAINING PARAMETERS AS ENV VARS

ENTRYPOINT python3 train.py
