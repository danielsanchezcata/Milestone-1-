from floodsystem.geo import rivers_by_station
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list
    N=9
    print(rivers_by_station(stations, N))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run