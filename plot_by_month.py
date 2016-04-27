# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 16
Oscar Johnson 24 March 2016

Copyright Oscar Johnson 2016
"""

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


def listify(file):
    """
    takes input .csv file and splits on commas
    returns list of lists, pertaining to columns 
    first item in each list is the column name
    """
    my_lists = []
    for line in file:
        li = line.replace('\n', '')
        l = li.split(',')
        my_lists.append(l)
    return my_lists


def p(df):
    spec = set(df['Species'])
    counts = []
    for s in spec:
        for row in df:
            if s == row[0]:


def array(my_list):
    """convert list to numpy array"""
    array = np.array(my_list)
    return array


def main():
    months = ('Jan', 'Feb', 'Mar', 'Apr',
              'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec')
    df = pd.read_csv('/Users/home/LA_Tissues/LA_month_tissue_DB.csv')    
    p(df)


    """fname = cbook.get_sample_data('/Users/home/LA_Tissues/LA_month_tissue_DB.csv', asfileobj=False)
    my_file = open('/Users/home/LA_Tissues/LA_month_tissue_DB.csv', 'r')
    lists = listify(my_file)
    
    l = []
    for line in lists:
        if line[0] == 'Dendroica_pinus':
            l.append(line)
            print(line)    
    
    
    
    my_array = array(lists)
    my_array.sort()
    if str in my_array[:,0] == 'Dendroica_pinus':
        print(str)
        
    for line in my_array:
        if line[0]== 'Dendroica_pinus' or line[1] == 'Dendroica_pinus':
            # print(my_array[:,0])
            print(line)

    print(my_array[:,0])
    
    for line in lists:
        print(line)
    """

if __name__ == '__main__':
    main()
