from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, mundo! esta es la prueba..'

if __name__ == '__main__':
    # Obtén el puerto de la variable de entorno o usa 5000 si no está disponible
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
