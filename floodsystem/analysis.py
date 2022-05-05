from datetime import datetime, timedelta
from .station import MonitoringStation 
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates) 
    #x = np.linspace(x)
    #y = levels

    p_coeff = np.polyfit(x-x[0],levels,p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])

