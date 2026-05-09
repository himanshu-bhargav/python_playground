''' This file is for learning purposes only. It is not intended to be used in production. '''
from sklearn.cluster import KMeans
# KMeans
#age, amount
inputdata=[[20,500],[40,1000],[30,800],[18,300,],[28,1200],[35,1400],[45,1800]]
initial_centroids =[[20,500],[40,1000]]
model=KMeans(n_clusters=2, init=initial_centroids, n_init=1) # The KMeans class from the sklearn.cluster module is used to perform K-means clustering. The n_clusters parameter specifies the number of clusters to form, which is set to 2 in this case. The init parameter specifies the method for initializing the cluster centers, which is set to initial_centroids in this case. The n_init parameter specifies the number of times the K-means algorithm will be run with different centroid seeds, which is set to 1 in this case. This means that the K-means algorithm will be run only once with the specified initial cluster centers.
model.fit(inputdata)
print(model.labels_) # The labels_ attribute of the KMeans model contains the cluster labels for each data point in the input data. In this case, it will print an array of cluster labels for each data point in the inputdata list. For example, it might print [0 1 0 0 1 1 1], which indicates that the first, third, and fourth data points belong to cluster 0, while the second, fifth, sixth, and seventh data points belong to cluster 1.
print(model.cluster_centers_) # The cluster_centers_ attribute of the KMeans model contains the coordinates of the cluster centers. In this case, it will print an array of cluster centers for each cluster in the KMeans model. For example, it might print [[25.0, 533.33333333], [37.5, 1350.0]], which indicates that the center of cluster 0 is at coordinates (25.0, 533.33333333) and the center of cluster 1 is at coordinates (37.5, 1350.0).