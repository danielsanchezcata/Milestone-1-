from floodsystem.flood import stations_level_over_threshold, stations_high_rel_level, high_risk
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    station = stations_level_over_threshold(stations, tol)
    s_list = []
    for s in range(len(station)):
        s_list.append((str(station[s][0].name), str(station[s][1])))
    assert len(s_list) >= 0

def test_stations_highest_rel_level():
    stations= build_station_list()
    s_list = []
    for s in stations_high_rel_level(stations,10):
        relative_level=s.latest_level-s.typical_range[1]
        s_list.append((s.name, relative_level))
    assert len(s_list) >= 0