#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:52:56 2018

@author: s1881079
"""
import TK2
import os

if __name__ == '__main__':
    
    #define the workpath
    workspace = os.getcwd()
    os.chdir(workspace)
    jcmb_name = 'JCMB_2011.csv'
    
    #read JCMB file
    jcmb_data,jcmb_head = TK2.readJCMB(jcmb_name)
    
    #plot as demo
    fig,sucPlotDemo = TK2.picDemo(jcmb_data,jcmb_head)
    
    #plot wind sppeed and direction between 0:15 to 0:32
    fig,sucPlotWind = TK2.picWind(jcmb_data,jcmb_head,1,1,0,15,1,1,0,32,fig)
    
    #wave Goodbye~
    TK2.goodBye(sucPlotDemo & sucPlotWind)
    
    
    
