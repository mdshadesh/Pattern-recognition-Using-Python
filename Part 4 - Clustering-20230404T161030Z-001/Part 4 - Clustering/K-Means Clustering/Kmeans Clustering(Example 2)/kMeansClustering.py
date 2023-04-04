import numpy as np
import os
import pandas as pd


def compute_euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))

def compute_manhattan_distance(point, centroid):
    return np.sum(abs(point - centroid))

def assign_label_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    #print(distance)
    #print("index", index_of_minimum)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]

def compute_new_centroids(cluster_label, centroids):
    #print("Centroid start")
    #print(cluster_label)
    #print(centroids)
    #print("Centroid end")
    return np.array(cluster_label + centroids)/2

def iterate_k_means(data_points, centroids, total_iteration):
    label = []
    cluster_label = []
    total_points = len(data_points)
    k = len(centroids)
    
    for iteration in range(0, total_iteration):# 0 to 99
        for index_point in range(0, total_points): # 0 to 14
            distance = {}
            for index_centroid in range(0, k): # 0 to 2
                distance[index_centroid] = compute_euclidean_distance(data_points[index_point], centroids[index_centroid])
            label = assign_label_cluster(distance, data_points[index_point], centroids)
            #print("start")
            #print(label)
            #print("end")
            centroids[label[0]] = compute_new_centroids(label[1], centroids[label[0]])

            if iteration == (total_iteration - 1):
                cluster_label.append(label)
        

    return [cluster_label, centroids]

def print_label_data(result):
    print("Result of k-Means Clustering: \n")
    #cluster_one = []
    #cluster_two = []
    #cluster_three = []
    for data in result[0]:
#        if data[0] == 0:
#            cluster_one.append(data[1])
#        elif data[0] == 1:
#            cluster_two.append(data[1])
#        else:
#            cluster_three.append(data[1])
#    print("Cluster One")
#    print(cluster_one)
        print("data point: {}".format(data[1]))
        print("cluster number: {} \n".format(data[0]))
    print("Last centroids position: \n {}".format(result[1]))

def create_centroids():
    centroids = []
    #centroids.append([5.0, 0.0])
    #centroids.append([45.0, 70.0])
    #centroids.append([50.0, 90.0])
    centroids.append([2, 10])
    centroids.append([5, 8])
    centroids.append([1, 2])
    return np.array(centroids)

if __name__ == "__main__":
    #filename = "G:\Dropbox\SU\CSE-425(PR)\Lab\In Python\Machine Learning Algorithms\Part 4 - Clustering\K-Means Clustering\Kmeans Clustering(Example 2)\data.csv"
    filename = os.path.dirname(__file__) + "\data.csv"
    #print(filename)
    data_points = np.genfromtxt(filename, delimiter=",")
    #print(data_points)
    # Importing the dataset
    #data_points = pd.read_csv('data.csv')
    centroids = create_centroids()
    total_iteration = 1
    
    [cluster_label, new_centroids] = iterate_k_means(data_points, centroids, total_iteration)
    print_label_data([cluster_label, new_centroids])
    print()