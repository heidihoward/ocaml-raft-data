from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.pylab as pyl
import numpy as np
import csv
from utils import *
from plotting_funct import *


set_paper_rcs()


# setu[ graphs]



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


y_axis = []
# assuming all figs have same number of iterations
size = len(data_dict['org'][graph_a[0]])
for y in range (1,size+1):
    y_axis.append(y*100.0/size)

# get figure to quote in the text
# print (size)
# print (data_dict['org']['150-155'].pop(int(size*0.95)))
# print (data_dict['fixed']['150-155'].pop(int(size*0.95)))

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
        # print (line + figure + str(np.mean(pkt_data[line][figure])))

# plot hist
hist_data = pkt_data['150-200']['org']
# print (hist_data)
min = np.amin(hist_data)
max = np.amax(hist_data)
ax.hist(hist_data, max-min,
        range=[min,max], normed=True,histtype='bar',linewidth=0.5)
ax.set_xlabel('Number of packets to elect leader')
ax.set_ylabel('Probability')

eights = [8,16,24,32,40,48,56,64]
ax.set_xticks(eights)
ax.set_xticklabels([str(x) for x in eights])
ax.set_yticks(np.arange(0.0, 0.36, 0.05))
ax.set_yticklabels([str(x)+"\%%" for x in range(0, 36, 5)])


fig.show()
fig_to_file(fig,'pkt_histogram','pdf')


plot_graph_a(data_dict['org'],y_axis,'org')
plot_graph_b(data_dict['org'],y_axis,'org')

plot_graph_b(data_dict['fixed'],y_axis,'fixed',75,400,False,'(a) ')
plot_graph_b(data_dict['expo'],y_axis,'expo',75,400,False,'(b) ')
plot_graph_b(data_dict['combo'],y_axis,'combo',75,400,False,'(c) ')



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



plot_graph_a(diago_time,diago_percent['150-300'],'diago')
plot_graph_b(diago_time,diago_percent['150-300'],'diago')



update_paper_figs('~/dissertation/sig-ops/graphs')



# data_dict = {}
# for numb in [1,3,5]:
#     numb_str = str(numb)
#     data_dict[numb] = {}
#     for line in graph_a + graph_b:
#         file = open('raw/ine-'+numb_str+'/'+line+'results.log')
#         file_reader = csv.reader(file,delimiter=',')
#         data_dict[numb][line] = []
#         for point in file_reader:
#             data_dict[numb][line].append(float(point[0]))
#         data_dict[numb][line].sort()
#     plot_graph_b(data_dict[numb],y_axis,numb_str,400,False,numb_str)

