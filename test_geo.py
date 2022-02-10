from floodsystem.geo import stations_by_river, stations_within_radius
from floodsystem.geo import rivers_by_station
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():
    stations = stations_within_radius()
    for station in stations:
        if station.name == 'Bin Brook':
            station_cam = station
            break
    assert station_cam

def test_rivers_by_station():
    rivers  = rivers_by_station()
    for river in rivers:
        assert river[1] >= 0 

def test_stations_by_river():
    stations = stations_by_river()
    for station in stations:
        if station.name == 'Airmyn':
            station_cam = station
        break
    assert station_cam
