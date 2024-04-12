def linear_regression(y):
    m = 10
    b = 10
    taxa_de_aprendizagem = 0.00001

    def derivada_custo_m(x):
        if x < 0:
            return 0
        # print(2*(m*x+b-y[i])*x + (2*(m*x+b-y[i-1])*x))
        # print(y[len(y)-1])
        return (2 * (m * x + b - y[x]) * x) + derivada_custo_m(x - 1)

    def derivada_custo_b(x):
        if x < 0:
            return 0
        return 2 * (m * x + b - y[x]) + derivada_custo_b(x - 1)

    for i in range(1000000):
        m = m - taxa_de_aprendizagem * derivada_custo_m(len(y) - 1)  # derivada_custo_m(len(y)-1)
        b = b - taxa_de_aprendizagem * derivada_custo_b(len(y) - 1)

    return m, b
