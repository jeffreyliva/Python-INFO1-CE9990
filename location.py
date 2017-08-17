"""

location.py

"""

import sys
import urllib.request
import json


class Location(object):


    def __init__(self, latitude, longitude):
        if not (isinstance(latitude, int) or isinstance(latitude, float)):
            raise TypeError("Latitude must be int or float, not", str(type(latitude)))
        if not (isinstance(longitude, int) or isinstance(longitude, float)):
            raise TypeError("Longitude must be int or float, not", str(type(latitude)))
        if abs(latitude) > 90:
            raise ValueError("Latitude must be in the range from -90 to 90 inclusive, not", str(latitude))
        if abs(longitude) > 180:
            raise ValueError("Longitude must be in the range from -180 to 180 inclusive, not", str(longitude))


        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        vertical = "N" if self.latitude >= 0 else "S"
        horizontal = "E" if self.longitude >= 0 else "W"
        return "{}°{} {}°{}".format(abs(self.latitude), vertical, abs(self.longitude), horizontal)

    def getLatitude(self):
        return self.latitude

    def setLatitude(self, latitude):
        "Set the latitude."
        self.latitude = latitude

    def getLongitude(self):
        return self.longitude

    def setLongitude(self, longitude):
        "Set the longitude"
        self.longitude = longitude

    def getZipcode(self):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(self.latitude, self.longitude)

        try:
            source = urllib.request.urlopen(url)
        except urllib.error.URLError as error:
            print("urllib.error.URLError", error)
            sys.exit(1)

        file = source.read()
        source.close()

        try:
            utfFile = file.decode("utf-8")
        except UnicodeError as unicodeError:
            print(unicodeError)
            sys.exit(1)

        try:
            dictionary = json.loads(utfFile)
        except json.JSONDecodeError as jsonDecodeError:
            print(jsonDecodeError)
            sys.exit(1)

        results = dictionary["results"]
        if len(results) > 0:
            address_components = results[0]["address_components"]
            for component in address_components:
                if "postal_code" in component["types"]:
                    # return int(component["long_name"])
                    try:
                        s = component["long_name"]
                    except KeyError:
                        return 0
                    try:
                        return int(s)
                    except ValueError:
                        return 0
        return 0


if __name__ == '__main__':
    l = Location(40.750700, -73.993439)
    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longitude of {} is {}.".format(l, l.getLongitude()))
    print("The zipcode of {} is {}.".format(l, l.getZipcode()))

    print("\nChanging latitude and longitude...\n")
    l.setLatitude(40.740566)
    l.setLongitude(-73.984852)

    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longitude of {} is {}.".format(l, l.getLongitude()))
    print("The zipcode of {} is {}.".format(l, l.getZipcode()))
    
    sys.exit(0)
