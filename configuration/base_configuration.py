# pylint: disable=invalid-name

'''
Contains abstract definition of configuration for the flask app.
'''
from abc import ABC
import os
from dataclasses import dataclass


@dataclass
class BaseConfiguration(ABC):
    '''
    hello owrld
    '''

    _db_env_var_key = "DATABASE_URL"

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    def __init__(self):
        db_url_env_var = os.environ.get(self._db_env_var_key)
        if db_url_env_var is None:
            raise EnvironmentError(f"{self._db_env_var_key} environment var must be set")
        self.SQLALCHEMY_DATABASE_URI = db_url_env_var
