from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#---Database connection---
# -> "postgres" is the database user.
# -> "12345" is the password for the database user.
# -> "localhost" is the host where the database is running.
# -> "Quiz" is the name of the database.# The "echo=True" parameter enables verbose logging, useful for debugging.
# The "pool_pre_ping=True" parameter enables the engine to check the connection health 
#        before returning a connection from the pool.
# The "create_engine" function is part of SQLAlchemy and is used to create a database engine 
#        which serves as a source of connectivity to the database and manages database connections..
engine = create_engine("postgresql://postgres:12345@localhost/Quiz",echo=True,pool_pre_ping=True)

#Create a SessionLocal instance using the sessionmaker.
#This will be used to create database sessions.
# -> "autocommit=False" disables automatic commit of transactions.
# -> "autoflush=False" disables automatic flushing of changes to the database.
# -> "bind=engine" binds the session to the database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base for database models.
# This will be used as a base class for all models.
Base = declarative_base()
