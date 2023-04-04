# Example of making predictions
from math import sqrt
#import math

# calculate the Euclidean distance between two vectors
def euclidean_distance(x, y):
	distance = 0.0
	length = len(y)
	for i in range(length):
		distance = distance + (x[i] - y[i])**2
	return sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	#print(train)
    #train_row = [7,7,0]
    #test_row = [3,7]
	for train_row in train:
		dist = euclidean_distance(train_row, test_row)
		distances.append((train_row, dist))
        #[[3, 7], 4]
# =============================================================================
# 		print("start")
# 		print(distances)
# 		print("end")
# =============================================================================
	#print(distances)
	distances.sort(key=lambda tup: tup[1])
	#print(distances)
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	#print(neighbors)
	return neighbors

# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	print(output_values)
	#return value which has majority occurrance
	print(set(output_values))
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# =============================================================================
# # Test distance function
# dataset = [[2.7810836,2.550537003,0],
# 	[1.465489372,2.362125076,0],
# 	[3.396561688,4.400293529,0],
# 	[1.38807019,1.850220317,0],
# 	[3.06407232,3.005305973,0],
# 	[7.627531214,2.759262235,1],
# 	[5.332441248,2.088626775,1],
# 	[6.922596716,1.77106367,1],
# 	[8.675418651,-0.242068655,1],
# 	[7.673756466,3.508563011,1]]
# =============================================================================
''' 0="Bad"
    1="Good"
    '''
labels = ["Bad", "Good"]
dataset =[
        [7,7,0],
        [7,4,0],
        [3,4,1],
        [1,4,1]
        ]

test_data = [3,7]

k = int(input("Enter k value = "))
'''params
   dataset: contains samples data
   test_data: to test knn leaning model againt given data set
   k: number of neighbours
'''
#to predict class for test data
prediction = predict_classification(dataset, test_data, k)
#print('Expected %d, Got %d.' % (dataset[0][-1], prediction))
print('Got %s.' % (labels[prediction]))
