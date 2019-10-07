import pandas as pd
from kafka import KafkaConsumer

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import numpy as np

    consumer = KafkaConsumer('output', bootstrap_servers=['127.0.0.1:9092'])
    inc = 1
    csv = pd.read_csv('./d.csv')


    def do(message, csv, inc):
        result_w = list(map(lambda x: float(x), message.value.decode('utf8').split(',')))
        w = [0.0, 0.0, 0.0, 0.0]

        def make_y_line(w, x_line):
            return [sum([w[k] * (x ** k) for k in range(len(w))]) for x in x_line]

        x_line = np.arange(-1, 1, 0.01)
        plt.plot(x_line, make_y_line(w, x_line), label='init')
        csv_part = csv[0:inc]
        plt.plot(csv_part['x'], csv_part['y'], 'o')
        plt.plot(x_line, make_y_line(result_w, x_line), label='result')
        plt.legend()
        print(result_w)
        plt.show()

    count = 0
    limit = len(pd.read_csv('./d.csv'))
    csv = pd.read_csv('./d.csv')
    while True:
        for message in consumer:
            count += 1
            if count % 1 == 0:
                do(message, csv, inc)
                inc = count + 1
        # plt.show()