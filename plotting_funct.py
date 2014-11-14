from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import numpy as np
import csv
from itertools import cycle
from utils import *

figs = ['org','expo','combo','fixed']
graph_a = ['12-24','25-50','50-100','100-200','150-300']
graph_b = ['150-151','150-155','150-175','150-200','150-300']

graph_a_labels = ['12--24 ms','25--50 ms','50--100 ms','100--200 ms','150--300 ms']
graph_b_labels = ['150--151 ms','150--155 ms','150--175 ms','150--200 ms','150--300 ms']

lines = ["-","--","-.",":"]

def plot_graph_a (data_x,data_y,name):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

    # for line colours

    linecycler = cycle(lines)

    for line in graph_a:
        if (len(data_x[line]) != len(data_y)):
            print (line)
        axes.plot(data_x[line],data_y,next(linecycler), lw=1.0)

    # labels
    axes.set_xlabel('Time to elect leader [ms]',fontsize=9)
    axes.set_ylabel('Cumulative percent',fontsize=9)
    if "diago" in name:
      axes.set_title('\\textbf{Original}~(Ongaro and Ousterhout)',fontsize=9)
    elif not("combo" in name) and not ("expo" in name) and not ("fixed" in name):
      axes.set_title('\\textbf{Reproduction}',fontsize=9)

    # ticks & axes
    x_marked = range(0, 401, 50)
    axes.set_xticks(x_marked)
    axes.set_xticklabels([str(x) for x in x_marked])
    y_marked = [0,20,40,60,80,100]
    axes.set_yticks(y_marked)
    axes.set_yticklabels(['0%','20%','40%','60%','80%','100%'])
    axes.set_xlim([0,400])

    axes.legend(graph_a_labels,loc=4,frameon=False,handlelength=2.5)
    fig.show()
    fig_to_file(fig,'graph_a_'+name,'pdf')


# In[ ]:

def plot_graph_b(data_x,data_y,name,x_min=0,x_max=10000,log=True,letter=''):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

    linecycler = cycle(lines)

    for line in graph_b:
        if (len(data_x[line]) != len(data_y)):
            print (line)
            print (len(y_axis))
        axes.plot(data_x[line],data_y,next(linecycler), lw=1.0)

    # labels
    xlabel = 'Time to elect leader'
    if log:
        xlabel += ' [ms, $\log_{10}$ scale]'
    else:
        xlabel += ' [ms]'


    axes.set_xlabel(xlabel,fontsize=9)
    axes.set_ylabel('Cumulative percent',fontsize=9)
    if "diago" in name:
      axes.set_title('\\textbf{Original}~(Ongaro and Ousterhout)',fontsize=9)
    elif not("combo" in name) and not ("expo" in name) and not ("fixed" in name):
      axes.set_title('\\textbf{Reproduction}',fontsize=9)

    # ticks & axes
    if (log):
        axes.set_xscale("log")
        x_marked = [75, 150, 300, 1000, 3000, 10000]
        axes.set_xticks(x_marked)
        axes.set_xticklabels(x_marked)
        axes.set_xlim([75,x_max])
    else:
        x_marked = range(0, 401, 50)
        axes.set_xticks(x_marked)
        axes.set_xticklabels([str(x) for x in x_marked])
        axes.set_xlim([x_min,x_max])

    y_marked = [0,20,40,60,80,100]
    axes.set_yticks(y_marked)
    axes.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

    axes.legend(graph_a_labels,loc=4,frameon=False,handlelength=2.5)
    fig.show()
    fig_to_file(fig,'graph_b_'+name,'pdf')
