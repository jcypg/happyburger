import sqlite3
import os


class BaseDeDatos:

    def __init__(self, db_name='happy_burger.db'):
        self.db_name = db_name


    def createDatabase(self):
        try:
            conect = sqlite3.connect(self.db_name)
            conect.close()
            print('Base de datos creada')
        except Exception as e:
            print("Error al crear base de datos {}".format(e))


    def checkIfDatabaseExists(self):
        if os.path.isfile(self.db_name):
            return True
        else:
            return False
        

    def openConexion(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            print('conexion exitosa a la base de datos')
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos {}".format(e))
            return None
        
    
    def closeConexion(self, conexion):
        if conexion:
            conexion.close()
            print('conexion cerrada')


    def createTable(self):
        conexion = self.openConexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute( """CREATE TABLE IF NOT EXISTS clientes(
                               clave TEXT PRIMARY KEY,
                               nombre TEX,
                               direccion TEXT,
                               correo_electronico TEXT,
                               telefono INTEGER) """)
                
                cursor.execute(""" CREATE TABLE IF NOT EXISTS menu (
                               clave TEXT PRIMARY KEY,
                               nombre TEXT,
                               precio FLOAT) """)
                
                cursor.execute("""  CREATE TABLE IF NOT EXISTS pedidos (
                               pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                               cliente TEXT,
                               producto TEXT,
                               precio FLOAT) """)


                conexion.commit()
                print('tablas creadas correctamente')
            except Exception as e:
                ("Error al crear las tablas: {}".format(e))
            finally:
                self.closeConexion(conexion)


