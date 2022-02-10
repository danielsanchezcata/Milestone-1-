from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():
    stations = stations_within_radius()
    assert len(stations) > 0

def test_rivers_by_station():
    stations = build_station_list()
    rivers = rivers_by_station()
    for river in rivers:
        if river in stations.river:
            assert river

    for river in rivers:
        assert river[1] >= 0 



