FROM python:3.11.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /source
COPY requirements.txt /source/
RUN pip install -r requirements.txt
COPY . /source/