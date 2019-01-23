Run t2_jcmb.py to readfile JCMB_2011.csv and plot data.

Ideally, a figure looks similar to the demo on slide would be shown, and after
the user closes it, another figure about wind speed and wind direction during
2011-1-1 00:15:00 to 2011-1-1 00:32:00 would pop up on the screen. (I am not really
sure about this process because sometimes the function runs successfully but the wind figure
would not pops out on screen. I looked up on the website and found people having the same
problem that pyplot.show() could not excute twice, but i did success sometime...I am still working 
on this, and hopefully it would do well on your computer:) ) you can change parameter to see wind
data in other time period, but it is recommended to narrow the period within 20min. See detail in
TK2.picWind() in demoplot.py

if file being successfully read and plotted, the function would exit with 0, otherwise it would print
something relavant to possible exception and exit with 1. file input should be comma delimited and has
the first line as header line.the number of colum in header line would be considered as the number of 
column os the whole file, following lines with missing or extra columns would be considered as bad 
data line and therefore be skipped. total number of skipped lines and valid lines would be print on screen.

and there's a funtion to say goodbye, hope every user would get a smilling face in the end :)