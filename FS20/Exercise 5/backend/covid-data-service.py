# -*- coding: utf-8 -*-
'''
Author: Janick Spirig, Github: janick187, E-Mail: janick.spirig@student.unisg.ch
Date: March 2020

This program's aim is to provide a simple interface to query the latest COVID data for any country.
The COVID data is extracted from Johns Hopkins University over an external API.
-> https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
-> https://documenter.getpostman.com/view/2568274/SzS8rjbe?version=latest
'''

from flask import Flask, request, Response, render_template
import requests
import json
from datetime import date

# create a Flask app
app = Flask(__name__)

# simple hello message on default path to check if app is running
@app.route('/', methods = ['GET'])
def sayHello():
    return "Hello I am up and running"

# funnction to get the latest COVID data for any country
@app.route('/getCountryStats', methods = ['GET'])
def getCountryStats():
    
    # the api's ressource from where the COVID data is obtained
    url = 'https://coronavirus-19-api.herokuapp.com/countries/{}'.format(request.args.get('country'))
    # url = "https://covidapi.info/api/v1/country/{}/latest".format(request.args.get('country'))
    
    # execute a HTTP GET request to get the data
    response = requests.get(url)
    
    # check if request was successful
    if response.status_code == 200:
        
        # convert received json data into a python dictionary
        data_dict = response.json()
        print(data_dict)
        
        # extract and store the data in local variables
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        infected = data_dict['cases']
        deaths = data_dict['deaths']
        recovered = data_dict['recovered']
        mortality = round((deaths * 100) / infected, 2)
   
        # create dictionary with all data which should be sent back to the front-end / sender of the request
        data_dict = {
            'updated': today,
            'infected' : infected,
            'deaths' : deaths,
            'recovered' : recovered,
            'mortality' : mortality
            }
        
        print(data_dict)
        
        # convert python dictionary to json
        json_data = json.dumps(data_dict)
        
        # create response
        resp = Response(json_data)
    
    # check if error occured while calling the COVID api
    else:
        # set response status to 404 as there was an error and request could not be processed as intended
        resp = Response(status=404)
        
    # add header to allow cross domain requests -> https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    # send response to front-end / sender of the request
    return resp