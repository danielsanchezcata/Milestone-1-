from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    station = stations_level_over_threshold(stations, tol)
    s_list = []
    for s in range(len(station)):
        s_list.append(str(station[s][0].name), str(station[s][1]))
    assert len(s_list) >= 1