from .station import MonitoringStation, NoneType
from .utils import sorted_by_key
from .stationdata import update_water_levels
#from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
import datetime
import numpy as np

def stations_level_over_threshold(stations, tol):
    station_list = []
    for station in stations:
        if (type(station.latest_level) == float) and (station.typical_range_consistent() == True):
            if (station.relative_water_level() > tol):
                station_list.append((station, station.relative_water_level()))
    return (sorted_by_key(station_list, 1, reverse=True))


def stations_high_rel_level(stations,N):
    NoneType= type(None)
    """calculates relative water level compared to its typical range, returns 'N' highest"""
    relative_levels=[]
    update_water_levels(stations)
    for station in stations:
        if station.typical_range != None and station.typical_range_consistent and station.latest_level != None :
            #only counts stations with consistent data
            relative_level=station.latest_level-station.typical_range[1]
            #finds difference between current station level and typical upper range
            relative_levels.append((station, relative_level))
            #adds station and its relative level as a tuple to a list
            sorted_relative_levels= sorted_by_key(relative_levels, int(1),reverse=True)
            #sorts list based on relative level, in reverse (to make list descending)
            station_only=[]
            #creates empty list for just stations
            for tuple in sorted_relative_levels[0:N]:
            #iterates over first 'N' tuples in list of (station,relative level)
                station_only.append(tuple[0])
    #adds station terms of sorted list to a new list
    return station_only


#def high_risk(stations,x=5,y=3,dt=3):
    """calculates relative risk level compared to its typical range, and 'predicted' level based on rise over past 'dt' days. Predicts 'y' days into future, returns 'N' highest"""
   # predicted_levels=[]
    #update_water_levels(stations)
    #for station in stations:
        #if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None:
            #relative_level=station.latest_level-station.typical_range[1]
            #dates,levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #finds dates,levels for river over past dt days
            #try:
                #predicted_rise= ((levels[0]-levels[-1])/dt)*y
            #takes difference between first and last values from levels list,to get change in level over 'dt' days. Then divides by dt for rise per day
            #Then multiplies this diff by the number of days over which the risk levels are to be predicted, to get the predicted rise   
            #except IndexError:
            #avoids an error when fetch measure levels is an empty list, due to an 'except IndexError' added in the fetch function
                #continue
            #except TypeError:
            #avoids an error when fetch measure levels[0] or levels[-1] is a list, due to an Error in the fetch function
                #continue                
            #predicted_rel_level=(relative_level + predicted_rise)
            #predicted relative level is current level added to expected rise, rounded to 4dp
            #if predicted_rel_level>5:
             #   risk_rating="Severe"
            #elif predicted_rel_level<5 and predicted_rel_level>=1:
             #   risk_rating="High"
            #elif predicted_rel_level<1 and predicted_rel_level>=0:
             #   risk_rating="Moderate"
            #elif predicted_rel_level<0:
             #   risk_rating="Low"
            #risk rating based on predicted level
            #predicted_levels.append((station.town, "Predicted relative level={}".format(predicted_rel_level) ,"Risk={}".format(risk_rating) ))
            #adds station, its predicted level and its risk rating a tuple to a list
    #sorted_predicted_levels= sorted_by_key(predicted_levels,int(1),reverse=True)
    #most_risk_list=[]
    #for item in sorted_predicted_levels[0:x]:
        #iterates over first 'N' tuples in list of (station,predicted level, risk rating)
     #   most_risk_list.append(item)
    #print("This prediction is based on data over the past {} days, predicting {}days into the future".format(dt,y))
    #return most_risk_list

def high_risk(stations, x, dt=1):
    update_water_levels(stations)
    high_risk_list = []
    #dt = matplotlib.dates.date2num(dates) 
    for station in stations:
        relative_level_list = []
        if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None:
            #rel_levels_list = []
            dates,levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            levels = np.array(levels)
            for l in levels:
                relative_level = l*(1/station.typical_range[1])
                relative_level_list.append(relative_level)
            if len(levels) > 0:
                try:
                    rel_average = sum(relative_level_list)/len(relative_level_list)
                except IndexError:
            #avoids an error when fetch measure levels is an empty list, due to an 'except IndexError' added in the fetch function
                    continue
                except TypeError:
            #avoids an error when fetch measure levels[0] or levels[-1] is a list, due to an Error in the fetch function
                    continue
                if rel_average >= 1.5:
                    risk = "Severe"
                elif rel_average < 1.5 and rel_average >= 1:
                    risk = "High"
                elif rel_average < 1 and rel_average >= 0.75:
                    risk = "Moderate" 
                elif rel_average < 0.75:
                    risk = "Low"
                #print((station.name, rel_average, risk))
        #increase = all(i < j for i, j in zip(levels, levels[1:]))
            if risk == "Severe":
        #if rel_levels_list[i-1]>rel_levels_list[i-2] and rel_levels_list[i-2]>rel_levels_list[0] and risk == "Severe":
                high_risk_list.append((station.town, risk))

            sorted_risk_list= sorted_by_key(high_risk_list, int(1),reverse=True)

            #rel_levels_list.reverse()
    
    return (sorted_risk_list[0:x])
                