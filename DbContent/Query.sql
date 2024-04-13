
-- Select all the cars brand
SELECT brand
    FROM fipecar
    GROUP BY brand;

-- Select all models
SELECT model
    FROM fipecar
    GROUP BY model;

-- Select all the years of a model
SELECT year_model
    FROM fipecar
    WHERE model = '{year_model}'
    GROUP BY year_model;

-- Select the price of a specify car model by month
SELECT DISTINCT c.model, c.reference_month, c.average_price
    FROM fipecar c
    WHERE c.brand = '{brand}'
    AND c.modelo = '{model}'
    AND c.year_model = '{year_model}'
    ORDER BY reference_month;
