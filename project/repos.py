from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_

from .db import get_session
from .models import Pokemon, Type, Evolution
from .exceptions import PokemonNotFound, DeletionDeined


class BaseRepository:

    MODEL_CLS = None

    @property
    def _session(self):
        return get_session()

    def get(self, id_):
        try:
            return self._session.query(self.MODEL_CLS).filter_by(_id=id_).one()
        except NoResultFound:
            raise PokemonNotFound(self.MODEL_CLS, id_)

    def add(self, entity):
        self._session.add(entity)
        self._session.flush()
        return entity

    def list(self):
        return self._session.query(self.MODEL_CLS).all()


class TypeRepository(BaseRepository):

    MODEL_CLS = Type

    def get_or_create(self, name):
        type_ = self._session.query(self.MODEL_CLS) \
            .filter_by(name=name) \
            .one_or_none()
        if not type_:
            type_ = self.MODEL_CLS(name=name)
            self.add(type_)
        return type_


class PokemonRepository(BaseRepository):

    MODEL_CLS = Pokemon

    def find(self, type_):
        return self._session.query(self.MODEL_CLS) \
            .join(self.MODEL_CLS.types).filter_by(name=type_).all()

    def remove(self, id_):
        pokemon = self.get(id_)
        evolutions = evolution_repo.find(evolution_id=id_)
        if evolutions:
            raise DeletionDeined
        if not pokemon:
            return
        self._session.delete(pokemon)


class EvolutionRepository(BaseRepository):

    MODEL_CLS = Evolution

    def get(self, pokemon_id=None, evolution_id=None):
        return self._session.query(self.MODEL_CLS) \
            .filter_by(pokemon_id=pokemon_id, evolution_id=evolution_id) \
            .one_or_none()

    def find(self, evolution_id):
        return self._session.query(self.MODEL_CLS) \
            .filter_by(evolution_id=evolution_id).all()

    def remove(self, pokemon_id, evolution_id):
        evolution = self.get(pokemon_id, evolution_id)
        if not evolution:
            return
        self._session.delete(evolution)


pokemon_repo = PokemonRepository()
type_repo = TypeRepository()
evolution_repo = EvolutionRepository()


# vi:et:ts=4:sw=4:cc=80
