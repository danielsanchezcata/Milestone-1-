from floodsystem.station import inconsistent_typical_range_stations
def test_F():
    list_inconsistent_stations = inconsistent_typical_range_stations()
    assert len(list_inconsistent_stations) > 0