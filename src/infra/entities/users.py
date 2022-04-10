from sqlalchemy import Column, String, Integer
from src.infra.config import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key = True) 
    public_id = Column(String(50), unique = True) 
    name = Column(String(100))
    user = Column(String(50), unique = True)
    password = Column(String(80))

    def __rep__(self):
        return f"User [name={self.name}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.password == other.password
        ):
            return True
        return False
