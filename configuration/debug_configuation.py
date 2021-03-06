'''
Contains the debug configuration class
'''
from .base_configuration import BaseConfiguration
from dataclasses import dataclass

@dataclass
class DebugConfiguration(BaseConfiguration):
    '''
    Configuration for debugging app during development
    '''
    DEBUG = True

    def __init__(self):
        super().__init__()
