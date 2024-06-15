from datetime import datetime, UTC
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

metadata = MetaData()

class Roles(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)

class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    role_id = Column(Integer, ForeignKey("role.id", ondelete="CASCADE"))
