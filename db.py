from sqlalchemy import create_engine, MetaData, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd


# Creating a database engine.
engine = create_engine('sqlite:///metric_spaces.db', echo=True)

# Creating a metadata object.
metadata = MetaData()

# Creating a declarative base.
Base = declarative_base()


# Creating a class to represent the metric spaces table.
class MetricSpaces(Base):
    __tablename__ = 'metric_spaces'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    min_value = Column(Float)
    max_value = Column(Float)
    D = Column(String)
    
# Creating the metric spaces table.
Base.metadata.create_all(engine)

def save_metric_space(name, n, min_value, max_value, D):
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Saves a metric space in the database.

    Parameters:
    name (str): Name of the metric space.
    n (int): Number of points.
    min_value (float): Minimum value of the points.
    max_value (float): Maximum value of the points.
    D (str): Distance matrix of the metric space.

    Returns:
    None
    """
    metric_space = MetricSpaces(name=name, n=n, min_value=min_value, max_value=max_value, D=D)
    session.add(metric_space)
    session.commit()
    session.close()


def get_metric_spaces():
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    returns a dataframe with all the values of the metric spaces table.

    Parameters:
    None
    
    """
    metric_spaces = pd.read_sql_table('metric_spaces', engine)
    session.close()
    return metric_spaces

    





