
-- Select all the cars brand
SELECT marca
    FROM carros_fipe
    GROUP BY marca;

-- Select all models
SELECT modelo
    FROM carros_fipe
    GROUP BY modelo;

-- Select all the years of a model
SELECT ano_modelo
    FROM carros_fipe
    WHERE modelo = '{ano_modelo}'
    GROUP BY ano_modelo;

-- Select the price of a specify car model by month
SELECT DISTINCT c.modelo, c.mes_referencia, c.preco_medio
    FROM carros_fipe c
    WHERE c.marca = '{marca}'
    AND c.modelo = '{modelo}'
    AND c.ano_modelo = '{ano_modelo}'
    ORDER BY mes_referencia;
