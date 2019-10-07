# Python Example for Spring Cloud Data Flow for Kubernetes

## requirements
* Kafka 2.0.1
* python37 (This example uses `venv`)

run

```
# create data
venv/bin/python ./create_data.py

# run test.py
venv/bin/pyshon ./test.py

# run client.py
export SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS=127.0.0.1:9092
venv/bin/python client.py --spring.cloud.stream.bindings.input.destination=input --spring.cloud.stream.bindings.output.destination=output  --reverestring=true

# run processor
export SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS=127.0.0.1:9092
./venv/bin/python python_processor.py --spring.cloud.stream.bindings.input.destination=input --spring.cloud.stream.bindings.output.destination=output  --reverestring=true

```
# memo


* Run Zookeeper and Kafka listening with port 9092.
* Run `test.py` ordinarily which describes the result by subscribing Kafka.
* Run main script by the following commands:

```
export SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS=127.0.0.1:9092
./venv/bin/python python_processor.py --spring.cloud.stream.bindings.input.destination=input --spring.cloud.stream.bindings.output.destination=output  --reverestring=true
```

* Run `client.py` by the following commands which publishes test data:

```
export SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS=127.0.0.1:9092
venv/bin/python client.py --spring.cloud.stream.bindings.input.destination=input --spring.cloud.stream.bindings.output.destination=output  --reverestring=true
```

CAUTION: Probably your IDE would occur OOM.