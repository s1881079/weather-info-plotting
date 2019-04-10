# Weather Data Plotting

This is a coursework of Technological Infrastructures for GIS

## Data

* **plenty.data**

simple x-y coordinates for plotting test


* **JCMB_2011.csv**

whether data per minute from 2011.1 - 2011.10


## Examples

**plotting multi-lines**

plotting colorful multilines using coordinates from plenty.data using matplotlib

run

```
python3 task1_plenty.py
```


result figure

![Alt text](./rst_figs/multi_line.PNG?raw=true)

**plotting whether information**

Ideally, a figure looks similar to the demo on slide would be shown, and after the user closes it, another figure about wind speed and wind direction during 2011-1-1 00:15:00 to 2011-1-1 00:32:00 would pop up on the screen. you can change parameter to see wind data in other time period, but it is recommended to narrow the period within 20min. See detail in TK2.picWind() in demoplot.py

if file being successfully read and plotted, the function would exit with 0, otherwise it would print something relavant to possible exception and exit with 1. file input should be comma delimited and has the first line as header line.the number of colum in header line would be considered as the number of  column os the whole file, following lines with missing or extra columns would be considered as bad  data line and therefore be skipped. total number of skipped lines and valid lines would be print on screen.

run

```
python3 t2_jcmb.py
```

result figure

![Alt text](./rst_figs/multi_weather.PNG?raw=true)
![Alt text](./rst_figs/windplot.PNG?raw=true)

## Author

* **Louise Liu**
