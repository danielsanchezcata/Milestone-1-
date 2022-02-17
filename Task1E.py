from floodsystem.geo import rivers_by_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    N = 10
    print(rivers_by_station(stations, N))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run ()