class PokedexError(Exception):
    pass


class PokemonNotFound(PokedexError):

    def __init__(self, obj, id_):
        print(obj.__table__)
        msg = f'{obj.__table__} (id={id_}) not found'
        super().__init__(msg)


class DeletionDeined(PokedexError):

    def __init__(self):
        msg = 'Can not be deleted. It is an evolution of other Pokemon'
        super().__init__(msg)
