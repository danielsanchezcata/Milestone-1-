# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
#from importlib_metadata import import_module
from .haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    list_within_r = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            list_within_r.append(station)
    return(list_within_r)


def rivers_by_station(stations, N):
    river_list = []
    number_list = []
    for riv in stations:
        river_list.append(riv.river)
    for num in river_list:
        c = river_list.count(num)
        number_list.append((num, c))
    number_list = list(dict.fromkeys(number_list))
    number_list.sort(key=lambda x:x[1], reverse=True)
    while number_list[N-1][1] == number_list[N][1]:
        N+=1
    ordered = number_list[0:N]
    return ordered


def stations_by_distance (stations, p):
    stations_distances=[]
    for station in stations:
        distance=float(haversine(p,station.coord))
        stations_distances.append((station.name, distance))
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




     

