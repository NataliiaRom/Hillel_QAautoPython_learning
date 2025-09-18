from sqlalchemy.orm import sessionmaker
from creating_tables import engine

# creating the session constructor
Session = sessionmaker(bind=engine)
# creating a session instance
session = Session()