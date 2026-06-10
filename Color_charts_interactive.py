import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Button, TextBox, CheckButtons
from matplotlib.widgets import RadioButtons
import statistics
import math

plt.ion()
import os
import pandas as pd

# These lines supress warnings
import warnings
warnings.filterwarnings('ignore')

# 3/29/26: GWC changes name of input Plot Master csv file to PlotMaster-GWC.csv
# Also installed 'seaborn' in environment MakePlots
path= '.'
catalog_name= os.path.join(path, 'PlotMaster-10fluxes-GWC.csv') #Crossmatch catalog csv name
save_name= os.path.join(path, 'FigureX.png') 

####################
# Define Functions #
####################
#Multiply used functions
def close(event):
    global done
    done = True
    plt.close()

#Functions for step 1:
def make_histograms(event):
    global plttype
    plt.close()
    plttype = 3
    return plttype

def make_histograms_color(event):
    global plttype
    plt.close()
    plttype = 1
    return plttype

def make_histograms_physical(event):
    global plttype
    plt.close()
    plttype = 4
    return plttype
    
def make_colorcolor(event):
    global plttype
    plt.close()
    plttype = 2
    return plttype

def select_color_physical():
    global plttype

    plttype = 0

    secondpage = plt.figure(figsize= (5,3))
    secondpage.suptitle('Select Histogram Type', fontsize = 20, y = .9)

    hist_axes_color = plt.axes([.15,.55,.7,.25])
    histbutton_color = Button(hist_axes_color, 'Color Histogram', )
    histbutton_color.on_clicked(make_histograms_color)

    hist_axes_physical = plt.axes([.15,.25,.7,.25])
    histbutton_physical = Button(hist_axes_physical, 'Physical Property Histogram', )
    histbutton_physical.on_clicked(make_histograms_physical)
    plt.show()
    while plttype==0:
        plt.pause(0.1)
    plt.close()

    return plttype
#Functions for Step 2:
def select_properties(plttype):
    global done
    if plttype == 1:
        # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
        colorsel = plt.figure(figsize= (10,10))
        # colorsel.suptitle('Select Color', fontsize = 15)
        colorsel.suptitle('Select Color For Histogram', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
        axes = plt.axes([.3,.3,.4,.6])
        label_props={'fontsize':[15]*len(coloroptions)},
                                        # radio_props={'s':[64]*len(coloroptions)})
        radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[10]*len(coloroptions)},
                                        radio_props={'s':[64]*len(coloroptions)})
        radio_hist.on_clicked(histcolorfunc)

        axes2 = plt.axes([.2,.15,.7,.1])
        contbutton = Button(axes2, 'Continue')
        contbutton.on_clicked(close)
        plt.show()
        
        done = False
        while done==False:
            plt.pause(.1)
        return color
        
    if plttype == 2:
        global colorcolor
        # GWC - colorcolor needs to point to 1st entry in colordict.
        # colorcolor = [['F70','F24'],['F70','F24']]
        # Adjusting figsize, fontsize, axes to make room for more colors. 5/12/26
        colorcolor = [['F1100','F870'],['F1100','F870']]
        # colorsel = plt.figure(figsize= (6,4))
        colorsel = plt.figure(figsize= (6,10))
        # colorsel.suptitle('Select Colors', fontsize = 15)
        colorsel.suptitle('Select Colors', fontsize = 10)
        # axesx = plt.axes([.1,.3,.4,.5])
        axesx = plt.axes([.1,.3,.4,.6])
        # axesx.set_title('x-axis color',fontsize = 15, loc = 'left')
        axesx.set_title('x-axis color',fontsize = 10, loc = 'left')
        # radio_ccx= RadioButtons(axesx, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
        radio_ccx= RadioButtons(axesx, coloroptions, label_props={'fontsize':[10]*len(coloroptions)},
                                 radio_props={'s':[64]*len(coloroptions)})
        radio_ccx.on_clicked(colorfuncx)
        # axesy = plt.axes([.5,.3,.4,.5])
        axesy = plt.axes([.5,.3,.4,.6])
        # axesy.set_title('y-axis color', fontsize = 15, loc='left')
        axesy.set_title('y-axis color', fontsize = 10, loc='left')
        # radio_ccy= RadioButtons(axesy, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
        radio_ccy= RadioButtons(axesy, coloroptions, label_props={'fontsize':[10]*len(coloroptions)},
                                 radio_props={'s':[64]*len(coloroptions)})
        radio_ccy.on_clicked(colorfuncy)
        axes2 = plt.axes([.1,.18,.8,.1])
        contbutton = Button(axes2, 'Continue')
        contbutton.on_clicked(close)
        plt.show()
        done = False
        while done==False:
            plt.pause(.1)
        return colorcolor
    if plttype == 4:
        global physical
        global physeq
        physical = ['LRAT']
        physeq = r"Luminosity Ratio [$\log_{10}(L/L_{\mathrm{ssm}})$]"
        # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
        colorsel = plt.figure(figsize= (6,5))
        # colorsel.suptitle('Select Color', fontsize = 15)
        colorsel.suptitle('Select Physical Property For Histogram', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
        axes = plt.axes([.3,.3,.4,.6])
        label_props={'fontsize':[15]*len(physical_options)},
                                        # radio_props={'s':[64]*len(coloroptions)})
        radio_hist= RadioButtons(axes, physical_options, label_props={'fontsize':[10]*len(physical_options)},
                                        radio_props={'s':[64]*len(physical_options)})
        radio_hist.on_clicked(histphysicalfunc)

        axes2 = plt.axes([.2,.15,.6,.1])
        contbutton = Button(axes2, 'Continue')
        contbutton.on_clicked(close)
        plt.show()
        
        
        done = False
        while done==False:
            plt.pause(.1)
        return physical

# GWC adds 160 um on 5/8/26. Added all longer-wavelength fluxes on 5/12/26.
def histcolorfunc(label):
    global color
    colordict = {'1100/870': ['F1100','F870'], '1100/500': ['F1100','F500'], '1100/350': ['F1100','F350'],
                 '1100/250': ['F1100','F250'], '1100/160': ['F1100','F160'], '1100/70': ['F1100','F70'],
                 '1100/24': ['F1100','F24'], '1100/12': ['F1100','F12'], '1100/8': ['F1100','F8'],
                 '870/500': ['F870','F500'], '870/350': ['F870','F350'],
                 '870/250': ['F870','F250'], '870/160': ['F870','F160'], '870/70': ['F870','F70'],
                 '870/24': ['F870','F24'], '870/12': ['F870','F12'], '870/8': ['F870','F8'],
                 '500/350': ['F500','F350'],'500/250': ['F500','F250'], '500/160': ['F500','F160'], 
                 '500/70': ['F500','F70'],'500/24': ['F500','F24'], '500/12': ['F500','F12'], 
                 '500/8': ['F500','F8'], '350/250': ['F350','F250'], '350/160': ['F350','F160'], 
                 '350/70': ['F350','F70'],'350/24': ['F350','F24'], '350/12': ['F350','F12'], 
                 '350/8': ['F350','F8'], '250/160': ['F250','F160'], '250/70': ['F250','F70'], 
                 '250/24': ['F250','F24'], '250/12': ['F250','F12'], '250/8': ['F250','F8'],
                 '160/70': ['F160','F70'], '160/24': ['F160','F24'], '160/12': ['F160','F12'], 
                 '160/8': ['F160','F8'], '70/24': ['F70','F24'], '70/12': ['F70','F12'],
                 '70/8': ['F70','F8'],'24/12': ['F24','F12'],'24/8': ['F24','F8'],'12/8': ['F12','F8']}
    color = colordict[label]
    return color
def histphysicalfunc(label):
    global physical
    global physeq
    physicaldict = {"Luminosity Ratio": ['LRAT'], "Bolometric Temperature": ['TBOL'],
                    "Surface Density": ['SIGMA'],"Greybody Temperature": ['TEMP'],}
    physicalform = {"Luminosity Ratio": r"Luminosity Ratio [$\log_{10}(L/L_{\mathrm{ssm}})$]",
                    "Bolometric Temperature": r"Bolometric Temperature [$T_{\mathrm{bol}}/\mathrm{K}$]",
                    "Surface Density": r"Surface Density [$\log_{10}(\sum/\mathrm{g\,cm^{-3}})$]",
                    "Greybody Temperature": r"Greybody Temperature [$T_{\mathrm{g}}/\mathrm{K}$]"}
    physical = physicaldict[label]
    physeq = physicalform[label]
    return physical, physeq
def colorfuncx(label):
    global colorcolor
    colordict = {'1100/870': ['F1100','F870'], '1100/500': ['F1100','F500'], '1100/350': ['F1100','F350'],
                 '1100/250': ['F1100','F250'], '1100/160': ['F1100','F160'], '1100/70': ['F1100','F70'],
                 '1100/24': ['F1100','F24'], '1100/12': ['F1100','F12'], '1100/8': ['F1100','F8'],
                 '870/500': ['F870','F500'], '870/350': ['F870','F350'],
                 '870/250': ['F870','F250'], '870/160': ['F870','F160'], '870/70': ['F870','F70'],
                 '870/24': ['F870','F24'], '870/12': ['F870','F12'], '870/8': ['F870','F8'],
                 '500/350': ['F500','F350'],'500/250': ['F500','F250'], '500/160': ['F500','F160'], 
                 '500/70': ['F500','F70'],'500/24': ['F500','F24'], '500/12': ['F500','F12'], 
                 '500/8': ['F500','F8'], '350/250': ['F350','F250'], '350/160': ['F350','F160'], 
                 '350/70': ['F350','F70'],'350/24': ['F350','F24'], '350/12': ['F350','F12'], 
                 '350/8': ['F350','F8'], '250/160': ['F250','F160'], '250/70': ['F250','F70'], 
                 '250/24': ['F250','F24'], '250/12': ['F250','F12'], '250/8': ['F250','F8'],
                 '160/70': ['F160','F70'], '160/24': ['F160','F24'], '160/12': ['F160','F12'], 
                 '160/8': ['F160','F8'],'70/24': ['F70','F24'], '70/12': ['F70','F12'],
                 '70/8': ['F70','F8'],'24/12': ['F24','F12'],'24/8': ['F24','F8'],'12/8': ['F12','F8']}
    color = colordict[label]
    colorcolor[0]=color
    return colorcolor

def colorfuncy(label):
    global colorcolor
    colordict = {'1100/870': ['F1100','F870'], '1100/500': ['F1100','F500'], '1100/350': ['F1100','F350'],
                 '1100/250': ['F1100','F250'], '1100/160': ['F1100','F160'], '1100/70': ['F1100','F70'],
                 '1100/24': ['F1100','F24'], '1100/12': ['F1100','F12'], '1100/8': ['F1100','F8'],
                 '870/500': ['F870','F500'], '870/350': ['F870','F350'],
                 '870/250': ['F870','F250'], '870/160': ['F870','F160'], '870/70': ['F870','F70'],
                 '870/24': ['F870','F24'], '870/12': ['F870','F12'], '870/8': ['F870','F8'],
                 '500/350': ['F500','F350'],'500/250': ['F500','F250'], '500/160': ['F500','F160'], 
                 '500/70': ['F500','F70'],'500/24': ['F500','F24'], '500/12': ['F500','F12'], 
                 '500/8': ['F500','F8'], '350/250': ['F350','F250'], '350/160': ['F350','F160'], 
                 '350/70': ['F350','F70'],'350/24': ['F350','F24'], '350/12': ['F350','F12'], 
                 '350/8': ['F350','F8'], '250/160': ['F250','F160'], '250/70': ['F250','F70'], 
                 '250/24': ['F250','F24'], '250/12': ['F250','F12'], '250/8': ['F250','F8'],
                 '160/70': ['F160','F70'], '160/24': ['F160','F24'], '160/12': ['F160','F12'], 
                 '160/8': ['F160','F8'],'70/24': ['F70','F24'], '70/12': ['F70','F12'],
                 '70/8': ['F70','F8'],'24/12': ['F24','F12'],'24/8': ['F24','F8'],'12/8': ['F12','F8']}
    color = colordict[label]
    colorcolor[1]=color
    return colorcolor
#Functions For Step 3
def sortoptions():
    sortsel = plt.figure(figsize=(5,4))
    sortsel.suptitle('Sort Plots By', fontsize = 15)
    axes = plt.axes([.2,.7,.7,.2])
    radio_sort= RadioButtons(axes, sorttypes, label_props={'fontsize':[15]*2},
                             radio_props={'s':[64]*2})
    radio_sort.on_clicked(categoryselect)
    categoryselect(sorttypes[0])
    checked = [False]*len(categories)
    axes2 = plt.axes([.2,.05,.7,.2])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    global done
    done = False
    while not done:
        cataxes = plt.axes([.2,.25,.7,.4])
        catselect = CheckButtons(cataxes, categories, checked, 
                                 label_props={'fontsize':[15]*len(categories)})
        def marked(label):
            index= categories.index(label)
            checked[index] = not checked[index]
        catselect.on_clicked(marked)
        plt.pause(.1)
    plt.show()
    idx = sortlist.index(categories)
    sort = sorttypes[idx]
    catplotted = [x for x in categories if checked[categories.index(x)]==True]
    return sort, catplotted

def categoryselect(label):
    categorydict = {sorttypes[0]:sortlist[0], sorttypes[1]:sortlist[1]}
    global categories
    categories = categorydict[label]
    
#Functions for step 4
def entrynumber(entry):
    global cutoff
    cutoff = float(entry)
    return cutoff

def excludeoptions():
    excsel = plt.figure(figsize=(10,6))
    excsel.suptitle('Set Exclusion Parameters')
    startbox_axes = plt.axes([.1,.75,.4,.1])
    global cutoff
    cutoffentry = TextBox(startbox_axes, 'Set Cutoff', str(cutoff))
    cutoffentry.on_submit(entrynumber)
    axes0 = plt.axes([.1,.6,.4,.1])
    global clicked0
    clicked0 = [False]
    exsort0= CheckButtons(axes0, extype0, clicked0, label_props={'fontsize':[15]})
    exsort0.on_clicked(excategories0)
    axes1 = plt.axes([.5,.6,.4,.1])
    global clicked1
    clicked1 = [False]
    exsort1= CheckButtons(axes1, extype1, clicked1, label_props={'fontsize':[15]})
    exsort1.on_clicked(excategories1)
    axes2 = plt.axes([.1,.05,.8,.2])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    clickedcats0 = [False] * len(flagexlist)
    clickedcats1 = [False] * len(xmatexlist)
    global done
    done = False
    def marked0(label):
        index= flagexlist.index(label)
        clickedcats0[index] = not clickedcats0[index]
    def marked1(label):
        index= xmatexlist.index(label)
        clickedcats1[index] = not clickedcats1[index]
    while not done:
        if clicked0[0]==True:
            axes3 = plt.axes([.1,.25,.4,.35])
            exsortcat0 = CheckButtons(axes3, flagexlist, clickedcats0, label_props = 
                                      {'fontsize':[15]*len(flagexlist)})
            exsortcat0.on_clicked(marked0)
        else:
            axes3 = plt.axes([.1,.25,.4,.35])
            clickedcats0 = [False] * len(flagexlist)
            CheckButtons(axes3, [])
        if clicked1[0]==True:
            axes4 = plt.axes([.5,.25,.4,.35])
            exsortcat1 = CheckButtons(axes4, xmatexlist, clickedcats1, label_props = 
                                      {'fontsize':[15]*len(flagexlist)})
            exsortcat1.on_clicked(marked1)
        else:
            axes4 = plt.axes([.5,.25,.4,.35])
            clickedcats1 = [False] * len(xmatexlist)
            CheckButtons(axes4, [])
        plt.pause(.1)
    plt.show()
    catexc0 = [x for x in flagexlist if clickedcats0[flagexlist.index(x)]==True]
    catexc1 = [x for x in xmatexlist if clickedcats1[xmatexlist.index(x)]==True]
    return cutoff, [catexc0,catexc1]

def excludeoptionsphys():
    excsel = plt.figure(figsize=(4,6))
    excsel.suptitle('Set Exclusion Parameters')
    startbox_axes = plt.axes([.2,.8,.4,.1])
    global cutoff
    cutoffentry = TextBox(startbox_axes, 'Set Cutoff', str(cutoff))
    cutoffentry.on_submit(entrynumber)
    axes0 = plt.axes([.2,.2,.6,.5])
    axes0.set_title("By Flag", fontsize = 15)
    global clicked0
    clicked0 = [False] * len(flagexlist)
    exsort0= CheckButtons(axes0, flagexlist, clicked0, label_props={'fontsize':[10]})
    exsort0.on_clicked(excategories2)
    axes2 = plt.axes([.25,.075,.5,.1])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    global done
    done = False

    while not done:
        plt.pause(.1)
    plt.show()
    return cutoff, clicked0

def excategories0(label):
    global clicked0
    clicked0[0]= not clicked0[0]
def excategories1(label):
    global clicked1
    clicked1[0]=not clicked1[0]
def excategories2(label):
    index = flagexlist.index(label)
    clicked0[index]=not clicked0[index]
        
# For Plotting
def get_binlen(n):
    log = np.log10(n)
    if log >=3:
        bins = math.floor(log)
    else:
        bins = math.ceil(log)
    return 10*(bins - 1) + 5

def get_dimensions(n):
    root = math.sqrt(n)
    x = math.ceil(root)
    y = math.ceil(n/x)
    dimensions = [x,y]
    return dimensions

def get_range(datacol):
    longest_list = max(datacol, key=len)
    mean = statistics.mean(longest_list)
    dev = np.std(longest_list)
    return [mean-4*dev, mean + 4*dev]

def get_rangecc(datacol):
    longest_list = max(datacol, key=len)
    mean = statistics.mean(longest_list)
    dev = np.std(longest_list)
    return [mean-6*dev, mean + 6*dev, dev]

######################
# Start Program Here #
######################

##############################################################
#Selection Steps: Collect user input and store into variables#
##############################################################

#Step 1: Choose to generate either a histogram or color-color plot
startup = plt.figure(figsize= (5,3))
startup.suptitle('Select Plot Type', fontsize = 20, y = .9)
hist_axes = plt.axes([.15,.45,.7,.25])
histbutton = Button(hist_axes, 'Histogram', )
histbutton.on_clicked(make_histograms)
cc_axes = plt.axes([.15,.15,.7,.25])
ccbutton = Button(cc_axes, 'Color-Color Plot')
ccbutton.on_clicked(make_colorcolor)

plttype= 0
plt.show()
while plttype==0:
    plt.pause(0.1)

plt.close()

if plttype == 3:
    select_color_physical()

# Step 2: Choose what color(s) you want to plot
coloroptions = ['1100/870','1100/500','1100/350','1100/250','1100/160','1100/70','1100/24',
                '1100/12','1100/8','870/500','870/350','870/250','870/160','870/70','870/24',
                '870/12','870/8','500/350','500/250','500/160','500/70','500/24','500/12','500/8',
                '350/250','350/160','350/70','350/24','350/12','350/8','250/160','250/70',
                '250/24','250/12','250/8',
                '160/70','160/24','160/12','160/8','70/24','70/12','70/8','24/12','24/8','12/8']

physical_options = ["Luminosity Ratio", "Bolometric Temperature","Surface Density","Greybody Temperature"]
# GWC - This assignment needs to point to the first entry in colordict. 5/12/26
# color = ['F70','F24']
color = ['F1100','F870']
color = select_properties(plttype)
    #Step 3: Select whether data will be sorted by flag or crossmatch, then choose
    #        what categories to plot
sorttypes = ['CrossMatch', 'Flag']
sortlist = [['All Sources', 'RMS', 'WISE C,G,K', 'WISE Q', 'CORNISH', 'No Association'],
                ['All Sources', 'Multiple Sources', 'Very Circular', 
                'Not Multiple Sources', 'Not Very Circular', 'Neither']]
sort = sortoptions()
if plttype != 4 :
    #Step 4: Select parameters used to exclude data
    extype0 = ['By Flag']
    extype1 = ['By Crossmatch']
    flagexlist = ['No Obvious Source', 'Poor Confidence', 'Multiple Sources', 
                'Very Circular']
    xmatexlist = ['RMS', 'WISE Q', 'WISE C,G,K', 'CORNISH', 'No Association']
    cutoff = .5

    exclusions = excludeoptions()

    ########################
    # Create Selected Plot #
    ########################
    colordict = {'All Sources': 'green', 'RMS': 'red', 'WISE C,G,K':'orange', 'WISE Q': 'blue',
                'CORNISH':'purple', 'No Association':'gray', 'Multiple Sources': 'red', 'Very Circular':'orange', 
                'Not Multiple Sources': 'blue','Not Very Circular':'purple', 'Neither':'gray'}
    ccolordict = {'All Sources': 'Greens', 'RMS': 'Reds', 'WISE C,G,K':'Oranges', 'WISE Q': 'Blues',
                'CORNISH':'Purples', 'No Association':'Grays', 'Multiple Sources': 'Reds', 'Very Circular':'Oranges', 
                'Not Multiple Sources': 'Blues','Not Very Circular':'Purples', 'Neither':'Grays'}
if plttype == 4 :
    #Step 4: Select parameters used to exclude data
    extype0 = ['By Flag']
    flagexlist = ['No Obvious Source', 'Poor Confidence', 'Multiple Sources', 
                'Very Circular']
    cutoff = 3.5

    exclusions = excludeoptionsphys()

    ########################
    # Create Selected Plot #
    ########################
    colordict = {'All Sources': 'green', 'RMS': 'red', 'WISE C,G,K':'orange', 'WISE Q': 'blue',
                'CORNISH':'purple', 'No Association':'gray', 'Multiple Sources': 'red', 'Very Circular':'orange', 
                'Not Multiple Sources': 'blue','Not Very Circular':'purple', 'Neither':'gray'}
    ccolordict = {'All Sources': 'Greens', 'RMS': 'Reds', 'WISE C,G,K':'Oranges', 'WISE Q': 'Blues',
                'CORNISH':'Purples', 'No Association':'Grays', 'Multiple Sources': 'Reds', 'Very Circular':'Oranges', 
                'Not Multiple Sources': 'Blues','Not Very Circular':'Purples', 'Neither':'Grays'}
if plttype == 1:
    #Put together a relevant dataframe
    sortheaders = [x.replace('Not ','') for x in sort[1] if x != 'All Sources' and x!= 'Neither']
    print(sortheaders)
    if 'Neither' in sort[1]:
        sortheaders.append('Multiple Sources')
        sortheaders.append('Very Circular')
    sortheaders = list(set(sortheaders))
    exclusionheaders = exclusions[1][0]+exclusions[1][1]
    if 'No Obvious Source' in exclusionheaders:
        exclusionheaders.remove('No Obvious Source')
        exclusionheaders += ['No Obvious Source ' + color[0].replace('F',''), 
                             'No Obvious Source ' + color[1].replace('F','')]
    if 'Poor Confidence' in exclusionheaders:
        exclusionheaders.remove('Poor Confidence')
        exclusionheaders += ['Poor Confidence ' + color[0].replace('F',''), 
                             'Poor Confidence ' + color[1].replace('F','')]
    xmatdata = pd.read_csv(catalog_name, usecols=['YB']+color+['u_'+color[0],'u_'+color[1]]+
                           ['e_'+color[0],'e_'+color[1]]+ sortheaders+exclusionheaders)
    # Remove Rows based on exclusion parameters
    # Changing range from 6176 to 3945 for Herschel-matched objects. GWC 5/8/26.
    excludeidx = []
    for i in range(3945):
        for j in range(len(exclusionheaders)):
            if int(xmatdata[exclusionheaders[j]][i])== 1:
                excludeidx += [i]
        FEvals = [float(xmatdata['e_'+color[0]][i]), float(xmatdata['e_'+color[1]][i])]
        if exclusions[0]<max(FEvals) or min(FEvals)<0:
            excludeidx += [i]
    excludeidx = list(set(excludeidx))
    # Sort into lists based on sorting categories
    categorized = []
    uncategorized = []
    for j in sort[1]:
        cat = []
        uncat = []
        for i in range(3945):
            colornum = float(xmatdata[color[0]][i])
            colornums = float(xmatdata['u_' + color[0]][i])
            colorden = float(xmatdata[color[1]][i])
            colordens = float(xmatdata['u_' + color[1]][i])
            entry = np.log10(colornum/colorden)
            unc2 = ((colornums**2)/(colornum*np.log(10))**2)+((colordens**2)/(colorden*np.log(10))**2)
            unentry = np.sqrt(unc2)
            if np.isnan(entry) == False and np.isnan(unentry) == False and i not in excludeidx:
                if j =='All Sources':
                    cat.append(entry)
                    uncat.append(unentry)
                elif j=='Neither':
                    if xmatdata['Multiple Sources'][i] == 0 and xmatdata['Very Circular'][i]==0:
                        cat.append(entry)
                        uncat.append(unentry)
                elif 'Not ' in j:
                    if xmatdata[j.replace('Not ','')][i]==0:
                        cat.append(entry)
                        uncat.append(unentry)
                else:
                    if xmatdata[j][i]==1:
                        cat.append(entry)
                        uncat.append(unentry)
        categorized.append(cat)
        uncategorized.append(uncat)
    #Make Histograms (Finally)
    dim = get_dimensions(len(categorized))
    colorname = color[0] + '/' + color[1]
    fig= plt.figure(figsize=(10*dim[0],10*dim[1]))
    fig.canvas.header_visible= False
    fig.suptitle(r'$log_{10}$'+f'({colorname}) Color Histograms', fontsize = 25)
    plt.axis('off')
    plt.text(.5, -.075, r'$log_{10}$'+f'({colorname})', fontsize=28, ha='center')
    plt.text(-.075, 0.5, 'Number', fontsize=28, rotation='vertical', va='center')
    plt.text(.5,1.075,'Cutoff: '+str(exclusions[0]), fontsize = 20, ha='center')
    datarng = get_range(categorized)
    for i in range(len(sort[1])):
        title=sort[1][i]
        data= categorized[i]
        undata = uncategorized[i]
        uncertainty = np.mean(undata)
        minifig= plt.subplot(dim[1],dim[0],i+1)
        plt.title(title, fontsize= 28)
        n= len(data)
        avecolor= round(statistics.mean(data),2)
        stdevcolor = round(np.std(data),3)
        binlen = get_binlen(n)
        cnts, bns, ptchs = plt.hist(data, facecolor=colordict[title], bins= binlen, range=(datarng))
        minifig.tick_params(labelsize=20)
        y = max(cnts)
        #Average lines for F12/F8 colors, will only plot if those colors are selected
        if colorname == 'F12/F8':
            HIIline= minifig.axvline(x=-0.09, color='black', linestyle='-.', label= 'HII Region Average')
            PAVEline= minifig.axvline(x=-0.43, color='black', linestyle='--', label= 'Pilot Region Average')
        #Other formatting things
        FAVEline= plt.axvline(x=avecolor, color='black', label= title + ' Average')
        minifig.text(datarng[0], .95 *y,'N=' + str(n), fontsize=28)
        minifig.text(datarng[0],.85*y,r'$\bar{x} =$' + str(round(avecolor,2)), fontsize=28)
        minifig.text(datarng[0],.75*y,r'$s =$' + str(round(stdevcolor,3)), fontsize=28)
        minifig.errorbar(datarng[0]+ uncertainty,.65*y,xerr=uncertainty, yerr=None, capsize=10, color='k')
        minifig.vlines(datarng[0]+uncertainty, .61*y, .69*y, colors='k')
        print('Uncertainty ' + sort[1][i] + ': ' + str(uncertainty))
    plt.ioff()
    plt.show()


if plttype == 4:
    data_hcsc = pd.read_csv("MRT-hcsc.txt", sep=r"\s+", skiprows=27, usecols=physical + ["ID"] + ["e_" + physical[0]])
    sortheaders = [x.replace('Not ','') for x in sort[1] if x != 'All Sources' and x!= 'Neither']
    xmatdata = pd.read_csv("PlotMaster-10fluxes-GWC.csv", usecols=["YB"]+sortheaders)
    merged = pd.merge(data_hcsc, xmatdata, left_on="ID", right_on="YB", how="inner")
    print("Before exclusions:", len(merged))
    print("Cutoff:", exclusions[0])

    unc = np.sqrt(merged["e_"+physical[0]])
    print("Min uncertainty:", np.nanmin(unc))
    print("Max uncertainty:", np.nanmax(unc))
    print("Median uncertainty:", np.nanmedian(unc))
    excludeidx= []
    for i in range(len(merged)):
        for j in range(len(flagexlist)):
            if exclusions[1][j]:
                flag = flagexlist[j]
                if flag in merged.columns and merged[flag].iloc[i] == 1:
                    excludeidx.append(i)
        uncertainty = np.sqrt(merged["e_"+physical[0]].iloc[i])
        if uncertainty > exclusions[0] or uncertainty < 0:
            excludeidx.append(i)
    excludeidx = list(set(excludeidx))
    merged = merged.drop(index=excludeidx).reset_index(drop=True)
    if 'Neither' in sort[1]:
        sortheaders.append('Multiple Sources')
        sortheaders.append('Very Circular')
    #Put together a relevant dataframe
    physical_data = merged[physical[0]]
    if physical[0] == 'LRAT' or physical[0] == 'SIGMA':
        log_physical_data = np.log10(physical_data)
        log_physical_data_tot = np.log10(physical_data).tolist()
    else:
        log_physical_data = physical_data
        log_physical_data_tot = physical_data.tolist()
    flag_data = xmatdata.loc[(data_hcsc["ID"] == xmatdata["YB"])]
    physun = merged['e_' + physical[0]]
    unentry_list = np.sqrt(physun)
    phys_categorized = []
    phys_ercategorized =[]
    for category in sort[1]:
        cat = []
        ercat = []
        for i in range(len(merged)):
            value = log_physical_data.iloc[i]
            unentry = unentry_list.iloc[i]
            if np.isnan(value) == False and np.isnan(unentry) == False:
                if np.isnan(value):
                    continue
                if category == "All Sources":
                    cat.append(value)
                    ercat.append(unentry)
                elif category=='Neither':
                    if merged['Multiple Sources'].iloc[i] == 0 and merged['Very Circular'].iloc[i]==0:
                        cat.append(value)
                        ercat.append(unentry)
                elif 'Not ' in category:
                    if merged[category.replace('Not ','')].iloc[i]==0:
                        cat.append(value)
                        ercat.append(unentry)
                else:
                    if merged[category].iloc[i]==1:
                        cat.append(value)
                        ercat.append(unentry)
        phys_categorized.append(cat)
        phys_ercategorized.append(ercat)
    
    dim = get_dimensions(len(phys_categorized))
    fig= plt.figure(figsize=(8*dim[0],8*dim[1]))
    fig.subplots_adjust(top=0.81)
    fig.canvas.header_visible= False
    fig.suptitle(f'{physeq} Histograms\nCutoff:{str(exclusions[0])}', fontsize = 25)
    fig.patch.set_facecolor("White")
    fig.text(.5, .02,f'{physeq}', fontsize=28, ha='center')
    fig.text(.02, 0.5, 'Number', fontsize=28, rotation='vertical', va='center')
    maxval = max(log_physical_data_tot)
    minval = min(log_physical_data_tot)
    datarng = (minval, maxval)
    datarng1 = get_range(phys_categorized)
    for i in range(len(sort[1])):
        title = sort[1][i]
        data = phys_categorized[i]
        undata = phys_ercategorized[i]
        uncertainty = np.mean(undata)
        minifig= plt.subplot(dim[1],dim[0],i+1)
        minifig1= plt.subplot(dim[1],dim[0],i+1)
        plt.title(title, fontsize= 28)
        n = len(data)
        avephys= round(statistics.mean(data),2)
        stdevphys= round(np.std(data),3)
        binlen = get_binlen(n)
        plt.hist(log_physical_data, bins= binlen, range=(datarng))
        cnts, bns, ptchs = plt.hist(data, bins= binlen, range=(datarng1))
        minifig.set_xlim(datarng)
        minifig.tick_params(labelsize=20)
        y = max(cnts)
        #Average lines for F12/F8 colors, will only plot if those colors are selected
        #Other formatting things
        FAVEline= plt.axvline(x=avephys, color='black', label= title + ' Average')
        minifig.text(.02,.93,'N=' + str(n), fontsize=28, transform = minifig.transAxes)
        minifig.text(.02,.87,r'$\bar{x} =$' + str(round(avephys,2)), fontsize=28, transform = minifig.transAxes)
        minifig.text(.02,.81,r'$s =$' + str(round(stdevphys,3)), fontsize=28, transform = minifig.transAxes)
        minifig.errorbar(datarng1[0]+ uncertainty,.65*y,xerr=uncertainty, yerr=None, capsize=10, color='k')
        minifig.vlines(datarng1[0]+uncertainty, .61*y, .69*y, colors='k')
    plt.ioff()
    plt.show()


elif plttype == 2:
    #Put together a relevant dataframe
    colorx = color[0]
    colory = color[1]
    datatitles = sort[1]
    sortheaders = [x.replace('Not ','') for x in datatitles if x != 'All Sources' and x!= 'Neither']
    if 'Neither' in datatitles:
        sortheaders.append('Multiple Sources')
        sortheaders.append('Very Circular')
    sortheaders = list(set(sortheaders))
    exclusionheaders = exclusions[1][0]+exclusions[1][1]
    if 'No Obvious Source' in exclusionheaders:
        exclusionheaders.remove('No Obvious Source')
        exclusionheaders += ['No Obvious Source ' + colorx[0].replace('F',''), 
                             'No Obvious Source ' + colorx[1].replace('F',''),
                             'No Obvious Source ' + colory[0].replace('F',''),
                             'No Obvious Source ' + colory[1].replace('F','')]
    if 'Poor Confidence' in exclusionheaders:
        exclusionheaders.remove('Poor Confidence')
        exclusionheaders += ['Poor Confidence ' + colorx[0].replace('F',''), 
                             'Poor Confidence ' + colorx[1].replace('F',''),
                             'Poor Confidence ' + colory[0].replace('F',''),
                             'Poor Confidence ' + colory[1].replace('F','')]
    xmatdata = pd.read_csv(catalog_name, usecols=['YB']+colorx+['u_'+colorx[0],'u_'+colorx[1]]+
                           ['e_'+colorx[0],'e_'+colorx[1]]+ colory+['u_'+colory[0],'u_'+colory[1]]+
                           ['e_'+colory[0],'e_'+colory[1]]+sortheaders+exclusionheaders)
    
    # Remove Rows based on exclusion parameters
    excludeidx = []
    for i in range(3945):
        for j in range(len(exclusionheaders)):
            if int(xmatdata[exclusionheaders[j]][i])== 1:
                excludeidx += [i]
        cutoff = exclusions[0]
        FEvals = []
        for k in colorx+colory:
            FEvals.append(float(xmatdata['e_'+k][i]))
        if cutoff<max(FEvals) or min(FEvals)<0:
            excludeidx += [i]
    excludeidx = list(set(excludeidx))
    
    # Sort into lists based on sorting categories
    categorizedx = []
    categorizedy = []
    uncategorizedx = []
    uncategorizedy = []
    for j in sort[1]:
        catx = []
        caty = []
        uncatx = []
        uncaty = []
        for i in range(3945):
            colornumx = float(xmatdata[colorx[0]][i])
            colornumsx = float(xmatdata['u_' + colorx[0]][i])
            colordenx = float(xmatdata[colorx[1]][i])
            colordensx = float(xmatdata['u_' + colorx[1]][i])
            entryx = np.log10(colornumx/colordenx)
            unc2x = ((colornumsx**2)/(colornumx*np.log(10))**2)+((colordensx**2)/(colordenx*np.log(10))**2)
            unentryx = np.sqrt(unc2x)
            colornumy = float(xmatdata[colory[0]][i])
            colornumsy = float(xmatdata['u_' + colory[0]][i])
            colordeny = float(xmatdata[colory[1]][i])
            colordensy = float(xmatdata['u_' + colory[1]][i])
            entryy = np.log10(colornumy/colordeny)
            unc2y = ((colornumsy**2)/(colornumy*np.log(10))**2)+((colordensy**2)/(colordeny*np.log(10))**2)
            unentryy = np.sqrt(unc2y)
            if i not in excludeidx and not np.isnan(entryx) and not np.isnan(entryy) and not np.isnan(unentryx) and not np.isnan(unentryy):
                if j =='All Sources':
                    catx.append(entryx)
                    caty.append(entryy)
                    uncatx.append(unentryx)
                    uncaty.append(unentryy)
                elif j=='Neither':
                    if xmatdata['Multiple Sources'][i] == 0 and xmatdata['Very Circular'][i]==0:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
                elif 'Not ' in j:
                    if xmatdata[j.replace('Not ','')][i]==0:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
                else:
                    if xmatdata[j][i]==1:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
        categorizedx.append(catx)
        categorizedy.append(caty)
        uncategorizedx.append(uncatx)
        uncategorizedy.append(uncaty)
    dim = get_dimensions(len(categorizedx))
    catlabel = []
    colordatx = []
    colordaty = []
    for i in range(len(categorizedx)):
        for j in range(len(categorizedx[i])):
            catlabel.append(datatitles[i])
        colordatx = colordatx + categorizedx[i]
        colordaty = colordaty + categorizedy[i]
    dataframe = {'xcoor': colordatx, 'ycoor':colordaty, 'Type': catlabel}
    df = pd.DataFrame(dataframe)
    print('This is where we make a color-color plot :3')
    fig= plt.figure(figsize=(8*dim[0],8*dim[1]))
    fig.canvas.header_visible= False
    fig.suptitle(r'$log_{10}$'+f'({colory[0]}/{colory[1]}) v. '+r'$log_{10}$'+f'({colorx[0]}/{colorx[1]})  Color-Color Density', fontsize=20, y=.98)
    plt.axis('off')
    fig.subplots_adjust(left=.1, right=.95, top=.9, bottom=.1)
    plt.text(.5, .02, r'$log_{10}'+f'({colorx[0]}/{colorx[1]})$', fontsize=28, ha='center', transform=fig.transFigure)
    plt.text(.015, .5, r'$log_{10}'+f'({colory[0]}/{colory[1]})$', fontsize=28, rotation='vertical', va='center', transform=fig.transFigure)
    plt.text(.5, 1.075,'Cutoff: '+str(cutoff), fontsize = 20, ha='center', transform=fig.transFigure)
    rangex = get_rangecc(categorizedx)
    rangey = get_rangecc(categorizedy)
    for i in range(len(sort[1])):
        title = datatitles[i]
        data = [categorizedx[i],categorizedy[i]]
        n= len(data[0])
        avecolor= (float(round(statistics.mean(data[0]),2)),float(round(statistics.mean(data[1]),2)))
        stdevcolor = (float((round(np.std(data[0]),3))),float(round(np.std(data[1]),3)))
        undatax = uncategorizedx[i]
        uncertaintyx = np.mean(undatax)
        undatay = uncategorizedy[i]
        uncertaintyy = np.mean(undatay)
        minifig= fig.add_subplot(dim[1],dim[0],i + 1)
        minifig.set_xlabel("")
        minifig.set_ylabel("")
        #minifig.set_title(title + f'\nN={n}  ' + r'$\bar{x}=$' + str(avecolor) + '\ns=' + str(stdevcolor), fontsize=20)
        plt.title(title, fontsize=28)
        plt.xlim(rangex[0],rangex[1])
        plt.ylim(rangey[0],rangey[1])
        if n >100:
            sns.kdeplot(data= df[(df == datatitles[i]).any(axis=1)], x='xcoor', y='ycoor', 
                        shade=True, cmap=ccolordict[title], shade_lowest=False)
        else:
            for j in range(len(data[0])):
                plt.plot(data[0][j],data[1][j],'o', color= colordict[title])
        minifig.set(xlabel=None, ylabel=None)
        minifig.tick_params(labelsize=20)
        #Ave HII box and cutoffs will only show for F70/F24 vs. F24/F8 plots 
        #remove conditional and adjust these if you want to plot relevant lines/boxes for other plots
        if colorx == ['F70','F24'] and colory == ['F24','F8']:
            plt.axhline(y=1.0,color='k', linestyle='dashed', label='')
            plt.axvline(x=0.8, color='k', linestyle='dashed', label='')
            #Average HII box
            plt.vlines(1.05, 0.26, 0.84, colors='k', linestyles='solid', label='')
            plt.vlines(1.47, 0.26, 0.84, colors='k', linestyles='solid', label='')
            plt.hlines(0.26, 1.05,1.47, colors='k', linestyles='solid', label='')
            plt.hlines(0.84, 1.05, 1.47, colors='k', linestyles='solid', label='')
        #Show Statistics on Plot
        minifig.text(0.1,.88,'N=' + str(n), fontsize=20, transform=minifig.transAxes)
        minifig.text(0.1,.84, r'$\bar{x} =$' + str(avecolor), fontsize=20, transform=minifig.transAxes)
        minifig.text(0.1,.8, r'$s =$' + str(stdevcolor), fontsize=20, transform=minifig.transAxes)
        plt.hlines(rangey[0] + rangey[2], (rangex[1] - rangex[2])-uncertaintyx, (rangex[1] - rangex[2])+uncertaintyx, colors='k', linestyles='dotted')
        plt.vlines(rangex[1] - rangex[2], (rangey[0] + rangey[2])-uncertaintyy, (rangey[0] + rangey[2])+uncertaintyy, colors='k', linestyles='dotted')
       # GWC removed 70/24 and 24/8 from the print statements on 11may26.
       # print('70/24 Uncertainty ' + title + ': '+ str(uncertaintyx))
       # print('24/8 Uncertainty ' + title + ': '+ str(uncertaintyy))
        print('Uncertaintyx ' + title + ': '+ str(uncertaintyx))
        print('Uncertaintyy ' + title + ': '+ str(uncertaintyy))
    fig.savefig(fname= save_name, transparent=True)
    plt.ioff()
    plt.show()