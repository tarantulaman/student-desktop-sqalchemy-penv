from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *

class Insert:

    # Creamos una funcion que va a insertar los datos
    def add_student(username, firstname, lastname, university):

        engine = create_engine('sqlite:///student.db', echo=True)

        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        student = Student(username,firstname,lastname,university)
        session.add(student)

        
        # Hacemos un commit en la base de datos
        session.commit()
