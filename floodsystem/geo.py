# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_within_radius(stations, centre, r):
    list_within_r = []
    #stations = MonitoringStation(coord=(float(e['lat']), float(e['long'])))
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            list_within_r.append(station)
    return(list_within_r)


    return list_within_r.sort()

def rivers_by_station(stations, N):
    from.geo import stations_by_river
    stat_river = stations_by_river(stations)
    river_and_number = []
    for river in stat_river:
        number = len(stat_river[river])
        river_and_number.append((river,number))
    ordered = sorted_by_key(river_and_number,1,reverse=True)
    return ordered[:N]

    