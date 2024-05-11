import tkinter as tk

#importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *

class FormularioClientes: 
 
 global base
 base = None

 global textBoxId
 textBoxId = None

 global textBoxNombre
 textBoxNombre = None

 global textBoxApellido
 textBoxNombre = None

 global combo
 combo = None

 global groupBox
 groupBox = None

 global tree
 tree = None




def Formulario():
  
  global textBoxId
  global textBoxNombre
  global textBoxApellido
  global combo
  global base
  global groupBox
  global tree
  
  try:
     base = Tk()
     base.geometry("1200x300")
     base.title("Formulario Python")


     groupBox = LabelFrame(base, text="Datos del Personal", padx=5, pady=5)
     groupBox.grid(row=0, column=0, padx=10, pady=10)
     
     LableId = Label(groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
     textBoxId = Entry(groupBox)
     textBoxId.grid(row=0, column=1)

     LableNombre = Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
     textBoxNombre = Entry(groupBox)
     textBoxNombre.grid(row=1, column=1)
    
     LableApellido = Label(groupBox, text="Apellido:", width=13, font=("arial", 12)).grid(row=2, column=0)
     textBoxApellido = Entry(groupBox)
     textBoxApellido.grid(row=2, column=1)
     
     LableSexo = Label(groupBox, text="Sexo:", width=13, font=("arial", 12)).grid(row=3, column=0)
     seleccionSexo = tk.StringVar()
     combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
     combo.grid(row=3, column=1)
     seleccionSexo.set("Masculino")

     Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=4, column=0)
     Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=4, column=1)
     Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(row=4, column=2) 

     groupBox = LabelFrame(base, text="Lista de Personal", padx=5, pady=5,)
     groupBox.grid(row=0, column=1, padx=5, pady=5)
     #Treeview

     #Configuracion de Columnas
     tree = ttk.Treeview(groupBox, columns=("Id","Nombres","Apellidos","Sexo"), show='headings', height=5)
     tree.column("# 1", anchor=CENTER)
     tree.heading("# 1", text="Id")

     tree.column("# 2", anchor=CENTER)
     tree.heading("# 2", text="Nombres")

     tree.column("# 3", anchor=CENTER)
     tree.heading("# 3", text="Apellidos")

     tree.column("# 4", anchor=CENTER)
     tree.heading("# 4", text="Sexo")

     #Agregar datos a la tabla y mstrarla

     for row in CClientes.mostrarClientes():
        tree.insert("", "end", values=row)

      #Ejecutar la funcion hacer click
     tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

     tree.pack()



     base.mainloop()


  except ValueError as error:
        print("Error al mostrar la interfaz, error: {}".format(error))

def guardarRegistros():
   
   global textBoxNombre, textBoxApellido, combo, groupBox

   try:
      if textBoxNombre is None or textBoxApellido is None or combo is None:
         print("Los widgets no estan inicializados")
         return
      nombres = textBoxNombre.get()
      apellidos = textBoxApellido.get()
      sexo = combo.get()

      CClientes.ingresarClientes(nombres, apellidos, sexo)
      messagebox.showinfo("Informacion", "Los datos fueron guardados")

      actualizarTreeView()


      #Limpiar campos   
      textBoxNombre.delete(0,END)
      textBoxApellido.delete(0,END)
   
   except ValueError as error:
      print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
   global tree

   try:
      tree.delete(*tree.get_children())

      datos = CClientes.mostrarClientes()

      for row in CClientes.mostrarClientes():
        tree.insert("", "end", values=row)

   except ValueError as error:
      print("Error al mostrar los datos {}".format(error))

def seleccionarRegistro(event):
   try:
      itemSeleccionado = tree.focus()

      if itemSeleccionado:
         values = tree.item(itemSeleccionado)['values']

         textBoxId.delete(0,END)
         textBoxId.insert(0, values[0])

         textBoxNombre.delete(0,END)
         textBoxNombre.insert(0, values[1])

         textBoxApellido.delete(0,END)
         textBoxApellido.insert(0, values[2])

         combo.set(values[3])
   
   except ValueError as error:
      print("Error al seleccionar los datos {}".format(error))

def modificarRegistros():
   
   global textBoxId,textBoxNombre, textBoxApellido, combo, groupBox

   try:
      if textBoxId is None or textBoxNombre is None or textBoxApellido is None or combo is None:
         print("Los widgets no estan inicializados")
         return
      
      idUsuario = textBoxId.get()
      nombres = textBoxNombre.get()
      apellidos = textBoxApellido.get()
      sexo = combo.get()

      CClientes.modificarClientes(idUsuario,nombres, apellidos, sexo)
      messagebox.showinfo("Informacion", "Los datos fueron actualizados")

      actualizarTreeView()


      #Limpiar campos   
      textBoxNombre.delete(0,END)
      textBoxApellido.delete(0,END)
   
   except ValueError as error:
      print("Error al modificar los datos {}".format(error))

def eliminarRegistros():
   
   global textBoxId, textBoxNombre, textBoxApellido

   try:
      if textBoxId is None:
         print("Los widgets no estan inicializados")
         return
      
      idUsuario = textBoxId.get()
      nombres = textBoxNombre.get()
      apellidos = textBoxApellido.get()
      sexo = combo.get()

      CClientes.eliminarClientes(idUsuario)
      messagebox.showinfo("Informacion", "Los datos fueron eliminados")

      actualizarTreeView()


      #Limpiar campos   
      textBoxNombre.delete(0,END)
      textBoxApellido.delete(0,END)
   
   except ValueError as error:
      print("Error al modificar los datos {}".format(error))

Formulario()