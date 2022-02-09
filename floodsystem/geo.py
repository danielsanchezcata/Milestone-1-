# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from importlib_metadata import import_module
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list

def stations_by_distance (stations, p):
    stations_distances=[]
    for station in stations:
        distance=float(haversine(p,station.coord))
        stations_distances.append(station.name, distance)
        sorted_stations_distances=sorted_by_key(stations_distances,int(1))
        return sorted_stations_distances

def rivers_with_station(stations):
    list_rivers=[]
    for station in stations:
        list_rivers.append(station.river)
    set_rivers=set(list_rivers)
    return set_rivers

def stations_by_river(stations):
    dictionary_rivers={}
    for station in stations:
        if station.river in dictionary_rivers.keys():
            dictionary_rivers[station.river].append(station.name)
        else:
            dictionary_rivers[station.river]=[station.name]
    return dictionary_rivers 




     

