# -*- coding: utf-8 -*-
"""
Created on Mon Oct 08 21:27:13 2018

@author: hp
"""
from matplotlib import pyplot
from matplotlib import ticker
from datetime import datetime
import time
import re
import os
import numpy.ma as ma


    


    
#========================================== TASK 2
    

def modTomorrow(str_lstday):
    '''change to standard expression if things like '24:00' occures'''
    tup_lstday = tuple((int(i) for i in (re.split(r'/| |:', str_lstday))))
    tup_tail = (0,0,1,-1)
    tup_lstday += tup_tail
    time_stamp = time.mktime(tup_lstday)
    
    return time_stamp
    
    

def modifyTime(ori_strtime):
    '''convert date information from string to datetime''' 
    try:
        md_date = datetime.strptime(ori_strtime,'%Y/%m/%d %H:%M')
    except:
        if ori_strtime[11:13] == '24':
            t_stamp = modTomorrow(ori_strtime)
            md_date = datetime.fromtimestamp(t_stamp)
        
    return md_date


def readJCMB(file_dir):
    '''funciton used to read JCMB_2011.CSV,process incuding:
        changing data_type to datetime
        removing '/n' in the tail of lines
        removing missing value
        create dictionary to store the data'''
    
    data_value = [[] for i in range(10)]
    in_file = open(file_dir,'r')
    data_head = in_file.readline()[:-1].split(',')
    
    for line in in_file.readlines():
        slst_line = line[:-1].split(',')
        md_date = modifyTime(slst_line[0])
        flst_else= [float(item) for item in slst_line[1:]]
        mdform_value = [md_date] + flst_else
        
        for (v_lst,v) in zip(data_value,mdform_value):
            v_lst.append(v)
        
    in_file.close()
    
    data_dict = dict(zip(data_head, data_value))
    return data_dict,data_head
    

def plotDemo(ax,data_dict,str_x,str_y,show_x,show_y,nodata = -9999):
    '''this funtion is for mapping the data out in the plot'''
        
    x_data = data_dict[str_x]
    y_data = data_dict[str_y]
    y_mdata = ma.masked_values(y_data,nodata)
    
    ax.plot(x_data,y_mdata)
    if show_x : ax.set_xlabel(str_x)    
    if show_y : ax.set_ylabel(str_y)
    
    return 1
    

def setDemoFormat(fig,axs):
    '''this funtion is for formatting the mapping process
        making the result look similar to the demo on slide'''

    ax_surtp,ax_rain,ax_windsp= axs
    fig.subplots_adjust(wspace = 1.3,bottom = 0.2)
    
    ax_surtp.yaxis.set_major_locator(ticker.LinearLocator(3))
    ax_rain.yaxis.set_major_locator(ticker.LinearLocator(3))
    ax_windsp.yaxis.set_major_locator(ticker.LinearLocator(5))
    
        
    ax_windsp.tick_params(axis = 'x',labelrotation = 45)
    
    
    return 1


def picDemo(full_data,full_head):
    '''this funtion is for ploting particular coloumns of data in jcmb_2011.csv'''

#    nodata = -9999
    str_date, str_atpres, str_rain, str_windsp,str_winddr,str_surtp,str_humid,str_solar,str_scrtp,str_battery = full_head
    fig,axs = pyplot.subplots(3,1,sharex = True)

    fig.suptitle('This is the Demo',fontweight = 'bold')
    
    ax_surtp,ax_rain,ax_windsp= axs
    
#    ax_surtp = plotDemo(ax_surtp,jcmb_data,str_date,str_surtp,0,1)
#    ax_windsp = plotDemo(ax_windsp,jcmb_data,str_date,str_windsp,1,1)
#    ax_rain = plotDemo(ax_rain,jcmb_data,str_date,str_rain,0,1)
    
    plotDemo(ax_surtp,full_data,str_date,str_surtp,0,1)
    plotDemo(ax_windsp,full_data,str_date,str_windsp,1,1)
    plotDemo(ax_rain,full_data,str_date,str_rain,0,1)
    
    setDemoFormat(fig,axs)
    
    return 1


if __name__ == '__main__':
    workspace = '/home/s1881079/tigis/prac2'
    os.chdir(workspace)
    
    jcmb_dir = 'JCMB_2011.csv'
    jcmb_data,jcmb_head = readJCMB(jcmb_dir)
    
    picDemo(jcmb_data,jcmb_head)
    #fig,axs = picDemo(jcmb_data,jcmb_head)
    pyplot.show()
    
    #plot date-atmospher

    
    
    




