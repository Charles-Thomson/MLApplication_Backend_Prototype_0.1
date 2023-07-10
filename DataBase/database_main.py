"""Main functions associated with Database creation and managment"""
from sqlalchemy import create_engine, Column, CHAR, FLOAT, Table, MetaData, Select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Brain.brain_instance import BrainInstance

Base = declarative_base()

engine = create_engine("sqlite:///GenerationsDB.db", echo=False)

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
    # print(f"Saving: {brain.brain_id}")
    this_session.add(brain)
    this_session.commit()


# YH need to do this to clear the DB tble for each new map
def clear_DB() -> None:
    """Clear the DB"""


def get_and_format_db_data(generation_num: int) -> list[BrainInstance]:
    """Pull and format the relervent Brain instnce generation from the database"""
    brain_instances: list[BrainInstance] = []
    data = get_db_data(generation_num)
    for instance in data:
        instance.get_attributes_from_bytes()
        brain_instances.append(instance)

    ordered_brian_instances: list[BrainInstance] = sorted(
        brain_instances, key=lambda x: x.fitness, reverse=True
    )

    return ordered_brian_instances


# ***** USED IN RETURN DATA *****


def get_highest_fitness_from_gen(generation_num: int) -> list[BrainInstance]:
    """Pull and format the relervent Brain instnce generation from the database"""
    brain_instances: list[BrainInstance] = []
    data = get_db_data(generation_num)
    for instance in data:
        instance.get_attributes_from_bytes()
        brain_instances.append(instance)

    ordered_brian_instances: list[BrainInstance] = sorted(
        brain_instances, key=lambda x: x.fitness, reverse=True
    )

    return ordered_brian_instances[0]


def get_lowest_fitness_from_gen(generation_num: int) -> list[BrainInstance]:
    """Pull and format the relervent Brain instnce generation from the database"""
    brain_instances: list[BrainInstance] = []
    data = get_db_data(generation_num)
    for instance in data:
        instance.get_attributes_from_bytes()
        brain_instances.append(instance)

    ordered_brian_instances: list[BrainInstance] = sorted(
        brain_instances, key=lambda x: x.fitness, reverse=False
    )

    return ordered_brian_instances[0]


# this works
def get_db_data(generation_num: int) -> object:
    """Return the data stored in the DB"""
    session = Session()
    data = session.query(BrainInstance).filter(
        BrainInstance.generation_num == generation_num
    )
    session.expunge_all()
    session.close()

    return data
