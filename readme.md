# Flask Example

An example Flask app that reads some GIS data from POSTGIS and returns it as a GeoJSON.


## Example route

To test out some example routes, try the following:
Should return some geojson data
http://127.0.0.1:5000/api/ospostcodes?extent=-358183.914544,7544263.629197,-355305.209470,7548213.870932

Should return "Extent was too large" because it is a large requested area.
http://127.0.0.1:5000/api/ospostcodes?extent=-355305.209470,0,0,7548213.870932

If you flip the coordinates, it will also return an error
http://127.0.0.1:5000/api/ospostcodes?extent=10,10,0,0

# Running



## Configuration

While developing, on Mac or Linux, use [autoenv](https://github.com/hyperupcall/autoenv).

# Testing

There is a single test suite under models/extent_tests.py

# Notes

1. This is my first ever flask app, so please be kind. If you want to see an example app in a framework where I know what I am doing, please see [Amici](https://github.com/oshawa-connection/amici)
2. This whole app works only for EPSG:3857. It does not work at the x wraparound, which is ok for now because all data is in the UK.
3. I attempted to follow pep8 but pylint on my (8 year old) computer is a little messed up.
4. There should be a logger service, but I didn't have time.
5. I am going through a phase where I have fallen out with ORMs and prefer to do things in raw queries - talk to me about it!

