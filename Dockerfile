FROM python:3.10.15-slim
RUN apt update
RUN apt install -y git

WORKDIR /opt/app
COPY .requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt

