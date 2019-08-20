FROM python:3

RUN apt-get update && apt-get install --no-install-recommends -y \
    python-pip \
 && rm -rf /var/lib/apt/lists/*
 
COPY python_processor.py /processor/
COPY util/*.py /processor/util/
COPY requirements.txt /processor/

RUN pip install -r /processor/requirements.txt

ENV SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS 172.28.128.3

ENTRYPOINT ["python", "/processor/python_processor.py", "$@", "--"]
