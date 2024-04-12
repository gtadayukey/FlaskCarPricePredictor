import numpy as np


def variacao_media(dataFrame):
    print(dataFrame['preco_medio'])
    preco_inicial = dataFrame['preco_medio'][0]  # Supondo que seja 'R$ 3600,45'
    preco_final = dataFrame['preco_medio'][len(dataFrame['preco_medio'])-1]  # Supondo que seja 'R$ 3600,45'
    intervalo = np.arange(1, len(dataFrame['preco_medio']) + 1)

    return (preco_inicial + ((preco_final - preco_inicial) / (intervalo[len(intervalo)-1] - intervalo[0])) * len(intervalo),
            preco_final)

