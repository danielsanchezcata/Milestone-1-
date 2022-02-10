from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def test_distance():
    distance=stations_by_distance()
    assert distance >=0.0