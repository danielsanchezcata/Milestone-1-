from floodsystem.flood import high_risk, stations_high_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
#from datetime import datetime, timedelta
 
def run():
    stations= build_station_list()
    tol = 0.8
    stat_list= []
    x=10
   # dt=3
    #for station in stations:
   #dates, levels =fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    #stat = stations_level_over_threshold(stations, tol)
    print(high_risk(stations, x, dt=1))

    
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()