from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import *

class Delete:

    # Creamos una funcion que va actualizar los datos
    def delete_student(id):

        engine = create_engine('sqlite:///student.db', echo=True)

        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create objects  
        student = session.query(Student).filter(Student.id == id)
        student.delete()

        
        # Hacemos un commit en la base de datos
        session.commit()