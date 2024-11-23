from set_database import BaseDeDatos

class Pedido:
    # Clase para gestionar las operaciones relacionadas con los pedidos

    def __init__(self):
        # Inicializa la conexion con la base de datos
        self.data = BaseDeDatos()


    def create_order(self, select_client, select_product):
        # Crea un nuevo pedido asociado un cliente con un producto
        conexion = self.data.openConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT clave FROM clientes WHERE clave = ?", (select_client,))
                cliente = cursor.fetchone()
                if not cliente:
                    print(f"Cliente {select_client} no encontrado")
                    return
                
                cursor.execute("SELECT nombre, precio FROM menu WHERE clave = ?", (select_product,))
                producto = cursor.fetchone()
                if not producto:
                    print(f"El producto {select_product} no fue encontrado")
                    return
                
                producto_nombre, precio = producto

                

                cursor.execute(
                    "INSERT INTO pedidos (cliente, producto, precio) VALUES (?, ?, ?)",
                    (select_client, producto_nombre, precio)
                )


                conexion.commit()


                print('Pedido creado correctamente...  Imprimiendo Ticket...')
                self.ticket_print(cliente[0], select_product, precio)
            
            except Exception as e:
                print(f"Error al crear el pedido: {e}")
            finally:
                self.data.closeConexion(conexion)


    def order_cancel(self, order_id):
        # Cancela un pedido exitente por su ID
        conexion = self.data.openConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM pedidos WHERE pedido = ?", (order_id,))
                conexion.commit()
                if cursor.rowcount > 0:
                    print('Pedido cancelado correctamente')
                else:
                    print('Pedido no encontrado')
            except Exception as e:
                print(f"Error al cancelar el pedido: {e}")
            finally:
                self.data.closeConexion(conexion)


    def ticket_print(self, cliente, producto, precio):

        ticket_content = (
            "*****TIQUET DEL PEDIDO*****\n"
            F"Cliente: {cliente}\n"
            F"Producto: {producto}\n"
            F"Precio Final: ${precio}\n"
            "***************************"
        )
        print(ticket_content)


        try:
            with open('ticket.txt', 'w') as file:
                file.write(ticket_content)
            print("Ticket guardado como 'ticket.txt' ")
        except Exception as e:
            print(f"Error al guardar el ticket: {e}")



    def show_orders(self, order_number):
        conexion = self.data.openConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM pedidos WHERE pedido = ?", (order_number,))
                pedido = cursor.fetchone()
                if pedido:
                    return{
                        'Pedido': pedido[0],
                        'Cliente': pedido[1],
                        'Producto': pedido[2],
                        'Precio': pedido[3]
                    }
                else:
                    return None
            except Exception as e:
                print(f"Pedido no encontrado: {e}")
                return None
