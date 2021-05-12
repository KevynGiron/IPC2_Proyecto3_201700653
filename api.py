from flask import Flask, render_template, request, redirect, url_for
import xml.etree.ElementTree as ET
from tkinter import filedialog
import procesar_xml as PX
import os

app = Flask(__name__)
#app.config("DEBUG")
text = ""

@app.route("/")
def pagina_principal():
    return render_template('index.html', txt1 = "")

@app.route("/datos")
def show_data():
    return render_template("datos.html")

@app.route("/reporte")
def show_reporte():
    os.system("reporteipc2.pdf")
    return render_template('index.html', txt1 = "")

@app.route("/", methods = ["POST"])
def function():
    if request.method == "POST":
        text = request.form['u']
        #print(text)
        texto_advertencia = ""
        if PX.convertir_xml(text) == "Un error a ocurrido":
            texto_advertencia = "Un error a ocurrido"
        else:
            PX.convertir_xml(text)
        #print(text)
        return render_template("index.html", txt1 = text, txt2 = PX.mostrar_datos(), txt3 = texto_advertencia)
    #return flask.render_template("frontend\index.html", datos = [])

if(__name__ == "__main__"):
    app.run(debug = True)