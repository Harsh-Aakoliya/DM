# -*- coding: utf-8 -*-
"""DM_7_apriory_general_my.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1emOE7ZwbQ5jpvahj9LMoZLhAhugUm4wK
"""

print("apriori")
import pandas as pd

df=pd.read_csv("/content/Market_Basket_Optimisation.csv")
df

tempdf=df.to_numpy()
tempdf

print(tempdf)
data={}
id=0
for i in tempdf:
  temp=[]
  for j in i:
    if(pd.notna(j)):
      temp.append(j)

  data[id]=temp
  id=id+1

print(data)

# dic={
#     "1":["I1","I2","I5"],
#     "2":["I2","I4"],
#     "3":["I2","I3"],
#     "4":["I1","I2","I4"],
#     "5":["I1","I3"],
#     "6":["I2","I3"],
#     "7":["I1","I3"],
#     "8":["I1","I2","I3","I5"],
#     "9":["I1","I2","I3"]
# }
dic={
    "1":["Bear","Nuts","Diper"],
    "2":["Bear","Coffee","Diper"],
    "3":["Bear","Diper","egg"],
    "4":["Nuts","egg","milk"],
    "5":["Nuts","Coffee","Diper","egg","milk"]
}
# dic=data
min_support=2
min_confidence=3
all={}

unique=set()
for i in dic.values():
  for j in i:
    unique.add(j)

print(unique)

name2num={}
id=1
for i in unique:
  name2num[i]=id
  id=id+1

print(name2num)

def Merge(dict1, dict2):
  return(dict2.update(dict1))

#runnig algorithm one time
original=dic
pre={}#dictionary of list of item and support count
for i in unique:
  item_set = set()
  item_set.add(i)

  #count of i1 in whole dataset, count of i2 in whole dataset ....
  supportCnti=0
  for j in dic.values():
    supportCnti=supportCnti+j.count(i)

  # print("count of ",i," is ",supportCnti)

  # print(item_set,supportCnti)
  pre[frozenset(item_set)]=supportCnti

# Merge(all,pre)
# print(all)

for i in pre:
  for j in i:
    print(j, end=" ")
  print(pre[i])

def all_subset(s):
  if len(s) == 0:
      return [[]]
  x = all_subset(s[:-1])
  return x + [[s[-1]] + y for y in x]

def check_prun(key,dic):
  print(key)
  lst=list(key)
  print(lst)
  all_subset(lst)
  allsubsets=(all_subset(lst))
  print(allsubsets)
  return True

def rmv1(pre,min_support):
  new_pre = {}
  for key,val in pre.items():
    if(val>=min_support):
      new_pre[key] = val

  # print("here")
  return new_pre

removed=rmv1(pre,min_support)

# print(removed)
for i in removed:
  for j in i:
    print(j, end=" ")
  print(pre[i])

# def have_to_take_first(frozen1,frozen2,dic):
#   first=list(frozen1)
#   second=list(frozen2)
#   print(first,second)


def count_combined(frozen_combined,dic):
  combined=list(frozen_combined)
  print(dic)
  new_cnt=0
  for i in dic:
    cmplst=dic[i] #["I1","I2","I5"],["I2","I4"]
    flag=True
    for i in combined:
      if(i in cmplst):
        continue
      else:
        flag=False
    # all_present = all(element in cmplst for element in combined)
    if(flag==True):
      new_cnt=new_cnt+1

  return new_cnt


def rmv(pre,min_support):
  new_pre = {}
  for key,val in pre.items():
    if(val>=min_support and check_prun(key,dic)):
      new_pre[key] = val

  # print("here")
  return new_pre

cur={}
i=0
for frozen1,support1 in pre.items():
  j=0
  for frozen2,support2 in pre.items():
    # print(i,j)
    # print(frozen1,support1)
    # print(frozen2,support2)
    if(j<=i):
      j=j+1
      continue
    else:
      combined = frozen1.union(frozen2)
      new_cnt=count_combined(combined,dic)
      cur[combined]=new_cnt
    j=j+1
  i=i+1

# print(cur)
# for i in cur:
#   print(i,cur[i])

def have_to_take(frozen1,frozen2,dic):
  first=list(frozen1)
  second=list(frozen2)
  first.sort()
  second.sort()

  # print(first,second)
  if(first[:len(first)-1] != second[:len(second)-1]):
    return False

  return True

while(True):
  pre=cur
  for i in pre:
    for j in i:
      print(j, end=" ")
    print(pre[i])

  print()
  print()
  # print("pre",pre)
  pre=rmv(pre,min_support)
  # print("pre",pre)
  for i in pre:
    for j in i:
      print(j, end=" ")
    print(pre[i])
  print()
  cur={}

  # break

  i=0
  for frozen1,support1 in pre.items():
    j=0
    for frozen2,support2 in pre.items():
      if(j<=i):
        j=j+1
        continue
      elif(have_to_take(frozen1,frozen2,original)):
        combined = frozen1.union(frozen2)
        new_cnt=count_combined(combined,dic)
        cur[combined]=new_cnt
        # print("have to take ",frozen1,frozen2)
        # break
      j=j+1
      # break
    i=i+1
    # break
  # break
  if(cur=={}):
    break
  # till=till+1


print("final table")
for i in pre:
  for j in i:
    print(j, end=" ")
  print(pre[i])
print()
