#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:26:40 2018

@author: s1881079
"""

from datetime import datetime
import time
import re
import sys

__all__ = ['readJCMB','goodBye']


def modTomorrow(str_lstday):
    '''Generate datetime object from string when string has '24:00'
    
    datetime.strptime() cannot identify '24:00', therefore this fuction 
    generate timestamp of string containing '24:00' and then convert it to
    datetime type.
    
    ..code referencing:
        https://stackoverflow.com/questions/3493924/how-can-i-convert-the-time-in-a-datetime-string-from-2400-to-0000-in-python
    
    Parameters
    ----------
    str_lstday : str
        string of date to convert, format '%Y/%m/%d %H:%M'
        
    Returns
    -------
    datetime
        data in datetime type of the input date
        
    
    '''
    try:
        tup_lstday = tuple((int(i) for i in (re.split(r'/| |:', str_lstday))))
        tup_tail = (0,0,1,-1)
        tup_lstday += tup_tail
        time_stamp = time.mktime(tup_lstday)
    except:
        print('fail to modify time with 24:00 to 0:00')
        return None
    
    try:
        mod_tomorrow = datetime.fromtimestamp(time_stamp)
    except:
        print('fail to generate datetime from timestamp')
    
    return mod_tomorrow
    

def modifyTime(ori_strtime):
    '''Convert date information from string to datetime
    
    format of string should be like '%Y/%m/%d %H:%M'
    ''' 
    try:
        md_date = datetime.strptime(ori_strtime,'%Y/%m/%d %H:%M')
    except:
        if ori_strtime[11:13] == '24':
            try:
                md_date = modTomorrow(ori_strtime)
            except:
                print('Unexpected date format')
                return None
        else:
            print('Unexpected date format')
            return None
            
    return md_date


def modifyLine(ori_line):
    '''Modify input line 
    
    Each input string will be split by ',', with the first element 
    transformed into datetime object and the rest transformed to float.
    datetime format should be like '%Y/%m/%d %H:%M'
    
    Parameters
    ----------
    ori_line : str
        original string 
        
    Returns
    -------
    list
        list contained modified data value from the input string
        
    '''
    try:
        slst_line = ori_line[:-1].split(',')
    except:
        print('fail to spit data line with comma')
        return None
    
    md_date = modifyTime(slst_line[0])
    
    if md_date == None:
        print('fail to read date')
        return None
    
    try:
        flst_else= [float(item) for item in slst_line[1:]]
    except:
        print('fail to convert data to float')
        return None
        
    md_line = [md_date] + flst_else
    return md_line


def readHeader(in_file):
    '''Read file header
    
    Read first line of input file, split with ',' and return list of header
    
    Parameters
    ----------
    in_file
    
    Returns
    -------
    list
        list contain the data head
    int
        number of column shown in data head
        
    '''
    print('reading header...')
    data_head = in_file.readline()[:-1].split(',')
    return data_head,len(data_head)


def readValue(in_file,ncols):
    '''read value and modify by line
    
    Read values and modify by line through function modifyLine().
    If a line cannot be stored due to missing or extra column or wrong format etc., 
    this line would be skipped.
    
    Parameters
    ----------
    in_file
        file input
    ncols
        number of columns, this should be the same as the number given by readHeader(),
        which is number of cloumns of the header line in file 
        
    Returns
    -------
    list
        a result list that contants each list storing each cloumn of data
        
    '''
    print('reading value in following lines...')
    data_value = [[] for i in range(ncols)]
    
    line_num= 1
    valid_linecount = 0
    skip_linecount = 0
    
    for line in in_file.readlines():
        line_num += 1
        md_line = modifyLine(line)
        
        if md_line == None:
            print('skip line ' + str(line_num))
            skip_linecount += 1
            continue
        
        try:
            for (v_lst,v) in zip(data_value,md_line):
                v_lst.append(v)
        except:
            print('fail to include data in line ' + str(line_num) + '''to database. 
                  please check whether number of data fits with number of header''')
            print('skip line ' + str(line_num))
            skip_linecount += 1
            continue
        
        valid_linecount += 1
        
    print('total line read (except header):' + str(line_num - 1))
    print('valid lines:' + str(valid_linecount) + ' lines')
    print('skipped lines:' + str(skip_linecount) + ' lines')
        
    return data_value
    

def readJCMB(file_name):
    '''reading file JCMB_2011.csv
    
    This function is wirtten originally to read data in JCMB_2011.csv, but file with
    similar data storing format can also be read using this funciton.
    
    The required format is as follows:
        elements in each line are seperated by ',', lines are seperated by '\n'
        the first line is a header line
        data in the first coloum indicates date data, format as '%Y/%m/%d %H:%M'
        
    Parameters
    ----------
    filename : str
    
    Returns
    -------
    dict
        dictionary containing header as key and list of data as value
    list
        list of header input. Since the order of storing information in dictionary
        would be regenerated, and considering some headers are quite long and the
        possible need of further using them, the list of header are also reaturned 
        to keep the original order that can be more easily checked in the file.
        
    '''
    
    try:
        in_file = open(file_name,'r')
    except:
        print('fail to open file')
        goodBye(0)
    else:
        print('file ' + file_name + ' opened successfully')
    
    try:
        data_head,len_head = readHeader(in_file)
    except:
        print('fail to read header line, closing file...')
        in_file.close()
        return None,None
    
    
    data_value = readValue(in_file,len_head)
    
    try:
        dict_data = dict(zip(data_head, data_value))
    except:
        print('data value and header are read correctly, fail to generate dictionary')
        return None,None
    
    try:
        in_file.close()
    except:
        print('warning: file opened not closed yet')
    else:
        print('file ' + file_name + ' closed successfully')
        
    
    return dict_data,data_head


def goodBye(did_suc):
    '''a little funtion to say goodbye to my dear users :)'''
    if did_suc:
        print('Plotting process succeeded.')
        print('Congratulations! GoodBye~ :)')
        sys.exit(0)
    else:
        print('Sorry for that:( Maybe try again with another data file. \nGood luck next time! GoodBye~')
        sys.exit(1)