# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from matplotlib import pyplot


def readSomedata(file_dir):
    infile = open(file_dir, 'r')
    some_data = []
    for line in infile.readlines():
        some_data.append([float(i) for i in line[:-1].split(' ')])
    return some_data

def plotSomedata(x_data,y_data):
    pyplot.plot(x_data,y_data,'o')
    pyplot.show()
    
    
if __name__ == '__main__':
    workspace = '/home/s1881079/tigis/prac2'
    os.chdir(workspace)
    file_dir = 'some.data'
    cwd = os.getcwd()
    print('data source file: ' + cwd)
    
    some_data = readSomedata(file_dir)
    x_data = [i[0] for i in some_data]
    y_data = [i[1] for i in some_data]
    plotSomedata(x_data,y_data)