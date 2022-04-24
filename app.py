"""
An example app that reads some vector GIS data from a POSTGIS database
and returns it from an example API endpoint.
"""

from flask import Flask
from flask import request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from configuration.debug_configuation import DebugConfiguration

from resources.hello_resource import HelloWorld
from resources.os_postcodes_resource import OSPostcodes
from services.repositories.database.os_postcodes_repository import OS_POSTCODE_REPOSITORY_KEY, OSPostcodesRepository

APP = Flask(__name__)
# In reality we'd test for presence of env var for flask app environment.
APP.config.from_object(DebugConfiguration())
API = Api(APP)
DATABASE = SQLAlchemy(APP)

@APP.route("/healthcheck")
def health_check():
    '''
    Used by load balancer or other monitoring to check
    that app can connect to database.
    '''
    try:
        r = DATABASE.session.execute("SELECT 1+1 AS result;")
        for row in r:
            print(row[0])
    except psycopg2.OperationalError as exception:
        print("Could not connect to database")
        print(exception)
        return "Unhealthy"
    except Exception as exception:
        print(exception)
        return "Unhealthy"
    return "Healthy"


@APP.route("/")
def hello_world():
    '''
    An example route
    '''
    return "<p>Hello, World!</p>"


os_postcode_repository = OSPostcodesRepository(DATABASE)
API.add_resource(OSPostcodes, '/api/ospostcodes',resource_class_kwargs={ OS_POSTCODE_REPOSITORY_KEY:os_postcode_repository })

if __name__ == '__main__':
    APP.run()
