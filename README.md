# DWNN-Algorithm
Distance weighted nearest neighbours algorithm it's a supervised learning classification algorithm.

## Abstract:  
This algorithm receive as input a training set with N points, a sigma value and the query point. After that the algorithm  
associates weights to all points in dataset, points closer to the query point will receive bigger values. Then, it's calculated  
the mean between the y cordinates (classes) of our dataset using the weights that was computed before. The result value it's  
the approximation of the query point class.

## Example:  
  
#### Query point = 6, sigma = 0.1

#### Dataset (Blue points):  
![Dataset](https://raw.githubusercontent.com/MouraYuri/DWNN-Algorithm/master/datasetPlot.png)

#### Dataset and the result (red point):  
![DatasetAndResult](https://raw.githubusercontent.com/MouraYuri/DWNN-Algorithm/master/datasetAndQueryPoint.png)

## Tools used:  
1. Pandas  
2. Matplotlib
