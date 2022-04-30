from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    station = stations_level_over_threshold(stations, tol)
    for s in range(len(station)):
        print(str(station[s][0].name), str(station[s][1]))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

