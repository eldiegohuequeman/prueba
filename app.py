from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, mundo! esta es la prueba..'

if __name__ == '__main__':
    app.run(debug=True)