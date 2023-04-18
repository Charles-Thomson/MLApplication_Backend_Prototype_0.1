"""Main functions associated with Database creation and managment"""
from sqlalchemy import create_engine, Column, CHAR, FLOAT, Table, MetaData, Select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Brain.brain_instance import BrainInstance

Base = declarative_base()

engine = create_engine("sqlite:///GenerationsDB.db", echo=True)

meta = MetaData()


class GenerationsTable(Base):
    """Base table creation"""

    __tablename__ = "generations"
    brain_id = Column("brain_id", CHAR, primary_key=True)
    generation_num = Column("generation_num", CHAR)
    hidden_weights = Column("hidden_weights", CHAR)
    output_weights = Column("output_weights", CHAR)
    fitness = Column("fitness", FLOAT)
    traversed_path = Column("traversed_path", CHAR)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)


def save_brain_instance(brain: BrainInstance):
    """Save a given set of data to the DB as a brain instance"""

    this_session = Session()

    brain.set_attributes_to_bytes()  # convert the weights to bytes from np.array
    print(f"Saving: {brain.brain_id}")
    this_session.add(brain)
    this_session.commit()


# def create_new_table(table_name: str) -> None:
#     """Create a for the new generation in the DB"""

#     GenerationsTable(
#         table_name,
#         meta,
#         Column("brain_key", CHAR, primary_key=True),
#         Column("hidden_weights", CHAR),
#         Column("output_weights", CHAR),
#         Column("fitness", FLOAT),
#     )


#     Base.metadata.create_all(bind=engine)


# def save_brain_instance(brain: BrainInstance):
#     """Save a given set of data to the DB as a brain instance"""

#     this_session = Session()

#     brain.set_attributes_to_bytes()  # convert the weights to bytes from np.array
#     print(f"Saving: {brain.brain_id}")
#     this_session.add(brain)
#     this_session.commit()


# this works
def get_db_data(generation_num: int) -> object:
    """Return the data stored in the DB"""
    session = Session()
    data = session.query(BrainInstance).filter(
        BrainInstance.generation_num == generation_num
    )
    return data


# if __name__ == "__main__":
#     create_new_table("test_table")
