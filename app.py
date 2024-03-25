from flask import Flask  # La primera letra en Flask debe ser mayúscula

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'

if __name__ == '__main__':
    app.run(debug=True)
