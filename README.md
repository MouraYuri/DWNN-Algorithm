# DWNN-Algorithm
Distance weighted nearest neighbours algorithm  
Supervised learning classification algorithm.

## Abstract:  
This algorithm receive as input a training set with N points, a sigma value and the query point. After that the algorithm  
associates weights to all points in dataset, points closer to the query point will receive bigger values. Then, it's calculated  
the mean between the y cordinates (classes) of our dataset using the weights that was computed before. The result value it's  
the approximation of the query point class.

## Example:  
### query point = x = 6, sigma = 0.1
