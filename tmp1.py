#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:12:25 2018

@author: s1881079
"""

from matplotlib import pyplot
import os


cid_x = [i for i in range(11)]
cid_y = [i for i in range(11)]


for xid in cid_x:
    cid_y.remove(xid)
    for yid in cid_y:
        print(xid,yid)
#            x_data = [i[xid] for i in plenty_data]
#            y_data = [i[yid] for i in plenty_data]
#            line, = ax.plot(x_data,y_data)
    cid_y = [i for i in range(11)]
    
    
fig,ax = pyplot.subplots()

for x in range(10):
    x = x + 1
    x_data = [i[0] for i in plenty_data]
    y_data = [i[x] for i in plenty_data]
    ax.plot(x_data,y_data)

pyplot(x_data,y_data)


testlist = [i for i in range(10)]
for i in range(10):
    print(testlist)
    
for i in testlist:
    print(i)
    i = i + 1
    newlist = []
    #attention: this line should not be set inside the iteration
    newlist.append(i)
    print(testlist)
    
