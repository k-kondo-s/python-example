from kafka import KafkaConsumer, KafkaProducer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel, get_reverse_string
from util.http_server import HttpHealthServer

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])
print('pre-thread')
HttpHealthServer.run_thread()
print('post-thread')

while True:
    for message in consumer:
        print('within while')
        output_message = message.value
        reverse_string = get_reverse_string()

        if reverse_string is not None and reverse_string.lower() == "true":
            output_message = bytes("".join(reversed(str(output_message, 'utf-8'))), 'utf-8')

        producer.send(get_output_channel(), bytes(output_message))

