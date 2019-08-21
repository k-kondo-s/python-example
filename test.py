
from ml_actor import Mlalgorithm

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    m = Mlalgorithm()
    x = 5
    y = 5
    w = [0.22214171324536555,-0.017489090830986976,0.19461214963638276]
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