from kafka import KafkaConsumer, KafkaProducer
from util.task_args import get_kafka_binder_brokers, get_input_channel, get_output_channel, get_reverse_string
from util.http_server import HttpHealthServer
from ml_actor import Mlalgorithm

N = 4

consumer = KafkaConsumer(get_input_channel(), bootstrap_servers=[get_kafka_binder_brokers()])
producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])
HttpHealthServer.run_thread()

m = Mlalgorithm()

w = [0.0 for i in range(N)]

while True:
    for message in consumer:
        x, y = list(map(lambda z: float(z), message.value.decode('utf-8').split(',')))
        w = m.calculate(x, y, w)
        print(w)
        producer.send(get_output_channel(), bytes(','.join(map(str, w)), encoding='utf8'))

