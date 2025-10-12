import mysql.connector
import logging
from mysql.connector import errorcode

#Configuracion del logger
logger = logging.getLogger("conexion_mysql")
logger.setLevel(logging.INFO)

#Formateador para los mensajes de registro
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#Manejador para mostrar los registros en la consola
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Metodo que nos permite conectarnos a una base de datos MySQL
def connect_to_mysql():
    try:
        return mysql.connector.connect(
            user='root' ,
            password='Dragonballz11' ,
            host='localhost' ,
            database='sistema_ventas' ,
            port='3306'
        )
    except mysql.connector.Error as err:
        logger.error(err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Error de autenticación: usuario o contraseña incorrectos."
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Error: La base de datos no existe."
        else:
            return "Se ha produido un error. Por favor contecte al administrador."