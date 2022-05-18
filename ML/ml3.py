import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from math import sqrt
from collections import Counter

style.use('fivethirtyeight')
plt.figure(figsize=(5, 5))
dataset = {'positive':[[4,4], [6,2]], 'negative':[[2,4], [4,2], [4,6], [6,4]]}
point = [6,6]
colors = ['b', 'orange']
marker = ['o', 's']
k=0

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
        
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

for i in dataset:
    for j in dataset[i]:
        plt.scatter(j[0], j[1], s=80, c=colors[k], marker=marker[k])
    k = k+1
        
result = k_nearest_neighbors(dataset, point)
if result == 'positive':
    color = 'b'
    marker = 'o'
    
else:
    color = 'orange'
    marker = 's'
        
plt.scatter(point[0], point[1], s=200, c=color, marker=marker)
plt.show()
        
    
print(result)