
# coding: utf-8

# In[ ]:
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import numpy as np
import csv


# In[ ]:

def fig_to_file(fig, filename, ext):
    fig.savefig("graphs/%s.%s" % (filename, ext), format=ext, bbox_inches='tight')


# In[ ]:

def set_paper_rcs():
  fig_font = {'family':'sans-serif','sans-serif':['Helvetica'],
               'serif':['Helvetica'],'size':9}
  rc('font',**fig_font)
  rc('text', usetex=True)
  rc('figure', figsize=(3.33,2.22))
#  rc('figure.subplot', left=0.10, top=0.90, bottom=0.12, right=0.95)
  rc('axes', linewidth=0.5)
  rc('lines', linewidth=0.5)
set_paper_rcs()


# In[ ]:

figs = ['org','expo','combo','fixed']
graph_a = ['12-24','25-50','50-100','100-200','150-300']
graph_b = ['150-151','150-155','150-175','150-200','150-300']


# In[ ]:

#read data in
data_dict = {}
for figure in figs:
    data_dict[figure] = {}
    for line in graph_a + graph_b:
        file = open('raw/'+figure+'/'+line+'results.log')
        file_reader = csv.reader(file,delimiter=',')
        data_dict[figure][line] = []
        for point in file_reader:
            data_dict[figure][line].append(float(point[0]))
        data_dict[figure][line].sort()


# In[ ]:

# convert to ms floats
# flt_dict = {}
# for line in graph_a + graph_b:
#     flt_dict[line] = []
#     for point in data_dict[line]:
#         flt_dict[line].append(float(point))
#     flt_dict[line].sort()


# In[ ]:

y_axis = []
size = len(data_dict['org'][graph_a[0]])
for y in range (1,size+1):
    y_axis.append(y*100.0/size)


# In[ ]:

def plot_graph_a (data_x,data_y,name):
    fig = plt.figure()

    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

    for line in graph_a:
        if (len(data_x[line]) != len(data_y)):
            print (line)
        axes.plot(data_x[line],data_y)

    # labels
    axes.set_xlabel('Time to elect leader (ms)')
    axes.set_ylabel('Cummulative percent')
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
    axes.set_ylabel('Cummulative percent')
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


# In[ ]:

# collect pkt data
pkt_data = {} 
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
width = 0.2
for line in graph_a + graph_b:
    pkt_data[line] = {}
    for figure in figs:
        pkt_data[line][figure] = []
        file = open('raw/'+figure+'/'+line+'results.log')
        file_reader = csv.reader(file,delimiter=',')
        for point in file_reader:
            pkt_data[line][figure].append(int(point[1]))
        print (line + figure + str(np.mean(pkt_data[line][figure])))

# plot hist
hist_data = pkt_data['150-200']['org']
print (hist_data)
min = np.amin(hist_data)
max = np.amax(hist_data)
ax.hist(hist_data, max-min,
        range=[min,max], normed=True,histtype='bar',linewidth=0.5)
ax.set_xlabel('No. of packets to elect leader')
ax.set_ylabel('Probability')
fig.show()
fig_to_file(fig,'pkt_histogram','pdf')


# In[ ]:

plot_graph_a(data_dict['org'],y_axis,'org')
plot_graph_b(data_dict['org'],y_axis,'org')

plot_graph_b(data_dict['fixed'],y_axis,'fixed',400,False,'(a) ')
plot_graph_b(data_dict['expo'],y_axis,'expo',letter='(b) ')
plot_graph_b(data_dict['combo'],y_axis,'combo',400,False,'(c) ')


# In[ ]:

# initialisation
diago_percent = {}
diago_time = {}
for line in graph_a + graph_b:
    diago_percent[line] = []
    diago_time[line] = []
# reading in diago's results
file = open('raw/usableFormat.csv')
file_reader = csv.reader(file,delimiter=',')
next(file_reader, None)
for row in file_reader:
    if (row[0] != '150-150'):
        diago_percent[row[0]].append(100*float(row[1]))
        diago_time[row[0]].append(row[2])


# In[ ]:

plot_graph_a(diago_time,diago_percent['150-300'],'diago')
plot_graph_b(diago_time,diago_percent['150-300'],'diago')


# In[ ]:

def update_paper_figs():
    import os
    os.system('cp graphs/* ~/dissertation/sig-ops/graphs')


# In[ ]:

update_paper_figs()


# In[ ]:

# from collections import Counter
# pkt_data = {} 
# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
# width = 0.2
# for figure in figs:
#     pkt_data[figure] = []
#     line = '150-175'
#     file = open('raw/'+figure+'/'+line+'results.log')
#     file_reader = csv.reader(file,delimiter=',')
#     for point in file_reader:
#         pkt_data[figure].append(int(point[1]))
#     print (figure + str(np.mean(pkt_data[figure])))
# samples = np.array(list(pkt_data.values()))
# print (samples)
# ax.hist( [pkt_data['org'],pkt_data['fixed']], 20,
#         range=[np.amin(samples),np.amax(samples)], normed=False,
#         label=['orginal','combo'],histtype='bar')
# ax.set_xlabel( figure )
# ax.set_ylabel( 'Packets' )
# fig.show()
# print(Counter(pkt_data['org']))
fig_to_file(fig,'testing','pdf')


# In[ ]:

data_dict = {}
for numb in [1,3,5]:
    numb_str = str(numb)
    data_dict[numb] = {}
    for line in graph_a + graph_b:
        file = open('raw/ine-'+numb_str+'/'+line+'results.log')
        file_reader = csv.reader(file,delimiter=',')
        data_dict[numb][line] = []
        for point in file_reader:
            data_dict[numb][line].append(float(point[0]))
        data_dict[numb][line].sort()
    plot_graph_b(data_dict[numb],y_axis,numb_str,400,False,numb_str)


# In[ ]:




# In[ ]:



