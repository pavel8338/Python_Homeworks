"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle

class Car():
    def __init__(self, engine):
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine


