from floodsystem.geo import stations_by_river, stations_within_radius
from floodsystem.geo import rivers_by_station
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 0
    station = stations_within_radius(stations, centre, r)
    assert len(station) == 0

def test_rivers_by_station():
    stations = build_station_list()
    N = 9
    rivers  = rivers_by_station(stations, N)
    for river in rivers:
        assert river[1] >= 0

def test_stations_by_river():
    stations = build_station_list()
    station = stations_by_river(stations)
    assert len(stations) >= 0 
