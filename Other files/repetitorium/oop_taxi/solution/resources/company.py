from .trip import Trip
from .driver import Driver
from .car import Car


class Company:

    def __init__(self, name):
        self.name = name
        self.drivers = []
        self.trips = []
        self.cars = []
        
    def __str__(self):

        result = "Company {} has done the following trips:\n".format(self.name)

        for t in self.trips:
            result = result + "\nCustomer: {}, {}\nCar: {}, {} PS\nDriver: {}, {}\nRating: {}\n".format(t.customer.fname, t.customer.lname, t.car.brand, t.car.ps, t.driver.fname, t.driver.lname, t.rating)

        return result

    def addNewTrip(self, trip):
        self.trips.append(trip)
        
        for d in self.drivers:
            if trip.driver.fname == d.fname:
                d.addTrip(trip)


    def addDrivers(self, drivers):
        for d in drivers:
            self.drivers.append(d)

