def tendencia(coef_linear, coef_angular, X):
    return ((coef_angular * X[len(X) - 1] + coef_linear)*100)/coef_linear - 100
