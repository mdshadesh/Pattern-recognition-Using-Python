import numpy as np
import pandas as pd

def create_centroids(dataset, k):
    #number_of_rows = initial_data.shape[0]
    number_of_rows = len(dataset)
    random_indices = np.random.choice(number_of_rows, size=k, replace=False)
    centroids = dataset[random_indices, :]
    return np.array(centroids)

data_set = pd.read_csv("data.csv")
data_set = data_set.iloc[:,:].values
k = int(input("Enter cluster number = "))
centroids = create_centroids(data_set, k)
print(centroids)