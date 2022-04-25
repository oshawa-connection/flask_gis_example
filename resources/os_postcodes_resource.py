from flask import request
from flask_restful import Resource, reqparse
from constants import MAX_BBOX_AREA_METRES_SQUARED
from models.extent import Extent
from services.repositories.database.os_postcodes_repository import OS_POSTCODE_REPOSITORY_KEY, OSPostcodesRepository
from werkzeug.exceptions import BadRequest

class OSPostcodes(Resource):
    def get(self):
        '''
        Gets some postcode data given an extent as a comma seperated string.
        '''
        extent_string = request.args.get('extent')
        if extent_string is None:
            return {'message': 'You must specify an exent'}, 400
        
        try:
            extent = Extent.parse(extent_string)
        except ValueError as e:
            # We don't provide feedback here on what exactly was wrong.
            return {'message':'Bad extent string'}, 400

        if extent.exceeds_area(MAX_BBOX_AREA_METRES_SQUARED):
            return {'message':'Extent was too large'}, 400

        result = self.os_postcode_repository.get_within_extent(extent)
        
        return result
        
    def __init__(self, **kwargs):
        super().__init__()
        self.os_postcode_repository : OSPostcodesRepository = kwargs[OS_POSTCODE_REPOSITORY_KEY]
