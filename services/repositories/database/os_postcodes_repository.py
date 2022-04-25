'''
'''
from flask_sqlalchemy import SQLAlchemy

from models.extent import Extent


OS_POSTCODE_REPOSITORY_KEY = "os_postcode_repository"

class OSPostcodesRepository:
    '''
    The service that performs the SQL queries. This could be made into an ABC
    but I feel that would be "too C#" and we should instead rely on duck typing.
    During testing, we just mock this service out.
    '''
    def get_within_extent(self,extent:Extent):
        '''
        Selects all os postcodes within the specified extent.
        '''
        
        result = self._db.session.execute('''
        SELECT json_build_object(
            'type', 'FeatureCollection',
            'features', json_agg(ST_AsGeoJSON(t.*)::json)
            )
        FROM (select * from os_data.codepo_gb_code_point_open cgcpo 
        where geom && st_makeenvelope(:min_x,:min_y,:max_x,:max_y,3857)) t;
        ''',extent.get_sql_params())

        for row in result:
            value = row[0]
        # self._db.session.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
        return value

    def __init__(self,db:SQLAlchemy):
        self._db = db
        