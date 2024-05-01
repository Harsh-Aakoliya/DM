# -*- coding: utf-8 -*-
"""21BCE029_PRAC8_DM_apriory_on_dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rPvAwSRXM2BNqbl9buorERkENl7S9us2
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

Data =pd.read_csv("/kaggle/input/dblp-authors-dataset/final.csv")

Data.head()

d=Data.head(1000)
d

# cn=[]

# for value in d:
#     value=value[1:-1]
#     i=value.split(", ")
#     for j in i:
#         j=j[1:-1]
#         if j not in cn:
#             cn.append(j)

# len(cn)

data = {}

for _, row in d.iterrows():
    conferences = row['conference']
    if isinstance(conferences, str):
        conferences = conferences.strip("[]").split(", ")
        for conference in conferences:
            # Remove single quotes from the conference string
            conf = conference.strip("'")
            if conf not in data:
                data[conf] = []
            data[conf].append(row['author'])

data

values_list = [value for sublist in data.values() for value in sublist]

# print(values_list)
len(values_list)

values_list=list(set(values_list))
values_list
# len(values_list)
# vl

s=4

from collections import Counter

data



c = Counter()
for i in values_list:
    for key,val in data.items():
        if(i in val):
            c[i]+=1
print("C1:")
for i in c:
    print(str([i])+": "+str(c[i]))
print()

l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]
print("L1:")
for i in l:
    print(str(list(i))+": "+str(l[i]))
print()

pl = l
pos = 1
for count in range (2,1000):
    nc = set()
    temp = list(l)
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union(temp[j])
            if(len(t) == count):
                nc.add(temp[i].union(temp[j]))
    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i] = 0
        for key,val in data.items():
            temp = set(val)
            if(i.issubset(temp)):
                c[i]+=1
    print("C"+str(count)+":")
    for i in c:
        print(str(list(i))+": "+str(c[i]))
    print()
    l = Counter()
    for i in c:
        if(c[i] >= s):
            l[i]+=c[i]
    print("L"+str(count)+":")
    for i in l:
        print(str(list(i))+": "+str(l[i]))
    print()
    if(len(l) == 0):
        break
    pl = l
    pos = count
print("Result: ")
print("L"+str(pos)+":")
for i in pl:
    print(str(list(i))+": "+str(pl[i]))
print()

