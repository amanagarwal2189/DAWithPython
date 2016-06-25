import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])


rider_day1 = ridership[0,:]
#find index of max value in a np array
ind2 = ridership[0,:].argmax()
#find index of any element in a np array
ind = rider_day1.tolist().index(rider_day1.max())
#mean for column here station
avg_max_Station_ridership = np.mean(ridership[:,ind])
#mean for column here day
avg_max_day_ridership = np.mean(ridership[ind, :])
#over all mean
mean_data = np.mean(ridership)
#calc mean per station; axis donates direction; 0-column;1-row
mean_per_station = ridership.mean(axis=0)
max_mean_station = mean_per_station.max() 
min_mean_station = mean_per_station.min()
print(max_mean_station, min_mean_station)