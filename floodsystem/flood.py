from . import datafetcher
from .station import MonitoringStation
from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
#from importlib_metadata import import_module
from .haversine import haversine, Unit

def stations_level_over_threshold(stations, tol):
    for station in stations:
        if station.relative_water_level > tol:
            print((station, station.relatiev_water_level))
        else:
            pass

    
