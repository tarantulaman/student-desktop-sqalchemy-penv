from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *


# Creamos una clase la cual
class List:


    def list_student():


        engine = create_engine('sqlite:///student.db', echo=True)


        # Creamos una sesion
        Session = sessionmaker(bind=engine)
        session = Session()


        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        username = []
        firtsname = []
        lastname = []
        university = []



        # Recorremos el objeto donde almacena la informacion 

        # student = variable que almacena los datos obtenidos de nuestra consulta 
        for student in session.query(Student).order_by(Student.id):
            
            # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
            # que vamos obteniendo del for

            # append = permite crear un arreglo a partir de la obtencion de datos del for
            id.append(student.id)
            username.append(student.username)
            firtsname.append(student.firstname)
            lastname.append(student.lastname)
            university.append(student.university)


        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), (username), (firtsname), (lastname), (university)]



        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
    

    
    
 