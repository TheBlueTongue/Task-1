from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from flask_login import UserMixin
from datetime import datetime

# Define a consistent path for the SQLite database file
DATABASE_URL = 'sqlite:///persistent_database.db'

# Set up the engine and base
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    tasks = relationship('Task', back_populates='owner')

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    category = Column(String(50), nullable=False)
    due_date = Column(Date, nullable=True)
    is_complete = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('User', back_populates='tasks')

# Create tables if they don't already exist
Base.metadata.create_all(bind=engine)