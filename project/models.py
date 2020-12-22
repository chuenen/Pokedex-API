import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Pokemon(Base):
    __tablename__ = 'pokemon'
    _id = Column('id', Integer, primary_key=True)

    number = Column(String)
    name = Column(String)

    types = relationship('Type', secondary='pokemon_type', backref='pokemon')
    evolutions = relationship(
        'Evolution', primaryjoin='Pokemon._id==Evolution.pokemon_id')

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        self._disabled = disabled

    @property
    def data(self):
        return {
            'number': self.number,
            'name': self.name,
            'types': [type_.name for type_ in self.types],
        }

    def to_dict(self):
        data = self.data
        if self.evolutions:
            data['evolutions'] = [evolution.pokemon.data for evolution in self.evolutions]
        return data


class Type(Base):
    __tablename__ = 'type'
    _id = Column('id', Integer, primary_key=True)

    name = Column(String)


class PokemonType(Base):
    __tablename__ = 'pokemon_type'
    _id = Column('id', Integer, primary_key=True)

    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    type_id = Column(Integer, ForeignKey('type.id'))


class Evolution(Base):
    __tablename__ = 'evolution'
    _id = Column('id', Integer, primary_key=True)

    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    evolution_id = Column(Integer, ForeignKey('pokemon.id'))

    pokemon = relationship('Pokemon', foreign_keys=[evolution_id])


# vi:et:ts=4:sw=4:cc=80
