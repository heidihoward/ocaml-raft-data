from matplotlib import rc

def set_paper_rcs():
  fig_font = {'family':'sans-serif','sans-serif':['Helvetica'],
               'serif':['Helvetica'],'size':9}
  rc('font',**fig_font)
  rc('legend',fontsize=9, handletextpad=0.5)
  rc('text', usetex=True)
  rc('figure', figsize=(3.33,2.22))
#  rc('figure.subplot', left=0.10, top=0.90, bottom=0.12, right=0.95)
  rc('axes', linewidth=0.5, color_cycle= ['#496ee2', '#8e053b', 'm', '#ef9708', 'g', 'c'])
  rc('lines', linewidth=0.5)

def fig_to_file(fig, filename, ext):
    fig.savefig("graphs/%s.%s" % (filename, ext), format=ext, bbox_inches='tight')

def update_paper_figs(paper_location):
    import os
    os.system('cp graphs/* ' + paper_location)
