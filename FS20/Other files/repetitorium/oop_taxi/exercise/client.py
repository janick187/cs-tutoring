from resources import *

def addTrip(company, car, driver, customer, tip, rating):
    
    tripCreated = False
    
    try:
        trip = Trip(car, driver, customer)
        tripCreated = True
    except UnexpericencedException:
        print("\nDriver {}, {} is too bad due to lack of experience!\n".format(driver.fname, driver.lname))

        for d in company.drivers:
            print("Check if driver {} is good enough\n".format(d.fname))
            try:
                trip = Trip(car, d, customer)
                tripCreated = True
                break
            except UnexpericencedException:
                print("{} is also not good enough".format(d.fname))
                continue
        
    if tripCreated:
        trip.addRating(rating)
        trip.addTip(tip)
        company.addNewTrip(trip)
    else: 
        print("None of the drivers is good enough to perform this trip!")
    

def main():

    taxi_abc = Company("Taxi ABC")

    driver_jack = Driver("Jack", "Miller", 309459, "12.01.2022", 4)
    driver_julian = Driver("Julian", "Baum", 309491, "12.03.2022", 5)
    driver_melanie = Driver("Melanie", "Citron", 569459, "01.06.2021", 3)

    taxi_abc.addDrivers([driver_jack, driver_jack, driver_melanie])

    benz = Car("Mercedes", 200, 10)
    vw = Car("VW", 150, 8)

    taxi_abc.cars.append(benz)
    taxi_abc.cars.append(vw)

    addTrip(taxi_abc, benz, driver_jack, Customer("Hanna", "Blume"), 3, 5)
    addTrip(taxi_abc, vw, driver_julian, Customer("Hector", "Muller"), 2, 4)
    addTrip(taxi_abc, benz, driver_melanie, Customer("Franz", "Hug"), 1, 4)
    
    print(taxi_abc)

if __name__ == "__main__":
    main()