# Flask Example

An example Flask app that reads some GIS data from POSTGIS and returns it as a GeoJSON.

# Running

Docker

## Configuration

While developing, on Mac or Linux, use [autoenv](https://github.com/hyperupcall/autoenv).

# Testing

There is a single test

# Notes

This whole app works only for EPSG:3857. It does not work at the x wraparound, which is ok for now because all data is in the UK.