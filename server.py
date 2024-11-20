from flask import Flask, render_template, request
from orders import Pedido

app = Flask(__name__)
pedidos_db = Pedido()

@app.route('/', methods=['GET', 'POST'])
def consultar_pedido():
    datos_pedido = None
    if request.method == 'POST':
        pedido_numero = request.form.get('pedido_numero')
        datos_pedido = pedidos_db.show_orders(pedido_numero)
    return render_template('consultas_pedidos.html', datos_pedido=datos_pedido)

if __name__ == '__main__':
    app.run(debug=True)