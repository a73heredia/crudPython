import  mysql.connector

class Conexion:

 def ConexionBaseDeDatos():
    try:
        conexion = mysql.connector.connect(user='root', password='', host='127.0.0.1', 
                                               database='clientesdb', port='3306')
            
        print("Conexion correcta")

        return conexion


    except mysql.connector.Error as error:
            print("Error al conectarse a la Base de Datos {}".format(error))

            return conexion
        
 ConexionBaseDeDatos()