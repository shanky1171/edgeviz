FROM python:3.7-slim

RUN python -m pip install --upgrade pip

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV STATIC_URL /static
ENV STATIC_PATH /static

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY  . .
