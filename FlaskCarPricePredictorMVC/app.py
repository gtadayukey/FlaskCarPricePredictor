import json

from flask import Flask, render_template, request, jsonify, url_for, redirect
from FlaskCarPricePredictorMVC.utils.pesquisas_db import retornar_anos_modelo, retornar_modelos
from FlaskCarPricePredictorMVC.utils.plot_graph import plot_unitario
from FlaskCarPricePredictorMVC.math_model.variacao_media import variacao_media
from FlaskCarPricePredictorMVC.model.user import User
from FlaskCarPricePredictorMVC.validations.validacao_login import validar_login
from FlaskCarPricePredictorMVC.validations.validacao_cadastro import validar_cadastro

app = Flask(__name__)


@app.route('/index', methods=["POST", "GET"])
def index():
    if Usuario.usuario_logado:
        return render_template('index.html', nome_usuario=Usuario.nome_usuario)
    return redirect(url_for('login'))


@app.route('/processar_login', methods=["POST"])
def processar_login():
    email_recebido = request.form["email_login"]
    senha_recebida = request.form["senha_login"]

    validar_login(email_recebido, senha_recebida)

    if Usuario.usuario_logado:
        return redirect(url_for('index'))
    else:
        return render_template('login.html', erro_login="Dados inseridos inválidos!")


@app.route('/processar_cadastro', methods=["POST"])
def processar_cadastro():
    nome_recebido = request.form["nome_cadastro"]
    sobrenome_recebido = request.form["sobrenome_cadastro"]
    email_recebido = request.form["email_cadastro"]
    senha_recebida1 = request.form["senha_cadastro1"]
    senha_recebida2 = request.form["senha_cadastro2"]

    erro_cadastro = validar_cadastro(nome_recebido, sobrenome_recebido, email_recebido, senha_recebida1, senha_recebida2)

    if Usuario.usuario_logado:
        return redirect(url_for('index'))
    else:
        return render_template('register.html', erro_cadastro=erro_cadastro)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return render_template('register.html')


@app.route('/analiseUnitaria')
def carregar_analise_unitaria():
    if Usuario.usuario_logado:
        modelos_json = retornar_modelos()
        modelos_json = json.loads(modelos_json)
        modelos = [v['modelo'] for v in modelos_json.values()]
        # modelos = modelos_json['modelo']
        return render_template('unitary.html', modelos=modelos)
    return redirect(url_for('login'))


@app.route('/analisar', methods=['POST'])
def analisar():
    marca = 'Fiat'
    modelo = request.form['modelo']
    ano_modelo = request.form['ano_modelo']
    print(f'marca: {marca}, modelo:{modelo}, ano_modelo:{ano_modelo}')
    image_base64, dataFrame, tendencia_porcentagem = plot_unitario(marca, modelo, ano_modelo)
    previsao, preco_final = variacao_media(dataFrame)
    return render_template('data_display.html',
                           image_base64=image_base64,
                           previsao=previsao,
                           preco_final=preco_final,
                           tendencia_porcentagem=tendencia_porcentagem)


@app.route('/analiseComparativa')
def carregar_analise_comparativa():
    if Usuario.usuario_logado:
        return render_template('comparative.html')
    return redirect(url_for('login'))


@app.route('/pesquisar_ano_modelo', methods=['GET'])
def pesquisar_ano_modelo():
    modelo_carro = request.args.get('modelo')
    res = retornar_anos_modelo(modelo_carro)
    res = json.loads(res)
    anos_modelo = [v['ano_modelo'] for v in res.values()]

    return jsonify(anos_modelo)


if __name__ == '__main__':
    app.run()
