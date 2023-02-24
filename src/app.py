# IMPORTANDO MODULOS


# Importamos la biblioteca de Tkinter que permite diseñar
# toda la interfaz

# ttk = biblioteca de Tkinter que permite diseñar toda la interfaz
from tkinter import ttk


# Importamos todo el modulo de Tkinter

# tkinter = permite crear interfaces de Escritorio con Python
from tkinter import *


# Importamos el modulo de Message Box

# messagebox = este modulo permite mostrar mensajes de dialogo, lo
#              vamos a usar para eliminar los datos
from tkinter import messagebox


# Importamos el modulo de Tkinter nuevamente, para poder
# agregat el scroll a treeview
import tkinter as tk


# Importamos las clases donde se va a realizar un CRUD

# list = se refiere al archivo "src/list.py"
# List = nombre de la clase que contiene "src/list.py"
from list import List
from insert import Insert
from update import Update
from delete import Delete
from search import Search











class Ventana:


    # Creamos una funcion, para crear un constructor de la clase "Ventana"

    # self = es una referencia al instancia actual de la clase, y se utiliza para acceder
    #        a las variables que pertenecen a la clase, podemos llámarlo como queramos, pero
    #        tiene que ser el primer parámetro de cualquier función en la clase

    # window = parametro que espera recibir el constructor de la clase y que tendra la
    #          iniciacion del metodo que va a arrancar la ventana
    def __init__(self, window):



        



        # Almacenamos el parametro "window" que recibe el constructor en un propiedad llamada
        # "self.wind"

        # self. = primer parametro del contructor y hace referencia a la instancia actual
        #         de la clase

        # .wind = propiedad donde se va almacenar lo que reciba el parametro "window", puede
        #         tener cualquier nombre
        self.wind = window



        # Añadimos un titulo a la ventana
        self.wind.title('Student Application')




       



        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario

        # self.wind = aqui indicamos donde va a estar posicionado el Frame, aqui le estamos
        #             indicando que va a estar dentro de la ventana "window"

        # text = '' = aqui le estoy indicando el titulo que va a tener
        #             el Frame, aqui no va a tener titulo
        frame = LabelFrame(self.wind, text = '')




        # Ahora posicionamoe el Frame que hemos creado

        # frame = variable que almacena el Frame que anteriormente hemos creado

        # grid = metodo que nos permite indicar en que posicion de la ventana va a estar nuestro boton
        #        o entrada de texto, esto es una grilla invisible, que nos ayudara a colocar  nuestros
        #        elementos de acuerdo a la posicion que queramos

        # row=0 = esto indica que este elemento va a estar en la fila 0 de nuestra grilla, el valor
        #         se lo indica en pixeles

        # column=0 = esto indica que este elemento va a estar en la columna 0 de nuestra grilla

        # columnspan=3 = esto indica cuantas columnas de nuestra grilla va abarcar nuestra ventana
        #                es decir va a ser columnas vacias sin nada de contenido, es decir con esto vamos
        #                a centrar el frame

        # pady=20= esto es un padding, indica un espaciado ineterno de cada elemento, para que los elementos no
        #          se vean tan juntos, aqui le indicamos en pixeles el espaciado de arriba y abajo
        frame.grid(row=0, column=0, columnspan=3, pady=5, sticky = W)





        # Creamos los botones que van a realizar el CRUD
        ttk.Button(frame, text='Add', command=self.add_window).grid(row=0, column=0, sticky = W)
        ttk.Button(frame, text='Update', command=self.update_window).grid(row=0, column=1, sticky = W)
        ttk.Button(frame, text='Delete', command=self.delete_window).grid(row=0, column=2, sticky = W)






        # Creamos un label y un campo de texto donde podremos buscar algun dato
        # que necesitemos
        Label(frame, text = 'Search:').grid(row=0, column=3)

        entry_t = Entry(frame)
        entry_t.grid(row=0, column=4, sticky = W)
        entry_t.bind('<KeyRelease>', self.scankey_t)
        









        # Creamos un label que va a funcionar como mensaje despues de realizar una accion

        # Creamos el label y lo almacenamos en una propiedad con el nombre de "message"

        # text='' = aqui no le pasamos ningun texto ya que desde las otras funciones le vamos 
        #           a pasar un texto propio que queramos

        # fg='green' = esto indica el color que va a tener el mensaje
        self.message = Label(text='', fg='green')

        # Posicionamos el label dentro del Frame
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)







        # Creamos una tabla para que liste los datos

        # Guardamos la tabla en una propieedad de la clase

        # .tree = nombre de la tabla que va a ser llamada en diferentes funciones
        # ttk.Treeview = esto permite crear una tabla o grilla desde Tkinter
        # height=10 = estas son la cantidad de filas que va a mostrar la tabla
        # columns=("Firtsname", "Lastname") =  estas son la cantidad de columnas que va a mostrar la tabla
        self.tree = ttk.Treeview(height=10, columns=('#1', '#2', '#3', '#4', '#5'))

        # Ahora damos una posicion a la tabla para que se muestre
        self.tree.grid(row=4, column=0, columnspan=2)




        # Ahora agregamos encabezados a la tabla

        # '#0' = esto indica el numero de columna donde va a ir el encabezado
        # text= 'Username' = este va a ser el nombre que el encabezado va a mostrar
        # anchor=CENTER = esto es para indicarle que el encabezado vaya centrado
        self.tree.heading('#0', text= 'N°', anchor=CENTER) 
        self.tree.heading('#1', text= '', anchor=CENTER)
        self.tree.heading('#2', text= 'Username', anchor=CENTER)
        self.tree.heading('#3', text= 'Firstname', anchor=CENTER)
        self.tree.heading('#4', text= 'Lastname', anchor=CENTER)
        self.tree.heading('#5', text= 'University', anchor=CENTER)



        # Cambiamos el tamaño de las columnas para que no se vea tan separado
        self.tree.column('#0', width=40)

        # stretch=NO = con esto evitamos que la columna se muestre, esta es la columna del id, y la
        #              necesitamos para actualizar los datos
        self.tree.column('#1', width=0, stretch=NO)
        self.tree.column('#2', width=120)
        self.tree.column('#3', width=120)
        self.tree.column('#4', width=120)
        self.tree.column('#5', width=120)

        
        
        # Ahora agregamos unn scrollbar a la lista 
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=4, column=2, sticky='ns')

       


        # Llamamos a la funcion para obtener la lista de productos
        self.get_students()









    







    # Creamos una funcion para obtener la lista de productos
    def get_students(self):
    
        
        # Obtenemos todos los elementos de la tabla, con la finalidad de realizar
        # una limpieza de la tabla, en el caso que exista algun dato

        # .tree = nombre de la tabal que hemos creado anteriormente
        # get_children() = este metodo permite obtener los datos de la tabla
        records = self.tree.get_children()





        # Recorremos los elementos de la tabla para poder limpiarlos

        # Medinte un loop o for recorremos los elementos

        # element = variable que va a eliminar cada elemento de la tabla
        for element in records:
            # Eliminamos cada elemento de la tabla

            # delete() = metodo que permite eliminar elementos de la tabla
            self.tree.delete(element)

        




        # LLamamos a la funcion list_student(), que va a traer la lista de
        # estudiantes de la base de datos
        lista = List.list_student()

    



        # Creamos un contador y lo iniciamos, con la finalidad de saber la cantidad de datos
        # que tenemos registrados
        self.i = 1

       
        

        # LLenamos los datos obtenidos de la consulta en la tabla

        # a,b,c,d = variables que almacenan los datos obtenidos de nuestra consulta
        for a,b,c,d,e in zip(*lista): 

            # Insertamos los datos de nuestra conulta en la tabla

            # insert() = este metodo permirte insertar valores dentro de la tabla

            # '', 0 = aqui le indicamos que la posicion 0 de la consulta, no inserte ningun valor
            #         en la tabla

            # text = self.i = aqui le indicamos que el contador lo inserte en la posicion 0 de la 
            #                 tabla como texto

            # values = row[2] = aqui le indicamos que la posicion 2 de la consulta, inserte en la 
            #                   tabla como valor, aqui otenemos el precio del producto
            self.tree.insert('', 0, text = self.i, values = (a, b, c, d, e))

            # Incrementamos el contador creado anteriormente
            self.i = self.i + 1


        






















   
    # FUNCIONES PARA MOSTRAR LAS VENTANAS


    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # ingresar los datos
    def add_window(self):

        # Aqui abrimos una nueva ventana para agergar los datos

        # Creamos una ventana encima de la anterior y la almacenamos en una variable

        # self.edit_wind = variable que va almacenar la nueva variable
        # Toplevel() = esto crea una ventana encima de la anterior
        self.add_window = Toplevel()

        # Creamos un titulo para la nueva ventana y la almacenamos en una variable
        self.add_window.title = 'Add Student'




        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario

        # self.wind = aqui indicamos donde va a estar posicionado el Frame, aqui le estamos
        #             indicando que va a estar dentro de la ventana "window"

        # text = 'Register a new product' = aqui le estoy indicando el titulo que va a tener
        #                                   el Frame
        frame = LabelFrame(self.add_window, text = 'Register a new student')




        # Ahora posicionamoe el Frame que hemos creado

        # frame = variable que almacena el Frame que anteriormente hemos creado

        # grid = metodo que nos permite indicar en que posicion de la ventana va a estar nuestro boton
        #        o entrada de texto, esto es una grilla invisible, que nos ayudara a colocar  nuestros
        #        elementos de acuerdo a la posicion que queramos

        # row=0 = esto indica que este elemento va a estar en la fila 0 de nuestra grilla, el valor
        #         se lo indica en pixeles

        # column=0 = esto indica que este elemento va a estar en la columna 0 de nuestra grilla

        # columnspan=3 = esto indica cuantas columnas de nuestra grilla va abarcar nuestra ventana
        #                es decir va a ser columnas vacias sin nada de contenido, es decir con esto vamos
        #                a centrar el frame

        # pady=20= esto es un padding, indica un espaciado ineterno de cada elemento, para que los elementos no
        #          se vean tan juntos, aqui le indicamos en pixeles el espaciado de arriba y abajo
        frame.grid(row=0, column=0, columnspan=3, pady=20)





        # Creamos un label y una caja de texto para ingresar el nuevo "username"

        # Label = permite crear un texto en la ventana

        # frame = aqui indicamos donde va a estar posicionado el Label, aqui le estamos
        #         indicando que va a estar dentro del Frame que hemos creado anteriormente

        # text='Username: ' = aqui le estoy indicando el texto del label

        # grid() = esto permite posicionar el elemento Label(), como anteriormente se ha hecho
        #          con el frame
        Label(frame, text = 'Username:').grid(row = 1, column = 1)

        # Creamos un campo de entrada para ingresar el username

        # username = aqui guardamos el campo de texto en una variable

        # Entry(frame) = esto representa una entrada, es decir una caja de texto donde
        #              insertaremos los valores
        username = Entry(frame)

        # Ahora posicionamos el campo de entrada
        username.grid(row = 1, column = 2)

        


        # Creamos un label y una caja de texto para ingresar el nuevo "firstname"
        Label(frame, text = 'Firstname:').grid(row = 3, column = 1)
        firstname= Entry(frame)
        firstname.grid(row = 3, column = 2)

        # Creamos un label y una caja de texto para ingresar el nuevo "lastname"
        Label(frame, text = 'Lastname:').grid(row = 5, column = 1)
        lastname= Entry(frame)
        lastname.grid(row = 5, column = 2)

        # Creamos un label y una caja de texto para ingresar el nuevo "lastname"
        Label(frame, text = 'University:').grid(row = 7, column = 1)
        university= Entry(frame)
        university.grid(row = 7, column = 2)



        # Creamos un label que va a funcionar como mensaje despues de realizar una accion
        self.message_aw = Label(frame, text='', fg='red')
        self.message_aw.grid(row=8, column=2, sticky=W+E)



        # Creamos un boton para poder insertar los datos

        # lambda = permite ejecutar una funcion en esta misma ventana
        # add_student() = funcion que va a permitir insertar los datos
        # username.get(), firstname.get()....) = son parametros que espera recibir la funcion
        # sticky=W+E = esto indica que abarque todo el ancho posible de nuestra ventana, de Oeste a Este
        Button(frame, text = 'Add', command = lambda: self.add_student(
            username.get(), firstname.get(), lastname.get(), university.get())).grid(row = 9, column = 2, sticky=W+E)
        
        # Ejecutamos los eventos de la ventana
        self.add_window.mainloop()









    # Creamos una funcion para mostrar una ventana flotante en donde vamos a
    # editar los datos
    def update_window(self):

        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar

        # En el caso que se haya selleccionado una fila de datos, vamos a obtener los
        # datos y los almacenamos en variables
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            username = self.tree.item(self.tree.selection())['values'][1]
            firstname = self.tree.item(self.tree.selection())['values'][2]
            lastname = self.tree.item(self.tree.selection())['values'][3]
            university = self.tree.item(self.tree.selection())['values'][4]

        # Mostramos un mensaje de error para que el usuario seleccione una fila de datos
        # que necesita editar
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return




        # Aqui abrimos una nueva ventana para editar los datos
        self.update_window = Toplevel()
        self.update_window.title = 'Edit Student'

        # Creamos un Frame que va a funcionar como contenedor y lo almacenamos en una
        # variable para posicionarlo, este Frame lo creamos para que muestre un contorno
        # en nuestro formulario
        frame = LabelFrame(self.update_window, text = 'Update student')

        # Ahora posicionamos el Frame que hemos creado
        frame.grid(row=0, column=0, columnspan=3, pady=20)


        # Creamos los labels y cajas de texto
        Label(frame, text = 'Username:').grid(row = 1, column = 1)
        username = Entry(frame, textvariable = StringVar(frame, value = username))
        username.grid(row = 1, column = 2)

        Label(frame, text = 'Firstname:').grid(row = 3, column = 1)
        firstname= Entry(frame, textvariable = StringVar(frame, value = firstname))
        firstname.grid(row = 3, column = 2)
        
        Label(frame, text = 'Lastname:').grid(row = 5, column = 1)
        lastname= Entry(frame, textvariable = StringVar(frame, value = lastname))
        lastname.grid(row = 5, column = 2)
       
        Label(frame, text = 'University:').grid(row = 7, column = 1)
        university= Entry(frame, textvariable = StringVar(frame, value = university))
        university.grid(row = 7, column = 2)


        # Creamos un label que va a funcionar como mensaje despues de realizar una accion
        self.message_uw = Label(frame, text='', fg='red')
        self.message_uw.grid(row=8, column=2, sticky=W+E)


        # Creamos un boton para poder insertar los datos
        Button(frame, text = 'Update', command = lambda: self.update_student(
            id, username.get(), firstname.get(), lastname.get(), university.get())).grid(row = 9, column = 2, sticky=W+E)
        
        # Ejecutamos los eventos de la ventana
        self.update_window.mainloop()








    # Creamos una funcion para mostrar un mensaje en donde vamos a
    # eliminar los datos
    def delete_window(self):


        # Realizamos una limpieza de nuestro mensaje o label, en el caso que tenga algun dato
        self.message['text'] = ''

        # Creamos un try-catch, para evitar errores, en el caso que el usuario no  haya
        # seleccionado ningun dato para actualizar
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
          
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return



        # Mostramos un mensaje de dialogo, para decidir si eliminamos o no los datos
        res = messagebox.askquestion('Exit Application', 'Deseas eliminar este dato')
        
        if res == 'yes' :

            # Ejecutamos la funcion para eliminar los datos pasandole el id
            self.delete_student(id)

            messagebox.OK

            # LLamamos al label que va a actuar commo mensaje
            self.message['text'] = 'Student deleted successfully'
            
        else :
            messagebox.CANCEL























    # FUNCIONES PARA REALIZAR EL CRUD 

   
    # Creamos una funcion que va a llamar a la funcion de insercion de los datos
    # ubicada en src/insert.py
    def add_student(self, username, firstname, lastname, university):


        # LLamamos a la funcion de validacion_add_window(), para comprobar que el usuario esta ingresando
        # los datos en las cajas de texto

        # validation_add_window() = esta funcion como primer valor va a retornar un true, caso contrario un false
        if self.validation_add_window(username, firstname, lastname, university):

            # Llamamos a la funcion add_student(), de la clase Insert, ubicada en el archivo
            # src/insert.py, la cual va a permitir insertar los datos

            # username, firstname... = estos son los valores que vamos a insertar
            Insert.add_student(username, firstname, lastname, university)

            # Cerramos la ventana una vez que se actualicen los datos
            self.add_window.destroy()


            # LLamamos al label que va a actuar commo mensaje para indicar que el registro se ha insertado

            # message['text'] = llamamos a la propiedad "text" del label, para poder pasarle el mensaje que
            #                   queremos mostrar

            # {} = esto permite agregar un valor dentro del mensaje

            # format() = permite pasarle un valor dentro de las llaves {}
            self.message['text'] = 'Student added successfully'


            # LLamamos a la funcion get_students(), para que se actualicen los datos despues que
            # ingresemos
            self.get_students()

       

       



        



    # Creamos una funcion que va a llamar a la funcion de actualizacion de los datos
    # ubicada en src/update.py
    def update_student(self, id, username, firstname, lastname, university):

        # LLamamos a la funcion de validacion_update_window(), para comprobar que el usuario esta ingresando
        # los datos en las cajas de texto

        # validation_update_window() = esta funcion como primer valor va a retornar un true, caso contrario un false
        if self.validation_update_window(username, firstname, lastname, university):

            # Llamamos a la funcion add_student(), de la clase Update, ubicada en el archivo
            # src/update.py, la cual va a permitir actualizar los datos

            # username, firstname... = estos son los valores que vamos a insertar

            Update.update_student(id, username, firstname, lastname, university)

            # Cerramos la ventana una vez que se actualicen los datos
            self.update_window.destroy()

            # LLamamos al label que va a actuar commo mensaje
            self.message['text'] = 'Student updated successfully'

            # LLamamos a la funcion get_students(), para que se actualicen los datos despues que
            # ingresemos
            self.get_students()

    






    # Creamos una funcion que va a llamar a la funcion de eliminacion de los datos
    # ubicada en src/delete.py
    def delete_student(self, id):

        Delete.delete_student(id)

        # LLamamos a la funcion get_students(), para que se actualicen los datos despues que
        # ingresemos
        self.get_students()







   
    # Creamos una funcion que permite buscar en la base de datos por un dato que ingresemos
    def search_student(self, data):

        # Aqui aplicamos lo mismo que usamos al obtener la lista de datos

        records = self.tree.get_children()

        for element in records:
            self.tree.delete(element)

        # Llamamos a la funcion search_student(), de la clase Search, ubicada en el archivo
        # src/search.py

        # data = este es el valor por el cual vamos a buscar en la base de datos
        lista_search = Search.search_student(data)

    
        self.i = 1


        for a,b,c,d,e in zip(*lista_search): 

            self.tree.insert('', 0, text = self.i, values = (a, b, c, d, e))
            self.i = self.i + 1






    # Creamos una funcion la cual va a permitir obtener el valor que ingresemos en la
    # caja de texto de una forma rapida
    def scankey_t(self, event):
        
        # Obtenemos el dato que ingresamos en la caja de texto
        # en tiempo real

        # event.widget.get() = permite obtener el valor ingresado en la caja de texto en 
        #                      tiempo real
        val = event.widget.get()

        


        # Validamos si no existe ningun valor en la caja de texto, mostraremos
        # toda la lista de datos
        if val == '':
            self.get_students()
        # Caso contrario pasamos el dato que hemos ingresado en la caja de texto
        # para que busque en la base de datos
        else:
            self.search_student(val)






















    # FUNCIONES QUE VAN A VALIDAR LAS CAJAS DE TEXTO


    # Creamos una funcion que va a permitir validar que las cajas de texto no esten vacias
    # en el formulario de agregar estudiante
    def validation_add_window(self, username, firstname, lastname, university):

        # Validamos que las cajas de texto no no esten vacias

        # len = metodo que permite obtener la longitud de un elemento
        # == 0 = aqui le indicamos que la longitud del valor ingresado sea igual a 0
        if(len(username) == 0):

            # LLamamos al label que va a actuar commo mensaje para indicar que el registro se ha insertado
            self.message_aw['text'] = 'Username is required'
        
        elif(len(firstname) == 0):

            self.message_aw['text'] = 'Firstname is required'

        elif(len(lastname) == 0):

            self.message_aw['text'] = 'Lastname is required'
        
        elif(len(university) == 0):

            self.message_aw['text'] = 'University is required'

        # Caso contrario retornamos los valores de los datos para insertarlos
        else:
            return username and firstname and lastname and university






    # Creamos una funcion que va a permitir validar que las cajas de texto no esten vacias
    # en el formulario de actualizar estudiante
    def validation_update_window(self, username, firstname, lastname, university):

        if(len(username) == 0):

            self.message_uw['text'] = 'Username is required'
        
        elif(len(firstname) == 0):

            self.message_uw['text'] = 'Firstname is required'

        elif(len(lastname) == 0):

            self.message_uw['text'] = 'Lastname is required'
        
        elif(len(university) == 0):

            self.message_uw['text'] = 'University is required'

        else:
            return username and firstname and lastname and university
        









# ARRANCANDO LA APLICACION

# Comprobamos si este archivo es con el que va arrancar nuetra aplicacion
# para despues mostrar la ventana con interfaz grafica
if __name__ == '__main__':

    # Iniciando el modulo que va arrancar la ventana y almacenandolo
    # en una variable

    # Tk() = este sera el modulo con el que va a iniciar nuestra ventana y que hemos
    #        importado inicialmente
    window = Tk()

    

    # Instanciamos a la clase "Product" y la almacenamos en una variable

    # window = parametro que le pasamos a la clase "Product", la cual contendra el
    #          arranque de la ventana
    application = Ventana(window)



    # Arrrancamos la ventana

    # window.mainloop () = le dice a Python que ejecute el ciclo de eventos Tkinter.
    #                      Este método detecta eventos, como clics de botones o
    #                      pulsaciones de teclas, y bloquea la ejecución de cualquier
    #                      código que venga después hasta que se cierra la ventana a
    #                      la que se llama.
    window.mainloop()
