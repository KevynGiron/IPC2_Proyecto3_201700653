from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
from tkinter import filedialog

app = Flask(__name__)
#app.config("DEBUG")

@app.route("/", methods = ["POST", "GET"])
def pagina_principal():
    return render_template('index.html')
    #return flask.render_template("frontend\index.html", datos = [])


if(__name__ == "__main__"):
    app.run(debug = True)