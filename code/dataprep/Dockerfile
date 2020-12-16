FROM python:3.8-slim

ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD . /

ENV GITHUB_ACCESS_TOKEN=defaultvalue

ENTRYPOINT python3 dataprep.py
