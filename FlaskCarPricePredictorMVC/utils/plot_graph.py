import base64
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from FlaskCarPricePredictorMVC.math_model.linear_regression import linear_regression
from FlaskCarPricePredictorMVC.math_model.tendencia_variacao import tendencia
from FlaskCarPricePredictorMVC.utils.pesquisas_db import retornar_para_plot


def plot_unitario(marca, modelo, ano_modelo):
    dados = retornar_para_plot(marca, modelo, ano_modelo)

    dataFrame = pd.DataFrame(dados, columns=['modelo', 'mes_referencia', 'preco_medio'])

    X = dataFrame['mes_referencia']
    y = dataFrame['preco_medio']

    xreg = np.arange(len(X))

    # model = LinearRegression().fit(xreg.reshape(-1, 1), y)
    # print(model.coef_)
    # print(model.intercept_)

    coeficiente_angular, coeficiente_linear = linear_regression(y)
    print(coeficiente_angular, coeficiente_linear)

    plt.figure(figsize=(10, 6))
    plt.scatter(xreg, y, color='blue', label='Dados Reais')
    plt.plot(xreg, coeficiente_angular * xreg + coeficiente_linear, color='red', label='Linha de Regressão')
    plt.xlabel('Meses do ano')
    plt.ylabel('Preço Total')
    plt.title('Regressão Linear de Preços medios por mês')
    plt.legend()
    plt.gcf().autofmt_xdate()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    tendencia_porcentagem = tendencia(coeficiente_linear, coeficiente_angular, xreg)

    return image_base64, dataFrame, tendencia_porcentagem
