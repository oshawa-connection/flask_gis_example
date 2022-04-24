'''
test
'''

from typing import Dict
from flask_restful import Resource
from flask_restful import reqparse


class HelloWorld(Resource):
    def get(self):
        '''
        A simple example get method
        '''
        
        return {"hello":"world"}

