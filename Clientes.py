from Conexion import *

class CClientes:
    
   def mostrarClientes():
      try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;") 

            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
      except mysql.connector.Error as error:
              print("Error de Ingreso de Datos {}" .format(error))
            

   def ingresarClientes(nombres,apellidos,sexo):
         
         try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s)"
            #La variable valores tiene que ser una tupla(listas que no se pueden modificar)
            
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Ingresado")
            cone.close()

         except mysql.connector.Error as error:
              print("Error de Ingreso de Datos {}" .format(error))

   
   def modificarClientes(idUsuario,nombres,apellidos,sexo):
         
         try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %s Where usuarios.id = %s "
            
            valores = (nombres,apellidos,sexo, idUsuario)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()

         except mysql.connector.Error as error:
              print("Error de Actualizacion de Datos {}" .format(error))
 

   def eliminarClientes(idUsuario):
         
         try:
            cone = Conexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE from usuarios WHERE usuarios.id = %s"
            
            valores = (idUsuario,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Eliminado")
            cone.close()

         except mysql.connector.Error as error:
              print("Error de Eliminacion de Datos {}" .format(error))
