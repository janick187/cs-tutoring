from .driverlicense import DriverLicense
from . import *

class Driver:
    
    def __init__(self, fname, lname, license_no, license_expiry, rating):
        self.fname = fname
        self.lname = lname
        self.license = DriverLicense(license_no, license_expiry)
        self.trips = []
        self.tips = 0
        self.rating = rating

    def addTrip(self, trip):
        self.trips.append(trip)

    def checkRating(self):
        if self.rating < 4:
            raise UnexpericencedException()

class UnexpericencedException(Exception):
    pass