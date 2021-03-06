# services/users/project/__init__.py

from flask import Flask, jsonify


# instanciando la app

app = Flask(__name__)

# estableciendo configuración
app.config.from_object('project.config.DevelopmentConfig') # <-- nuevo

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'pong!!!'
    })
