#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 03:34:13 2019

@author: nihad
"""

import pandas as pd
import numpy as np
import math
df = pd.read_csv('/home/nihad/Desktop/Desicion Tree/iris.csv')
iris_array = df.values
iris_array
def SortingbyAttribute(data,columnIndex):
    sortedArr = data[data[:,columnIndex].argsort()]
    return sortedArr;
  
    
def DivideColumns (data,colindex):
    data = SortingbyAttribute(data,colindex)
    short = data[:50,:]
    middle = data[50:100,:]
    long = data[100:150,:]
    divided3Darray = np.array([short,middle,long])
    return divided3Darray;
data = DivideColumns(iris_array,0)


def Numberofoccurences(data,sortcolindex,g_index):
    df =  DivideColumns(data,sortcolindex)
    num_Iris_setosa = 0
    num_Iris_versicolor = 0
    num_Iris_virginica = 0
    for i in range(0,50):
           element = df[g_index, i,4]
           if(element == 'Setosa'):
               num_Iris_setosa+=1
           elif(element == 'Versicolor'):
               num_Iris_versicolor+=1
           elif (element == 'Virginica'):
               num_Iris_virginica+=1
    array1D_for_occ = np.array([num_Iris_virginica,num_Iris_versicolor,num_Iris_setosa])
    return array1D_for_occ ;


short = np.array([Numberofoccurences(iris_array,0,0),Numberofoccurences(iris_array,1,0),Numberofoccurences(iris_array,2,0), Numberofoccurences(iris_array,3,0)])
middle = np.array([Numberofoccurences(iris_array,0,1),Numberofoccurences(iris_array,1,1),Numberofoccurences(iris_array,2,1), Numberofoccurences(iris_array,3,1)])  
long = np.array([Numberofoccurences(iris_array,0,2),Numberofoccurences(iris_array,1,2),Numberofoccurences(iris_array,2,2), Numberofoccurences(iris_array,3,2)])
big_data = np.array([short,middle,long])


def find_entrophy(data,index):
    entrophy = 0
    for i in range(2):
        for j in range(3):
            entrophy-= data[index,i,j]/50 * math.log2(data[index,i,j]/50)
    return entrophy;
        
    
short_entrop = find_entrophy(big_data,0)    
middle_entrop = find_entrophy(big_data,1)
#long = find_entrophy(preparationforEntrophy(),2)

    
