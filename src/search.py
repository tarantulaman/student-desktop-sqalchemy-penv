from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *

class Search:


    # Creamos una funcion que va buscar los datos

    # data = este va a ser el dato por el cual se va a buscar en la base de datos el
    #        cual vamos a pasarle desde la caja de texto
    def search_student(data):


        engine = create_engine('sqlite:///student.db', echo=True)

        # Creamos la sesion
        Session = sessionmaker(bind=engine)
        session = Session()
        

        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        username = []
        firtsname = []
        lastname = []
        university = []

        

        # Aqui realizamos la busquema mediante varios campos, aqui usamos un like 
        # como en SQL , pero buscamos por varios campos usando or, como lo hariamos 
        # en SQL

        # all() = esto permite obtener toda la lista de datos que tiene similitud
        # or_( = esto indica que la conulta va usar OR y no AND
        # {} = esto permite agregar un valor dentro del mensaje
        # format() = permite pasarle un valor dentro de las llaves {}
        # data = aqui va el dato por el cual se va a buscar en la base de datos
        for student in session.query(Student).filter(or_(
            Student.username.like('%{}%'.format(data)),
            Student.firstname.like('%{}%'.format(data)), 
            Student.lastname.like('%{}%'.format(data)),
            Student.university.like('%{}%'.format(data)))).all():


            
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
