#FROM springcloud/openjdk:latest
FROM python:3

RUN apt-get update && apt-get install --no-install-recommends -y \
    python-pip \
 && rm -rf /var/lib/apt/lists/*
 
RUN pip install kafka-python

COPY python_processor.py /processor/
COPY util/*.py /processor/util/

ENV SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS 172.28.128.3

ENTRYPOINT ["python", "/processor/python_processor.py", "$@", "--"]
