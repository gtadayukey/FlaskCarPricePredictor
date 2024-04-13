import numpy as np


def average_variation(df):
    print(df['average_price'])
    initial_price = df['average_price'][0]
    final_price = df['average_price'][len(df['average_price']) - 1]
    interval = np.arange(1, len(df['average_price']) + 1)

    return (initial_price + ((final_price - initial_price) / (interval[len(interval) - 1] - interval[0]))
            * len(interval), final_price)


def variation_tendency(linear_coef, angular_coef, x):
    return ((angular_coef * x[len(x) - 1] + linear_coef)*100)/linear_coef - 100


def linear_regression(y):
    m = 10
    b = 10
    learning_rate = 0.00001

    def derivative_m_cost(x):
        if x < 0:
            return 0
        return (2 * (m * x + b - y[x]) * x) + derivative_m_cost(x - 1)

    def derivative_b_cost(x):
        if x < 0:
            return 0
        return 2 * (m * x + b - y[x]) + derivative_b_cost(x - 1)

    for i in range(1000000):
        m = m - learning_rate * derivative_m_cost(len(y) - 1)
        b = b - learning_rate * derivative_b_cost(len(y) - 1)

    return m, b
