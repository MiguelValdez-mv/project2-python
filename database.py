from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./chinook.db",
    connect_args={"check_same_thread": False}
)

# Sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Obtiene una sesión de la base de datos 

    Retorna
    -------
    Session: Sesión de la base de datos
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
