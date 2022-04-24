'''
'''
from flask_sqlalchemy import SQLAlchemy


OS_POSTCODE_REPOSITORY_KEY = "os_postcode_repository"

class OSPostcodesRepository:
    def get_within_extent(self):
        result = self._db.session.execute('''
        SELECT json_build_object(
            'type', 'FeatureCollection',
            'features', json_agg(ST_AsGeoJSON(t.*)::json)
            )
        FROM (select * from os_data.codepo_gb_code_point_open cgcpo 
        where geom && st_makeenvelope(-841259.181548079,6405988.47734992,187932.628033128,8263143.60249568,3857) 
        limit 10) t;
        ''')

        for row in result:
            value = row[0]
        # self._db.session.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
        return value

    def __init__(self,db:SQLAlchemy):
        self._db = db
        