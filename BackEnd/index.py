from flask import Flask, request, jsonify
from flask_cors import CORS
import flask as fl

app = Flask(__name__)
"""
app.config["DEBUG"] = True

CORS(app)
"""
#Generacion de los endpoint

@app.route('/')
def home():
    return fl.render_template('index.html', datos = [])


#iniciar el servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) #port=2500