from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler():
    """ sqlalchemy database connection """

    def __init__(self):
        self.__connection_string = "mysql+pymysql://root:senha@127.0.0.1:3306/siscam"
        self.session = None

    def get_engine(self):
      
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()