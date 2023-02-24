from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *

class Update:

    # Creamos una funcion que va actualizar los datos
    def update_student(id, username, firstname, lastname, university):

        engine = create_engine('sqlite:///student.db', echo=True)

        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        student = session.query(Student).filter(Student.id == id)
        student.update({Student.username: username})
        student.update({Student.firstname: firstname})
        student.update({Student.lastname: lastname})
        student.update({Student.university: university})

        
        # Hacemos un commit en la base de datos
        session.commit()
