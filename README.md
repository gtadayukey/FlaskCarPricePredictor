# Car Price Check

Problemas e objetivos:
Fizemos esse projeto por conta do dificil acesso aos dados da tabela fipe ao longo de um periodo.
Isso porque o site da Fipe nao disponibiliza uma api para coleta destes dados, tornando-se dificil o acesso a analise dos mesmos
Buscamos a facilidade no acesso a informação

Funcionalidades:
Analise unitaria - Analise de um unico carro
Analise comparativa - Analise de dois ou mais carros

Ferramentas:
Para armazenar os dados do projeto utilizamos o PostgreSQL 
Para rodar a aplicação utilizamos python e seu micro-framework flask
Para pegar os dados da tabela fipe foi feito um codigo web scraping que esta disponibilizado dentro da pasta do projeto
Para analisar os dados, utilizamos dois métodos:
  1 - Regressao Linear para analise de tendencia (Sem uso de bibliotecas como sklearn)
  2 - Funcao baseada na taxa de variação media dos preços em relacao aos meses

Limitações:
Por enquanto a aplicação é limitada somente a carros da fiat por conta da grande quantidade de dados e o curto periodo de tempo que tivemos para desenvolver.

Previsões:
Caso continuemos nesse projeto queremos incluir todos os carros de todas as marcas e de todos os meses referencia desde a criação da tabela Fipe
Buscaremos melhorar nossos modelos matematicos para melhor analise das tendencias de mercado
