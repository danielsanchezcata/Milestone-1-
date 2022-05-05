from floodsystem.flood import high_risk, stations_high_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
import datetime
#from datetime import datetime, timedelta
 
def run():
    stations= build_station_list()
    tol = 0.8
    #stat=stations_high_rel_level(stations, 30)
   # dt=3
    #for station in stations:
   #dates, levels =fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    print(high_risk(stations, tol, dt = 3))

    
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()