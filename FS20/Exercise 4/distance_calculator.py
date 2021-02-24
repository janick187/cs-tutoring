# -*- coding: utf-8 -*-
'''
Author: Janick Spirig, Github: janick187, E-Mail: janick.spirig@student.unisg.ch
Date: March 2020

This program's aim is to calculate the distance in km between two addresses using the Google Distance Matrix API.
It serves an example how to interact with a public API, which is relevant for Assignment 5 Task 4 & 5 of the Module Fundamentals of Computer Science.
The user enters the two addresses he/she wants to calculate the distance.
Then the program calls the Google Distance Matrix API and prints the distance between the two addresses to the console.
Just execute the program and see what is happening.
'''

import requests

class Route:
    def __init__(self, origin, destination, distance):
        # :string the origin address
        self.origin = origin
        # :string the detination address:
        self.destination = destination
        # :String the distance between origin and destination
        self.distance = distance
        
    def __str__(self):
        return '\n\nThe distance between {} and {} is {}'.format(self.origin, self.destination, self.distance)

def build_url(parameters):
    # :parameters a dictionary containing all parameters that are relevant for the request with the key as the parameter-key and the value as the parameter-value 
    # return the ready-to-be-used request URL
    
    # Distance Matrix API base URL
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    
    # Google API key
    api_key = ''
    
    # extend the base URL with all parameter-key's and their values
    for key, value in parameters.items():
        url += '{}={}&'.format(key, value)
        
    # extend the URL with the API key at the end
    url += 'key={}'.format(api_key)

    return url


def get_route(origin, destination):
    # :origin a list containing the street, numeber and place of the origin address
    # :destination a list containing the street, numeber and place of the destination address
    # return a route object containing the origin, destination and distance
    
    # create empty dictionary to store all parameters as key-value pairs
    parameters = {}
    
    # store parameters in dict -> see also: https://developers.google.com/maps/documentation/distance-matrix/intro?hl=de
    parameters['origins'] = '{}+{}+{}'.format(origin[0], origin[1], origin[2])
    parameters['destinations'] = '{}+{}+{}'.format(destination[0], destination[1], destination[2])
    
    # get read-to-use url
    url = build_url(parameters)
    
    # execute request and store JSON response as dictionary
    json_response = requests.get(url).json()
    
    # extract relevant data from dictionary
    destination = json_response['destination_addresses'][0]
    origin = json_response['origin_addresses'][0]
    distance = json_response['rows'][0]['elements'][0]['distance']['text']
    
    # create new route object
    route = Route(origin, destination, distance)
    
    return route
    

def main():
    
    # get user input and split user entries so that the addresses are stored in lists
    origin = input('Which is your starting point (Format: Street, Number, Place)?').split(',')
    destination = input('Which is your destination point (Format: Street, Number, Place)?').split(',')
    
    # calculate distance
    route = get_route(origin, destination)
    
    # print result -> hint: __str__() is executed
    print(route)

if __name__ == '__main__':
    main()    