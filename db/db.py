import os
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker