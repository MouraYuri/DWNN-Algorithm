import pandas as pd
import math
from matplotlib import pyplot as plt

def preProcessingData(data):
    for x in range(len(data)):
        data[x] = data[x].split(' ')
        data[x][1] = data[x][1].rstrip()
        data[x][0], data[x][1] = int(data[x][0]), int(data[x][1])
    df = pd.DataFrame(data, columns = ['xCordinate', 'yCordinate'])
    return df

def weight(x, xi, sigma):
    return math.exp((-(x-xi)**2)/(2*(sigma**2)))

def dwnn(dataset, x, sigma):
    u, d = 0, 0
    for z in range(len(dataset)):
        xi, yi = dataset.loc[z, 'xCordinate'], dataset.loc[z, 'yCordinate']
        u, d = u + (yi*weight(xi, x, sigma)), d + weight(xi, x, sigma)
    y = u/d
    plt.scatter(dataset.loc[:, 'xCordinate'], dataset.loc[:,'yCordinate'], color='blue')
    plt.scatter(x, y, color='red')
    plt.show()
dataset = open('./DWNN/dataset.txt', 'r')
dataset = preProcessingData(dataset.readlines())
dwnn(dataset, 6, 0.1)