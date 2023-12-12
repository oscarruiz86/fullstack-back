import json
from persistencia import guardar_pedido
from flask import Flask, Response, redirect, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route("/pizza",methods=['GET', 'POST'])
def pedido():
    nombre = request.form['NombreCliente']
    apellido = request.form['ApellidoCliente']
    pedidos = []
    pedidos.append({"nombre": nombre, "apellidos":apellido})
    crearPedido(pedidos)
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
      tamanioPizza =  data.get("tamanioPizza",None)
      mensaje = "No disponible" if  tamanioPizza.lower() == "s"  else "Disponible"
      return json.dumps({'mensaje':mensaje}), 200, {'ContentType':'application/json'}  
      

def crearPedido(pedidos):
      """
      crear Pedido
      """
      with open("pedidos.txt", "w", encoding="utf-8") as file:
            file.write("")
            file.close()     
            for pedido in pedidos:
                  print(pedido["nombre"],pedido["apellidos"])
                  guardar_pedido(pedido["nombre"],pedido["apellidos"])

