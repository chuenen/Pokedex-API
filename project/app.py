import connexion
from flask import jsonify

from .exceptions import PokemonNotFound, DeletionDeined


def create_app(config):
    _app = connexion.App(__name__)
    _app.add_api('v1.yml')
    _app.add_error_handler(PokemonNotFound, render_not_found)
    _app.add_error_handler(DeletionDeined, render_deletion_deined)
    app = _app.app

    return app

def render_not_found(error):
    return jsonify({
        'detail': f'{error}',
        'status': 404,
        'title': 'Not Found',
    }), 404

def render_deletion_deined(error):
    return jsonify({
        'detail': f'{error}',
        'status': 403,
        'title': 'Deletion Deined',
    }), 403



# vi:et:ts=4:sw=4:cc=80
