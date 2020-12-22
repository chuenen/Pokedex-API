import os

import yaml


class Config:

    def __init__(self, settings):
        self._settings = settings

    @property
    def sqlalchemy_database_url(self):
        return 'mysql+pymysql://%(username)s:%(password)s' \
               '@%(host)s/%(database)s?charset=utf8mb4' \
               % self._settings['mysql']


def config():
    env = os.environ
    with open(env['SETTINGS_PATH']) as ymlfile:
        settings = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return Config(settings)

config = config()


# vi:et:ts=4:sw=4:cc=80
