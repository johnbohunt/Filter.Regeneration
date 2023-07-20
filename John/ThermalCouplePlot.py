##################################################
#### Author  : Austin McDonald                ####
#### Modifer : Ilker Parmaksiz                ####
#### Date    : July 19 2023                   ####
##################################################

import matplotlib as pl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import datestr2num
import matplotlib.ticker as plticker
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.dates as mdates

import os
import time
import datetime as dt

# style.use('fivethirtyeight')

### Make a figure ###
fig1 = plt.figure()



# these are subplot grid parameters encoded as a single integer.
# For example, "111" means "1x1 grid, first subplot" and "234" means "2x3 grid, 4th subplot".
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)
fig1.autofmt_xdate()


def animate(i):
    # ---------------------------------------------------------------------------------------------------------------
    RangeData = np.loadtxt('TermalCouple_3_18_2022.csv', delimiter=' ', skiprows=14, dtype=str)

    ### Load the time stamp into an array ####
    xRange = np.arange(len(RangeData[:, 0]))
    dates = []
    for i in range(len(RangeData[:, 0])):
        curr = RangeData[:, 0][i] + ' ' + RangeData[:, 1][i]
        tmp = dt.datetime.strptime(curr, '%d/%m/%Y %H:%M:%S')
        dates.append(tmp)
    dates = np.array(dates)
    xRange = dates

    # xRange = [dt.datetime.strptime(M,"%d/%m/%Y %H:%M:%S").date() for M in dates]
    #print(RangeData)
    ### Load the distance (in cm) into an array ###
    Voltage = RangeData[:, 2].astype(float)
    Temp = RangeData[:, 3].astype(float)
    ### Convert the range from a string to a float ###
    # Ch0 = Ch0.astype(np.float)
    ax1.clear()
    ax2.clear()
    ax1.set_xlabel('time')
    ax2.set_xlabel('time')

    ax1.set_ylabel('Voltage(V)')
    ax2.set_ylabel('Temp(C)')

    # xfmt = mdates.DateFormatter("%d/%m/%Y %H:%M:%S")
    # minuets = mdates.MinuteLocator(interval = 10)
    # ax1.xaxis.set_major_formatter(xfmt)
    # ax1.xaxis.set_major_locator(minuets)


    # plt.gcf().autofmt_xdate()


    ax1.plot(xRange, Voltage, label="Voltage(V)", marker='o')
    ax2.plot(xRange, Temp, label="Temp(C)", marker='o')
    #ax1.legend(loc='upper left')
    #ax2.legend(loc='upper left')


ani = animation.FuncAnimation(fig1, animate, interval=5000)

mng = plt.get_current_fig_manager()
# mng.window.showMaximized()

plt.show()



