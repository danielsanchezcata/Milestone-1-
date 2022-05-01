import matplotlib


import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .station import MonitoringStation
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    t = dates
    level = levels
    plt.plot(t, level)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)

    plt.tight_layout()
    if station.typical_range != None:
            plt.axhline(station.typical_range[0], color='g') 
            plt.axhline(station.typical_range[1], color='g')
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    #x = matplotlib.dates.date2num(dates) 
    #x = np.linspace(x)
    #y = levels

    poly, d0 = polyfit(dates,levels,p)
    
    #poly = np.poly1d(p_coeff)
    x = matplotlib.dates.date2num(dates) 

    plt.plot(dates, poly(x - x[0]))
    
    if station.typical_range != None:
            plt.axhline(station.typical_range[0], color='g') 
            plt.axhline(station.typical_range[1], color='g')
    plt.tight_layout()
    plt.show()
