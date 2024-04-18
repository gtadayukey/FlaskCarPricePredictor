from flask import Flask

from FlaskCarPricePredictorMVC.views.analysis.analysis import analysis_bp
from FlaskCarPricePredictorMVC.views.authentications.authentications import authentications_bp
from FlaskCarPricePredictorMVC.views.home.home import home_bp
from FlaskCarPricePredictorMVC.views.shared.shared import shared_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(authentications_bp)
app.register_blueprint(shared_bp)
app.register_blueprint(analysis_bp)

if __name__ == '__main__':
    app.run()
