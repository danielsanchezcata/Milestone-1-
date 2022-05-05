from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.geo import build_station_list
from floodsystem.flood import stations_high_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    s=stations_high_rel_level(stations,5)
    #gets top 5 relative levelled stations
    dt = 2
    p=4
    for station in s:
        #iterates over each station and plots a graph using dates+levels for each one
        dates, levels =fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, p)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()