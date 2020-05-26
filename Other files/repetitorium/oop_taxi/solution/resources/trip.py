from random import randrange
from . import *
from .driver import UnexpericencedException

class Trip:

    def __init__(self, car, driver, customer):
        self.checkExperience(driver)
        self.id = randrange(1, 100000)
        self.car = car
        self.driver = driver
        self.customer = customer
        self.tip = 0
        self.rating = 0

    def addTip(self, amount):
        self.tip = amount
        self.driver.tips += amount
    
    def addRating(self, rating):
        self.rating = rating
    
    def checkExperience(self, driver):
        try:
            driver.checkRating()
        except UnexpericencedException as e:
            e.message = 'Driver {} is not experiences enough for carrying out this trip!'.format(driver.lname)
            raise e