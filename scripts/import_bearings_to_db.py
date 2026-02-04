import json
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Bearing(Base):
    __tablename__ = "bearings"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(String)
    type = Column(String)

    def __repr__(self):
        return f"<Bearing(name='{self.name}', size='{self.size}', type='{self.type}')>"


DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def import_bearings(file_path):
    with open(file_path, "r") as file:
        bearings_data = json.load(file)

    session = Session()
    for bearing in bearings_data:
        new_bearing = Bearing(
            name=bearing["name"], size=bearing["size"], type=bearing["type"]
        )
        session.add(new_bearing)
    session.commit()
    session.close()


if __name__ == "__main__":
    import_bearings("bearings.json")