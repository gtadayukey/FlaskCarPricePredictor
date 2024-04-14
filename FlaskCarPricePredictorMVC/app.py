from flask import Flask, render_template


app = Flask(__name__, template_folder="views")

@app.route('/')
def index():
    return render_template('authentications/login.html')


if __name__ == '__main__':
    app.run()
