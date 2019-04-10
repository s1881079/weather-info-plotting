#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:44:05 2018
This is a program for reading file plenty.data as float 
and do some data mapping

@author: Ananomous
"""

from matplotlib import pyplot
import os


def readPlenty(file_dir):
    '''read plenty.data and convert to float'''
    data = []
    in_file = open(file_dir,'r')
    for line in in_file.readlines():
        slst_line = line.split(' ')
        flst_line = [float(item) for item in slst_line]
        data.append(flst_line)
        
    in_file.close()
    return data


def someHandle(plenty_data):
    '''exchange former half of colomn3 with latter half of column 4'''
    cl3 = [i[3] for i in plenty_data] 
    cl4 = [i[4] for i in plenty_data]
    mid_id = int(len(cl3) / 2)
    f_half3 = cl3[:mid_id]
    l_half4 = cl4[mid_id:]
    cl3[mid_id:] = l_half4
    cl4[:mid_id] = f_half3
    
    return cl3,cl4
    

def plotAllPlenty(plenty_data):
    '''plot all data in plenty.data
        using the first coloum as x and other coloums as y'''
    print('plotting all data using the first coloum as x and other coloums as y...')
    
    xid = 0
    cid_y = [i for i in range(11)]
    cid_y.remove(xid)
    
    for yid in cid_y:
        x_data = [i[xid] for i in plenty_data]
        y_data = [i[yid] for i in plenty_data]
        ax.plot(x_data,y_data)  
        
    print('plotting completed')
    return 1
    
    
if __name__ == '__main__':
    #change workspace to proper file directory
    workspace = os.getcwd()
    os.chdir(workspace)
    plenty_dir = 'plenty.data'
    
    print('data source: ' + workspace + plenty_dir)
    
    #read data
    plenty_data = readPlenty(plenty_dir)

    #plot all data as demo
    fig,ax = pyplot.subplots()
    ax = plotAllPlenty(plenty_data)
    pyplot.show()
        
    #handle some colomns
    print('exchange former half of column3 with latter half of column4 after plotting...')
    ncl3,ncl4 = someHandle(plenty_data)
    plenty_data[3],plenty_data[4] = ncl3,ncl4
    print('exchange completed')
    
    