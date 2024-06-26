# -*- coding: utf-8 -*-
"""DM_9_kmeans_clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QruFGalJE2l2wcjgGyMISjZt9ltGhl_K
"""

print("practical 9")

import numpy as np

# Define the data points
data_points = {
    'A1': np.array([1, 2]),
    'A2': np.array([2, 3]),
    'A3': np.array([9, 4]),
    'A4': np.array([10, 1]),
    'B1': np.array([5, 8]),
    'B2': np.array([7, 5]),
    'B3': np.array([6, 4]),
    'C1': np.array([4, 2]),
    'C2': np.array([4, 9])
}

# Initialize cluster centers
initial_centers = {
    'A': np.array([1, 2]),
    'B': np.array([5, 8]),
    'C': np.array([4, 2])
}

print(data_points)

import matplotlib.pyplot as plt
import numpy as np

x1=np.array(data_points["A1"][0])
x1=np.append(data_points["A2"][0])
x1=np.append(data_points["A3"][0])
y1=np.array(data_points["A1"][1])
y1=np.append(data_points["A2"][1])
y1=np.append(data_points["A3"][1])

def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def assign_clusters(data_points, centers):
    clusters = {}
    for point_label, point in data_points.items():
        min_distance = float('inf')
        closest_center = None
        for center_label, center in centers.items():
            distance = euclidean_distance(point, center)
            if distance < min_distance:
                min_distance = distance
                closest_center = center_label
        if closest_center in clusters:
            clusters[closest_center].append(point_label)
        else:
            clusters[closest_center] = [point_label]
    return clusters

def update_centers(data_points, clusters):
    new_centers = {}
    for center_label, cluster_points in clusters.items():
        cluster_mean = np.mean([data_points[point] for point in cluster_points], axis=0)
        new_centers[center_label] = cluster_mean
    return new_centers

# Initial assignment
clusters = assign_clusters(data_points, initial_centers)
clusters = assign_clusters(data_points, initial_centers)
# Update centers
new_centers = update_centers(data_points, clusters)

# Second round
clusters = assign_clusters(data_points, new_centers)
new_centers = update_centers(data_points, clusters)

print("Cluster centers after the 2nd round:")
print(new_centers)
print("Clusters after the 2nd round:")
print(clusters)

import numpy as np
import matplotlib.pyplot as plt

# Define the data points
data_points = {
    'A1': np.array([1, 2]),
    'A2': np.array([2, 3]),
    'A3': np.array([9, 4]),
    'A4': np.array([10, 1]),
    'B1': np.array([5, 8]),
    'B2': np.array([7, 5]),
    'B3': np.array([6, 4]),
    'C1': np.array([4, 2]),
    'C2': np.array([4, 9])
}

# Initialize cluster centers
initial_centers = {
    'A': np.array([1, 2]),
    'B': np.array([5, 8]),
    'C': np.array([4, 2])
}

# Function to assign clusters
def assign_clusters(data_points, centers):
    clusters = {}
    for point_label, point in data_points.items():
        min_distance = float('inf')
        closest_center = None
        for center_label, center in centers.items():
            distance = np.linalg.norm(point - center)
            if distance < min_distance:
                min_distance = distance
                closest_center = center_label
        if closest_center in clusters:
            clusters[closest_center].append(point)
        else:
            clusters[closest_center] = [point]
    return clusters

# Assign clusters
clusters = assign_clusters(data_points, initial_centers)

# Plot the clusters
colors = ['red', 'blue', 'green']
fig, ax = plt.subplots()

for i, (center_label, center) in enumerate(initial_centers.items()):
    ax.scatter(center[0], center[1], color=colors[i], marker='x', label=f'Cluster {center_label}')

for i, (cluster_label, cluster_points) in enumerate(clusters.items()):
    cluster_points = np.array(cluster_points)
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors[i], label=f'Cluster {cluster_label}')

ax.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('C-Means Clustering')
plt.grid(True)
plt.show()













import numpy as np

# Initialize an empty 2D numpy array with shape (rows, columns)
rows = 3
columns = 4
empty_array = np.empty((rows, columns))

print(empty_array)

pnt=np.array([
    [2,10],
    [2,5],
    [8,4],
    [5,8],
    [7,5],
    [6,4],
    [1,2],
    [4,9],
])

print(pnt)

# # Extract x and y coordinates
# x = pnt[:, 0]
# y = pnt[:, 1]

# # Plot the scatter plot
# plt.scatter(x, y, color='blue', label='Points')

# # Add point coordinates as text
# for i, (x, y) in enumerate(zip(pnt[:, 0], pnt[:, 1])):
#     plt.text(x, y, f'({x},{y})', fontsize=9, ha='left', va='bottom')

# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Scatter Plot of Points with Coordinates')
# plt.legend()
# plt.grid(True)
# plt.show()

cls=np.array([
    [2,10],
    [5,8],
    [1,2]
],dtype=float)

# Extract x and y coordinates for points and cluster centroids
pnt_x = pnt[:, 0]
pnt_y = pnt[:, 1]

cls_x = cls[:, 0]
cls_y = cls[:, 1]

# Plot the points and cluster centroids
plt.scatter(pnt_x, pnt_y, color='blue', label='Points')
plt.scatter(cls_x, cls_y, color='red', label='Cluster Centroids')
for i, (x, y) in enumerate(zip(pnt_x, pnt_y)):
  plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(5, 5), ha='center')

for i, (x, y) in enumerate(zip(cls_x, cls_y)):
  plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(5, 5), ha='center')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Points and Cluster Centroids')
plt.legend()
plt.grid(True)
plt.show()

import math

def calculate_distance(x1,y1,x2,y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

dis={}
for i in range(len(pnt)):
  x1=pnt[i][0]
  y1=pnt[i][1]
  ithdis=[]
  for j in range(len(cls)):
    x2=cls[j][0]
    y2=cls[j][1]

    # ithdis.append(dis(x1,y1,x2,y2))
    distance = calculate_distance(x1, y1, x2, y2)
    ithdis.append(distance)

  print(x1,y1,ithdis)
  min_index = np.argmin(ithdis)
  min_distance = min(ithdis)
  if min_index in dis:
      dis[min_index].append((x1, y1))
  else:
      dis[min_index] = [(x1, y1)]


print(dis)

new_cls=cls
for key,value in dis.items():
  new_x=0
  new_y=0
  # print(type(value))
  # print(value[0][0])
  for i in value:
    new_x+=(i[0])
    new_y+=i[1]
  print(new_x,new_y)

  new_cls[key]=np.array([float(new_x/(len(value))),float(new_y/len(value))])

print(new_cls)

# Extract x and y coordinates for points and cluster centroids
pnt_x = pnt[:, 0]
pnt_y = pnt[:, 1]

cls_x = cls[:, 0]
cls_y = cls[:, 1]

# Plot the points and cluster centroids
plt.scatter(pnt_x, pnt_y, color='blue', label='Points')
plt.scatter(cls_x, cls_y, color='red', label='Cluster Centroids')
for i, (x, y) in enumerate(zip(pnt_x, pnt_y)):
  plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(5, 5), ha='center')

for i, (x, y) in enumerate(zip(cls_x, cls_y)):
  plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(5, 5), ha='center')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Scatter Plot of Points and Cluster Centroids')
# plt.legend()
# plt.grid(True)
# plt.show()


# Extract x and y coordinates for points and cluster centroids
pnt_x = pnt[:, 0]
pnt_y = pnt[:, 1]

cls_x = new_cls[:, 0]
cls_y = new_cls[:, 1]

# Plot the points and cluster centroids
plt.scatter(pnt_x, pnt_y, color='blue', label='Points')
plt.scatter(cls_x, cls_y, color='red', label='Cluster Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Points and Cluster Centroids')
plt.legend()
plt.grid(True)
plt.show()

