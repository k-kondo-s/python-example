from kafka import KafkaConsumer, KafkaProducer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel, get_reverse_string

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])

while True:
    for message in consumer:
        output_message = message.value
        print(message)
        reverse_string = get_reverse_string()

        if reverse_string is not None and reverse_string.lower() == "true":
            print(output_message)
            output_message = "".join(reversed(str(output_message, 'utf-8')))

        print(output_message)
        producer.send(get_output_channel(), bytes(output_message, 'utf-8'))

