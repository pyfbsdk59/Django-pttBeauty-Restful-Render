from sqlalchemy.sql import func  # type: ignore
from sqlalchemy import Column, Integer, String, DateTime, create_engine  # type: ignore
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore

Base = declarative_base()
DB_connect = "postgresql+psycopg2://root:2doigtwstock168uxi@localhost/postgres" 
#postgress為資料庫名稱，必須和settings.py和docker-compose.yml相同
#DB_connect = "postgresql+psycopg2://root:2doigtwstock168uxi@localhost/django"

class Images(Base):  # type: ignore
    __tablename__ = "Images"

    id = Column(Integer, primary_key=True)
    Url = Column(String)
    CreateDate = Column(DateTime(timezone=True), server_default=func.now())


if __name__ == "__main__":
    engine = create_engine(DB_connect, echo=True, future=True)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    #docker-compose run python sh -c "python3 manage.py migrate --run-syncdb" 跑這個整合資料庫
