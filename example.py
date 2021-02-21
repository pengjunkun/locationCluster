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
        lat.append(latitude)
        lon.append(longitude)

plt.figure(figsize=(50,50))
plt.scatter(lon,lat)
xTicks=range(1152,1174)
xTicks=[i/10 for i in xTicks]
yTicks=range(392,411)
yTicks=[i/10 for i in yTicks]
plt.xticks(xTicks,xTicks)
plt.yticks(yTicks,yTicks)
plt.xlabel("longitude")
plt.ylabel("latitude")


kmeans=KMeans(n_clusters=5)
kmeans.fit(locations)
result=kmeans.cluster_centers_
plt.scatter(result[:,1],result[:,0],s=5000,c='r',marker='D')


plt.show()

# K = range(5, 20)
# meanDispersions = []
# centers={}
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(locations)
#     meanDispersions.append(
#         sum(np.min(cdist(locations, kmeans.cluster_centers_, 'euclidean'), axis=1)) / len(locations))
#     centers.update({k:kmeans.cluster_centers_})
# plt.plot(K, meanDispersions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Average Dispersion')
# plt.title('Selecting k with the Elbow Method')
# plt.show()
#
# print(centers)
