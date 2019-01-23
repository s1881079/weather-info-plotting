#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:13:22 2018

@author: s1881079
"""
from matplotlib import pyplot
#from matplotlib import ticker
import numpy.ma as ma
import datetime

__all__ = ['canPic','getDataByTime','picDemo','picWind']

def canPic(dict_data,list_head):
    '''Check whether the columns area qualified to plot (not empty) 
    
    Parameters
    ----------
    dict_data : dict
        dictionry containing the data
    list_head : list
        list of header specifying the colomn(s) ready to plot
    
    Returns
    -------
    bool
        showing whether the column(s) specified are not empty
    
    
    '''
    print('checking data...')
    
    list_coltoPic = [dict_data[head] for head in list_head]
    ncol = 0
    for col in list_coltoPic:
        if col == []:
            print('colomn ' + list_head[ncol] + ' is empty, not able to plot.')
            return False
        ncol += 1

    return True

        

def plotData(ax,dict_data,str_x,str_y,show_x,show_y,nodata = -9999):
    '''input data into the x-y plot
    
    Parameters
    ----------
    ax_data : matplotlib.axes
    
    dict_data : dict
        dictionary of the data
    str_x : str
        string indicating x axis to plot, this should be one of the keys in dict_data
    str_y : str
        strign indicating y axis to plot, this should be one of the keys in dict_data
    show_x : bool
        whether to show the label of x-axies
    show_y : bool
        whether to show the label of y-axies
    nodata:
        define the nodata value that need to be masked, default is -9999
    
    this funtion is for mapping the data out in the plot'''
        
    x_data = dict_data[str_x]
    y_data = dict_data[str_y]
    y_mdata = ma.masked_values(y_data,nodata)
    
    ax.plot(x_data,y_mdata)
    if show_x : ax.set_xlabel(str_x)    
    if show_y : ax.set_ylabel(str_y)
    
    return 1
    

def setDemoFormat(fig,axs):
    '''formatting the axis and graph
    making the result look similar to the demo on slide'''
    
    fig.suptitle('This is the Demo',fontweight = 'bold')
    ax_surtp,ax_rain,ax_windsp= axs
    fig.subplots_adjust(wspace = 1.3,bottom = 0.2)
    
#    ax_surtp.yaxis.set_major_locator(ticker.LinearLocator(3))
#    ax_rain.yaxis.set_major_locator(ticker.LinearLocator(3))
#    ax_windsp.yaxis.set_major_locator(ticker.LinearLocator(5))
    
        
    ax_windsp.tick_params(axis = 'x',labelrotation = 45)
    
    
    return 1


def getDataByTime(dict_data,key_date,s_month,s_day,s_h,s_min,e_month,e_day,e_h,e_min):
    '''To extract data specifed by date
    
    Parameters
    ----------
    dict_data : dict
        dictionary that contains the whole dataset
    key_date
        string that indicate the key of date in data dictionary
    s_month : int
        start month defined by user
    s_day : int
        start date defined by user
    s_h : int
        start hour defind by user
    s_min : int
        start minute defined by user
    e_month : int
        end month defined by user
    e_day : int
        end date defined by user
    e_h : int
        end hour defind by user
    e_min : int
        end minute defined by user
    
    
    Returns
    -------
    dict
        dictionary containning only data of the spcified date
    '''
    try:
        datetime.datetime(2011,s_month,s_day,s_h,s_min,0)
        datetime.datetime(2011,e_month,e_day,e_h,e_min,0)
    except:
        print('Invalid datetime range defined')
        return None
        
    st_time = datetime.datetime(2011,s_month,s_day,s_h,s_min,0)
    ed_time = datetime.datetime(2011,e_month,e_day,e_h,e_min,0)
    
    data_of_the_day = dict_data.copy()
    for key in data_of_the_day:
        data_of_the_day.update({key:[]})
    
    row_count = 0
    for date in dict_data[key_date]:
        if st_time < date < ed_time:
            for key, value in zip(data_of_the_day.keys(),data_of_the_day.values()):
                data_of_the_day.update({key:value + [dict_data[key][row_count]]})
            
        row_count += 1
        
    return data_of_the_day
            

def initFig(fig = None):
    '''initializing figure
    
    create when not exist, clear when exisited
    
    '''
    #pyplot.ion()
    if fig == None:
        try:
            fig= pyplot.figure()         
        except:
            print('fail to generate original plot, check the matplotlib module for help')
            return None
    else:
        fig.clf()
        
    return fig
    

def picDemo(full_dict,full_head,fig = None):
    '''ploting particular coloumns of data as demo in slide
    
    This function plots the surface tempreture, windspeed and rainfall data
    
    in JCMB_2011.csv. We assume that the order of header in file is as follow:
        date, atosphere preessure, rainfall, windspeed, windirection, 
        surface tempreture, relative humidity, solar flux, 
        steven screen tempreture, battery.
        
    if the order of header changed while remaining the same number, it would not plot as domo 
    but as long asthe datain the relative colomn is float type, but it would still plot it.
    
    Parameters
    ----------
    full_dict : dict
        dictionary of the whole dataset
    full_head : list
        list of data head remain the same order as shown in file
    fig : matplotlib.figure, optional
        figure to show the data
        
    Returns
    -------
    matplotlib.figure
        figure that shows data plotting
    bool
        showing whether succeeded in plotting
    '''

#    nodata = -9999
    fig = initFig(fig)
    axs = fig.subplots(3,1,sharex = True)
    
    try:
        str_date, str_atpres, str_rain, str_windsp,str_winddr,str_surtp,str_humid,str_solar,str_scrtp,str_battery = full_head
    except:
        print('header length import does not fmatch JCMB_2011.csv')
        return None,False
    
    list_demoHeader = [str_date,str_surtp,str_windsp,str_rain]
    if canPic(full_dict,list_demoHeader) == False:
        return None,False
        
    print('plotting Demo...')
    
    ax_surtp,ax_rain,ax_windsp= axs
    
    plotData(ax_surtp,full_dict,str_date,str_surtp,0,1)
    plotData(ax_windsp,full_dict,str_date,str_windsp,1,1)
    plotData(ax_rain,full_dict,str_date,str_rain,0,1)
    
    setDemoFormat(fig,axs)
    
    #pyplot.ioff()
    pyplot.show()
    return fig,True


def picWind(full_dict,full_head,s_month,s_day,s_h,s_min,e_month,e_day,e_h,e_min,fig = None):
    '''ploting data in tipical time period in polar coordinate system
    
    in this task, this is function is created for plotting wind speed and wind direction.
    considering the visualization effect, it is recommended to plot no more than 20 records
    in a time - which means the time period below 20 minutes.
    
    Parameters
    ----------
    full_dict : dict
        dictionary that contains the whole dataset
    full_head : list
        list of header of data
    s_month : int
        start month defined by user
    s_day : int
        start date defined by user
    s_h : int
        start hour defind by user
    s_min : int
        start minute defined by user
    e_month : int
        end month defined by user
    e_day : int
        end date defined by user
    e_h : int
        end hour defind by user
    e_min : int
        end minute defined by user
    fig : matplotlib.figure, optional
        figure to show the data
        
    Returns
    -------
    bool
        showing whether the plotting process has succeeded
    '''
    
    fig = initFig()
    ax = fig.add_subplot(111,projection = 'polar')

    try:
        str_date, str_atpres, str_rain, str_windsp,str_winddr,str_surtp,str_humid,str_solar,str_scrtp,str_battery = full_head
    except:
        print('header length import does not match JCMB_2011.csv')
        return None,False
    
    list_demoHeader = [str_windsp,str_winddr]
    if canPic(full_dict,list_demoHeader) == False:
        return None,False
    
    print('plotting Wind...')
    
    
    day_data = getDataByTime(full_dict,str_date,s_month,s_day,s_h,s_min,e_month,e_day,e_h,e_min)
    if day_data == None:
        return None, False
    
    winddir = day_data[str_winddr]
    windsp = day_data[str_windsp]
    bars = ax.bar(winddir, windsp, bottom = 0.0)
    
    for r,bar in zip(windsp,bars):
        bar.set_facecolor(pyplot.cm.viridis(r / 5.))
        bar.set_alpha(0.5)
    
    fig.suptitle('Wind spped and direction',fontweight = 'bold')
    #pyplot.ioff()
    pyplot.show()
    #fname = 'wind_fig.svg'
    #pyplot.savefig(fname)
    
    return fig,True
