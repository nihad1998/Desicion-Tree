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
data


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

