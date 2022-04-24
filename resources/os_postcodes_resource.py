'''
test
'''

from typing import Dict
from flask_restful import Resource
from services.repositories.database.os_postcodes_repository import OS_POSTCODE_REPOSITORY_KEY, OSPostcodesRepository


class OSPostcodes(Resource):
    def get(self):
        '''
        A simple example get method
        '''
        result = self.osPostcodeRepository.get_within_extent()
        return result
        
    def __init__(self, **kwargs):
        super().__init__()
        self.osPostcodeRepository : OSPostcodesRepository = kwargs[OS_POSTCODE_REPOSITORY_KEY]
