from set_database import BaseDeDatos
from customers import Clientes
from menu import Menu
from orders import Pedido

base_de_datos = BaseDeDatos()
base_de_datos.createTable()


clientes = Clientes()
menu = Menu()
pedidos = Pedido()



def main_menu():
    print('menu de opciones')
    print('1.- Clientes')
    print('2.- Menu')
    print('3.- Pedidos')
    print('4.- Salir')


def menu_clients():
    print('opciones: ')
    print('1.- Agregar cliente')
    print('2.- Eliminar cliente')
    print('3.- Actualizar Cliente')
    print('4.- Menu Principal')


def menu_products():
    print('Seleccionar menu: ')
    print('1.- Agregar producto')
    print('2.- Eliminar producto')
    print('3.- Actualizar producto')
    print('4.- Menu Principal')


def menu_orders():
    print('Pedidos: ')
    print('1.- Crear pedido')
    print('2.- Cancelar pedido')
    print('3.- Menu principal')


def select_main_menu():
    while True:
        main_menu()
        opcion = int(input("Ingresar una opcion del menu: "))

        if opcion == 1:
            manage_clients()
        elif opcion == 2:
            manage_products()
        elif opcion == 3:
            manage_orders()
        elif opcion == 4:
            print('Saliendo de la App...')
            break
        else:
            print("Ingresa un numero valido")


def manage_clients():
    while True:
        menu_clients()
        opcion = int(input('Seleciona una opcion: '))

        if opcion == 1:
            clave = input('Igresar Clave del Cliente: ')
            nombre = input('Ingresar Nombre del Ciente: ')
            direccion = input('Ingresar Direccion del Cliente: ')
            correo = input('Ingresar Correo del Cliente: ')
            telefono = input('Ingresar telefono del Cliente: ')
            clientes.agregar_cliente(clave, nombre, direccion, correo, telefono)

        elif opcion == 2:
            clave = input('Ingrese la clave del cliente a eliminar: ')
            clientes.eliminar_cliente(clave)

        elif opcion == 3:
            clave = input('Ingresar Clave del cliente para actualizar: ')
            nombre = input('Ingresar el nuevo nombre para actualizar: ')
            direccion = input('Ingresar la nueva direccion: ')
            correo = input('Ingresar el nuevo telefono: ')
            telefono = input('Ingresar el nuevo telefono: ')
            clientes.actualizar_cliente(clave, nombre or None, direccion or None, correo or None, telefono or None)

        elif opcion == 4:
            break
        else:
            print('Opcion no valida, intentar otra vez')

def manage_products():
    
    while True:
        menu_products()
        opcion = int(input('Selecciona una opcion: '))
        if opcion == 1:
            clave = input('Ingrese la clave del producto: ')
            nombre = input('Ingrese la nombre del producto: ')
            precio = float(input('Ingrese el precio del producto: '))
            menu.agregar_productos(clave, nombre, precio)

        elif opcion == 2:
            clave = input('Ingrese la clave del producto para eliminar: ')
            menu.eliminar_producto(clave)

        elif opcion == 3:
            clave = input('Ingrese la clave del producto para actualizar: ')
            nombre = input('Ingrese el nuevo nombre: ')
            precio = input('Ingrese el nuevo precio: ')
            menu.agregar_productos(clave, nombre, precio)
            menu.actualizar_producto(clave, nombre or None, float(precio) if precio else None)
        
        elif opcion == 4:
            break
        else:
            print('Opcion no valida, intentar de nuevo')

def manage_orders():
    while True:
        menu_orders()
        opcion = int(input('Seleciona una opcion: '))

        if opcion == 1:
            cliente = input('Ingresa la clave del cliente: ')
            producto = input('Ingresa la clave del producto: ')
            
            pedidos.create_order(cliente, producto)
        elif opcion == 2:
            pedido_id = int(input('Ingresa el id del producto para cancelar: '))
            pedidos.order_cancel(pedido_id)
        elif opcion == 3:
            break
        else:
            print('opcion no valida, intenta de nuevo')



select_main_menu ()
