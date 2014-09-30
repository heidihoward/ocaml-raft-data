from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import numpy as np
import csv
from utils import *

figs = ['org','expo','combo','fixed']
graph_a = ['12-24','25-50','50-100','100-200','150-300']
graph_b = ['150-151','150-155','150-175','150-200','150-300']

def plot_graph_a (data_x,data_y,name):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

    for line in graph_a:
        if (len(data_x[line]) != len(data_y)):
            print (line)
        axes.plot(data_x[line],data_y)

    # labels
    axes.set_xlabel('Time to elect leader (ms)')
    axes.set_ylabel('Cumulative percent')
    axes.set_title('Time taken to elect leader',fontsize=9)

    # ticks & axes

    y_marked = [0,20,40,60,80,100]
    axes.set_yticks(y_marked)
    axes.set_yticklabels(['0%','20%','40%','60%','80%','100%'])
    axes.set_xlim([0,400])

    axes.legend(graph_a,loc=4)
    fig.show()
    fig_to_file(fig,'graph_a_'+name,'pdf')


# In[ ]:

def plot_graph_b(data_x,data_y,name,x_max=10000,log=True,letter=''):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

    for line in graph_b:
        if (len(data_x[line]) != len(data_y)):
            print (line)
            print (len(y_axis))
        axes.plot(data_x[line],data_y)

    # labels
    axes.set_xlabel('Time to elect leader (ms)')
    axes.set_ylabel('Cumulative percent')
    axes.set_title(letter+'Time taken to elect leader',fontsize=9)

    # ticks & axes
    if (log):
        axes.set_xscale("log")
        x_marked = [75, 150, 300, 1000, 3000, 10000]
        axes.set_xticks(x_marked)
        axes.set_xticklabels(x_marked)
    axes.set_xlim([75,x_max])

    y_marked = [0,20,40,60,80,100]
    axes.set_yticks(y_marked)
    axes.set_yticklabels(['0%','20%','40%','60%','80%','100%'])

    axes.legend(graph_b,loc=4)
    fig.show()
    fig_to_file(fig,'graph_b_'+name,'pdf')