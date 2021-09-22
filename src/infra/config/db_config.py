from sqlalchemy import create_engine


class DBConnectionHandler:
    """SqlAlchemy database connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///projeto.db"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection do Database
        """
        engine = create_engine(self.__connection_string)
        return engine
