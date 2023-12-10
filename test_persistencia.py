from persistencia import guardar_pedido
from flask import Flask, redirect, request


app = Flask(__name__)

@app.route("/pizza",methods=['GET', 'POST'])
def pedido():  
      nombre = request.form['NombreCliente']
      apellido = request.form['ApellidoCliente']   
      pedidos = []
      pedidos.append({"nombre": nombre, "apellidos":apellido})
      crearPedido(pedidos)
      return redirect("http://127.0.0.1:5500/solicita_pedido.html", code=302)

def crearPedido(pedidos):
      with open("pedidos.txt", "w", encoding="utf-8") as file:        
            file.write("")
            file.close()     
      for pedido in pedidos:
            print(pedido["nombre"],pedido["apellidos"])
            guardar_pedido(pedido["nombre"],pedido["apellidos"])
