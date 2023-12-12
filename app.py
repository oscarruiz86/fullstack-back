"""
App
"""
import json
from flask_cors import CORS
from flask import Flask, redirect, request
from persistencia import guardar_pedido

app = Flask(__name__)
# CORS(app)

@app.route("/pizza",methods=['GET', 'POST'])
def iniciar_pedido():
    """
    pedido
    """
    nombre = request.form['NombreCliente']
    apellido = request.form['ApellidoCliente']
    pedidos = []
    pedidos.append({"nombre": nombre, "apellidos":apellido})
    crear_pedido(pedidos)
    return redirect("http://127.0.0.1:5500/solicita_pedido.html", code=302)
@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    Aquí va el código Python. Debe capturar el parámetro "size" de la request. Debe
    retornar siempre "Disponible", excepto para el tamaño "S" que debe retornar "No
    disponible" y se debe asignar en mensaje, así mensaje = "Lo que corresponda"
    """
    data = json.loads(request.data)
    tamanio_pizza = data.get("tamanioPizza",None)
    mensaje = "No disponible" if tamanio_pizza.lower() == "s" else "Disponible"
    return json.dumps({'mensaje':mensaje}), 200, {'ContentType':'application/json'}
def crear_pedido(pedidos):
    """
    crear Pedido
    """
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
        for pedido in pedidos:
            print(pedido["nombre"],pedido["apellidos"])
            guardar_pedido(pedido["nombre"],pedido["apellidos"])
