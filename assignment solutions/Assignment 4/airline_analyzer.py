# -*- coding: utf-8 -*-
"""
a4_task2.airline_analyzer
15-538-085
Janick Spirig
"""

import networkx as nx
from a4_task2 import get_data, NoSuchFlight


def get_airlines_per_route(airlines_dict, source_airport_code, target_airport_code, max_hops):
    """
    Find airlines that have a path between the given airports.

    :param airlines_dict: a dictionary whose key is the airline code and the value is the airline object
    :param source_airport_code: the code of the source airport
    :param target_airport_code: the code of the target airport
    :param max_hops: the maximum number of hops allowed between the two airports.
    :return: a list of Airline objects serving the two airports within the maximum number of hops
    """
    ###   Task 2(c)   ###

    # Hint: use Airline's class method get_route() from 2(b)
    # ADD YOUR CODE HERE
    
    # empty result list to store all airline objects which cover the route
    serving_airlines = []
    
    # check for each airline if they cover the route
    for airline_code, airline_object in airlines_dict.items():
    
        try:
            # get route from source to target for current airline
            route = airline_object.get_route(source_airport_code, target_airport_code)
            
            # check if route fulfills maximum hops -> ['ZRH','FRA'] is a direct flight with zero hops -> len(list)-2
            if ((len(route)-2) <= max_hops):
                
                # add airline to result list
                serving_airlines.append(airline_object)
        
        # if the current airline does not cover the route from source to target
        except NoSuchFlight:
            # ignore airline
            pass
        
    return serving_airlines

    ### Task 2(c) END ###


def find_most_connected_airport(airlines_dict):
    """
    Find the airport with the highest number of connections available and return its code.

    :param airlines_dict: a dictionary whose key is the airline code and the value is the airline object
    :return: the airport code with the highest number of connections available.
    """

    ###   Task 2(d)   ###

    # ADD YOUR CODE HERE
    
    # create a new dict to store each airport code as key and the number of connections as value
    dct = {}
    
    # process all airlines and its flight-routes
    for airline_code, airline_object in airlines_dict.items():
        
        # get airline graph (flight-routes)
        g = airline_object.graph
        
        # process all airports that the airline is serving
        for airport in g.nodes:
            
            # count number of connections of airport
            number_connections = len(list(g.neighbors(airport)))
            
            # check if airport already occurred before
            if airport in dct:
                
                # increase existing connection number by the numer of connections of the current airline at this airport
                dct[airport] += number_connections
                
            else:
                # add airport to result dict
                dct[airport] = number_connections
    
    # get and return airport-code with most connections
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

    return max(dct, key=dct.get)

    ### Task 2(d) END ###


def main():
    airlines_dict, airports_dict = get_data()

    print("\n --------------- Airline Analyzer ---------------\n")
    print("# {} airlines are loaded with {} routes"
            .format(len(airlines_dict.keys()), sum([len(a.graph.edges) for a in airlines_dict.values()])))
    print("------")

    # Print a few airlines and their number of routes:
    print("# A few airlines and their number of routes:")
    some_airline_codes = ["AF", "LX", "FI"]
    for airline in airlines_dict.values():
        if airline.code in some_airline_codes:
            print(' - {} has {} routes'.format(airline.name, nx.number_of_edges(airline.graph)))

    print("------")


    # Airlines operating in "St Gallen Altenrhein Airport" (Airport code: "ACH")
    st_gallen_airport = "ACH"
    airlines_in_st_gallen = []
    for airline in airlines_dict.values():
        if airline.graph.has_node(st_gallen_airport):
            airlines_in_st_gallen.append(airline)
    print("# Airlines operating in {}:".format(st_gallen_airport))
    for airline in airlines_in_st_gallen:
        print(" - {}".format(airline))

    print("------")

    # Uncomment this comment block after Task 2(b) #
    # Check if Swiss International Air Lines (id: 4559) operates in two airports
    swissair_id = 4559
    zurich_airport = "ZRH"
    destination_airports = ["NRT", "NUE", "YVR", "BAH"]
    print("# Check routes for {} from {}:".format(airlines_dict[swissair_id].name, airports_dict[zurich_airport]))
    for dst in destination_airports:
        try:
            route = airlines_dict[swissair_id].get_route(zurich_airport, dst)
            print(" - has a route to {}: {}".format(airports_dict[dst], '->'.join(route)))
        except NoSuchFlight:
            print(" - no route to {}".format(airports_dict[dst]))

    print("------")
    # Comment block for Task 2(b) END #


     # Uncomment this comment block after Task 2(c) #
    airlines_with_max_1_hop_LIS_to_NUE = get_airlines_per_route(airlines_dict, "LIS", "NUE", 1)
    print("# Airlines with max 1 connection from LIS to NUE")
    for airline in airlines_with_max_1_hop_LIS_to_NUE:
        print(" - {}".format(airline))

    print("------")
    # Comment block for Task 2(c) END #


    # Uncomment this comment block after Task 2(d) #
    print("# Most Connected Airport:")
    most_connected = find_most_connected_airport(airlines_dict)
    if most_connected in airports_dict:
        print(" - {}".format(airports_dict[most_connected]))
    # Comment block for Task 2(d) END #


if __name__ == '__main__':
    main()
