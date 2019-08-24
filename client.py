import time
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer

from util.task_args import get_kafka_binder_brokers, get_input_channel

producer = KafkaProducer(bootstrap_servers=[get_kafka_binder_brokers()])

N = 100

csv = pd.read_csv('./d.csv')

for i in csv.values:
    producer.send(get_input_channel(), bytes(str(i[0]) + ',' + str(i[1]), encoding='utf8'))
time.sleep(3)

