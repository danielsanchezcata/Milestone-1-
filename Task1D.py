from importlib_metadata import import_module
from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations=build_station_list
    rivers_with_station(stations)
    rivers_sorted=sorted(rivers_with_station(stations))
    print(len(rivers_sorted))
    print(rivers_sorted[0:10])
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations)
    print("River Aire:")
    print(sorted(rivers_dict['River Aire']))
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations)
    print("River Cam:")
    print(sorted(rivers_dict['River Cam']))
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations)
    print("River Thames:")
    print(sorted(rivers_dict['River Thames']))
    print("""
    *
    *
    *""")

if __name__ == "__main__":
    run()