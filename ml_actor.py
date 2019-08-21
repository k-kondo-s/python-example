class Mlalgorithm:
    def __init__(self):
        self.mu = 0.001
        self.limit = 1000

    def calculate(self, x, y, w):
        for i in range(self.limit):
            f_wx = sum([w[k] * (x ** k) for k in range(len(w))])
            w_result = [w[k] + self.mu * (y - f_wx) * (x ** k) for k in range(len(w))]
            w = w_result
        return w


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    m = Mlalgorithm()
    x = 1
    y = 2
    w = [0, 0, 1]
    result_w = m.calculate(x, y, w)
    print(result_w)


    def make_y_line(w, x_line):
        return [sum([w[k] * (x ** k) for k in range(len(w))]) for x in x_line]


    x_line = np.arange(-3, 3, 0.1)
    plt.plot(x, y, 'o')
    plt.plot(x_line, make_y_line(w, x_line), label='default')
    plt.plot(x_line, make_y_line(result_w, x_line), label='result')
    plt.legend()
    print(result_w)
    plt.show()
