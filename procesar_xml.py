import xml.etree.ElementTree as ET
import datos
import os
import re

lista = []
lista_datos = []

def save_data(cadena):
    lista_aux = cadena.split('\n')
    fecha = ""
    us = ""
    usuarios_afectados = ""
    error = ""
    #print("----------------------------------------------------------------------")
    for i in lista_aux:
        if re.search(r"\d\d/\d\d/\d\d", i) != None:
            sub_cadena = re.search(r"\d\d/\d\d/\d\d", i)
            fecha = sub_cadena.group()
        if re.search(r'Reportado por: ”Nombre Empleado \d', i) != None:
            sub_cadena = re.search(r"([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})", i)
            us = sub_cadena.group()
        if re.search(r"Usuarios afectados: ", i) != None:
            sub_cadena = i.lstrip("Usuarios afectados: ")
            usuarios_afectados = sub_cadena
        if re.search(r"Error: [0-9]{1,9}", i) != None:
            sub_cadena = re.search(r"[0-9]{1,9}", i)
            error = str(sub_cadena.group())
    
    #print('Usuarrio: ' + us)
    lista_datos.append(datos.datos(fecha, us,usuarios_afectados,error))

def convertir_xml(archivo):
    file = open("entrada.txt" , 'w')
    file.write(archivo)
    file.close()

    hola = []
    f = open("entrada.txt")
    for linea in f:
        if linea != '\n':
            hola.append(linea)
        #print(linea)
    f.close()

    nuevo_archivo = ""
    for i in hola:
        if re.search(r"<EVENTOS>", str(i)) != None:
            nuevo_archivo = nuevo_archivo + str(i)
        elif re.search(r"<EVENTO>", str(i)) != None:
            nuevo_archivo = nuevo_archivo + str(i)
        elif re.search(r"</EVENTO>", str(i)) != None:
            nuevo_archivo = nuevo_archivo + str(i)
        elif re.search(r"</EVENTOS>", str(i)) != None:
            nuevo_archivo = nuevo_archivo + str(i)
        else:
            aux1 = str(i).replace('<',"")
            aux2 = aux1.replace('>',"")
            nuevo_archivo = nuevo_archivo + aux2
            
    #print(nuevo_archivo)
    file = open("final.xml" , 'w')
    file.write(nuevo_archivo)
    file.close()

    try:
        doc = open("final.xml")
        xml_doc = ET.parse(doc)
        raiz = xml_doc.getroot()
        for i in raiz:
            #print(str(i.text))
            save_data(str(i.text))
    except:
        return "Un error a ocurrido"

def mostrar_datos():
    cadena = ""
    for i in lista_datos:
        cadena = cadena + 'Fecha: ' + i.get_fecha() + '\nUsuario: ' + i.get_usuario() + '\nAfectaods: ' + i.get_afectado() + '\nNo. Error: ' + i.get_error()
    #print(cadena)
    return cadena

