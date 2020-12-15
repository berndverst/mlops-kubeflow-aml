FROM python:3.8-slim

ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD . /
ENTRYPOINT python3 dataprep.py
