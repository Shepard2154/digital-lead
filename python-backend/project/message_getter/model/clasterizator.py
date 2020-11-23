import pandas as pd
import numpy as np
import warnings
from sklearn.cluster import DBSCAN
from math import *
from datetime import datetime
from tslearn.clustering import TimeSeriesKMeans
from tslearn.preprocessing import TimeSeriesScalerMeanVariance, TimeSeriesResampler

def distance(lat1, lon1, lat2, lon2):
    #функция вычисления расттояние с учетом сферического типа поверхности
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return (distance)

def danger(coord_patrol):
    if coord_patrol['type']<3:
        return 0
    elif coord_patrol['type'] >= 3 and coord_patrol['type'] < 5:
        return 1
    elif coord_patrol['type'] >= 5:
        return 2


def classter_by_time(tim):
    # препроцессинг datetime
    time_preprocc = TimeSeriesResampler(sz=40).fit_transform(tim)
    km = TimeSeriesKMeans(n_clusters=len(labels), verbose=True, random_state=seed)
    labels = km.fit_predict(time_preprocc)
    return(labels)

def classter_by_distance(coords):
    db = DBSCAN(eps=0.0001,min_samples=3,algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    labels = db.labels_
    return(labels)

def patrol_label(label,primer,pogr):   
    dist_all = []
    # вычисление расстояние между точками 
    if primer['labels'].value_counts(normalize=True)[label]>pogr:
        for i in range(len(primer[['latitude','longitude']][primer['labels']==label])):
            sum_dist = 0
            for j in range(len(primer[['latitude','longitude']][primer['labels']==label])):
                dist = distance(
                    primer[['latitude','longitude']][primer['labels']==label].iloc[i][0],
                    primer[['latitude','longitude']][primer['labels']==label].iloc[i][1],
                    primer[['latitude','longitude']][primer['labels']==label].iloc[j][0],
                    primer[['latitude','longitude']][primer['labels']==label].iloc[j][1]
                                )
                sum_dist += dist   
            dist_all.append(sum_dist)
        dist_all = np.array(dist_all)
        # определние равноудаленной точки кластера
        types = []
        timing = []
        for i in primer['type']:
            types.append(i)
        for i in primer['time']:
            timing.append(i)
        print(primer[['latitude','longitude']][primer['labels']==label].iloc[dist_all.argmin()])
        return (primer[primer['labels']==label].iloc[dist_all.argmin()],types,timing)
     else:
        return [0,0]

def main_patrol_func(df):    
    coord_patrol = pd.DataFrame()
    index_street = 0
    schet = 0
    dtp_count = 0
    
    # данные передаваемые в кластер
    latitude = []
    longitude = []
    types = []
    EAC_adr = []
    EAC_build = []
    timing = []
        
    # выявление кластеров в районах    
    for district in df['District'].unique():
        if objct.empty:
            continue
        coords = objct[["latitude", "longitude"]].values
        
        # кластеризатор по расстоянию на основе алгоритма ball_tree
        labels = classter_by_distance(coords)
        
        # кластеризация по времени
        labels_2 = km.fit_predict(objct['time'])
        
        # распределение координат по класстерам
        df_coords = pd.DataFrame()
        df_coords['latitude'] = coords[:,0]
        df_coords['longitude'] = coords[:,1]
        df_coords['labels'] = db.labels_
        df_coords['type'] = [x for x in objct['type']]
        df_coords['time'] = [x for x in objct['time']]
        
        for i in np.unique(db.labels_):
            # вычисление равноудаленной точки кластера
            a = patrol_label(i,df_coords[df_coords['labels']==i],pogr)
            if a[0][0] != 0:
                latitude.append(a[0][0])
                longitude.append(a[0][1])
                types.append(len(a[1]))
                timing.append(str(a[2]))
        index_street += 1
    coord_patrol['latitude'] = np.array(latitude)
    coord_patrol['longitude'] = longitude
    coord_patrol['type'] = types
    coord_patrol['time'] = timing
    coord_patrol['danger'] = danger(coord_patrol)
    return(coord_patrol)

