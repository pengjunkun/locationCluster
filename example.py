import csv
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

location_file = "C:\\Users\\HP\\work\\project\\SugarJar\\simu\\data\\24h.csv"
locations = []
lat=[]
lon=[]

with open(location_file, 'r') as f:
    dictReader = csv.DictReader(f)
    for row in dictReader:
        locations.append([row['latitude'], row['longitude']])
        latitude=float(row['latitude'])
        longitude=float(row['longitude'])
        if latitude>100:
            print(row)
            continue
        # lat.append(latitude)
        # lon.append(longitude)

# plt.scatter(lon,lat)
# plt.show()

# c1x = np.random.uniform(0.5, 1.5, (1, 10))
# c1y = np.random.uniform(0.5, 1.5, (1, 10))
# c2x = np.random.uniform(3.5, 4.5, (1, 10))
# c2y = np.random.uniform(3.5, 4.5, (1, 10))
# x = np.hstack((c1x, c2x))
# y = np.hstack((c1y, c2y))
# X = np.vstack((x, y)).T
K = range(5, 20)
meanDispersions = []
centers={}
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(locations)
    meanDispersions.append(
        sum(np.min(cdist(locations, kmeans.cluster_centers_, 'euclidean'), axis=1)) / len(locations))
    centers.update({k:kmeans.cluster_centers_})
plt.plot(K, meanDispersions, 'bx-')
plt.xlabel('k')
plt.ylabel('Average Dispersion')
plt.title('Selecting k with the Elbow Method')
plt.show()

print(centers)
