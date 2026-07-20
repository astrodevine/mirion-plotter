import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Button, TextBox, CheckButtons
from matplotlib.widgets import RadioButtons
import statistics
import math
from matplotlib.lines import Line2D

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
def restart(event):
    import os
    import sys
    os.execv(sys.executable, [sys.executable] + sys.argv)
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
def table_scatter(event):
    global plttype
    global done
    global scatopt
    plt.close()
    plttype = 7
    scatopt = 3
    done = True
    return scatopt
def physscat(event):
    global done
    global scatopt
    plt.close()
    done = True
    scatopt = 2
    return scatopt
def make_table1(event):
    global plttype
    global done
    plt.close()
    plttype = 6
    done = True
    return plttype
def table_scatter_opt(event):
    global scatopt
    global done
    plt.close()
    scatopt = 1
    done = True
    return scatopt
def scatter_quar(event):
    global scatopt
    global done
    plt.close()
    scatopt = 4
    done = True
    return scatopt
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
def make_table(event):
    global plttype
    plt.close()
    plttype = 6
    return plttype
def make_scatter_color(event):
    global done
    global plttype 
    global scatopt
    plt.close()
    done = True
    plttype = 7
    scatopt = 3
    return plttype
def includedistacne(event):
    global plttype
    plt.close()
    plttype = 5
    return plttype

def select_table_physical():
    global physical
    global physeq
    global phys_title
    global quartile_val
    global quar_title
    physical = ['LRAT']
    physeq = r"Luminosity Ratio [$\log_{10}(L/L_{\mathrm{ssm}})$]"
    phys_title = "Luminosity Ratio"
    quartile_val = [25]
    quar_title = "0-25%"
    # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
    colorsel = plt.figure(figsize= (6,5))
        # colorsel.suptitle('Select Color', fontsize = 15)
    colorsel.suptitle('Select Physical Property and Quartile', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
    axes2 = plt.axes([.25,.45,.5,.35])
                                        # radio_props={'s':[64]*len(coloroptions)})
    radio_hist2= RadioButtons(axes2, physical_options, label_props={'fontsize':[10]*len(physical_options)},
                                        radio_props={'s':[64]*len(physical_options)})
    radio_hist2.on_clicked(histphysicalfunc)

    axes3 = plt.axes([.25,.2,.5,.2])
                                        # radio_props={'s':[64]*len(coloroptions)})
    radio_hist3= RadioButtons(axes3, quartile, label_props={'fontsize':[10]*len(quartile)},
                                        radio_props={'s':[64]*len(quartile)})
    radio_hist3.on_clicked(quartilefunc)

    axes2 = plt.axes([.2,.05,.6,.1])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    plt.show()
        
    global done
    done = False
    while done==False:
        plt.pause(.1)
    return physical
def select_table_physical_opt():
    global physical
    global phys_title
    physical = ['LR_quar']
    phys_title = "Luminosity Ratio"
    # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
    colorsel = plt.figure(figsize= (6,5))
        # colorsel.suptitle('Select Color', fontsize = 15)
    colorsel.suptitle('Select Physical Property and Quartile', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
    axes2 = plt.axes([.25,.45,.5,.35])
                                        # radio_props={'s':[64]*len(coloroptions)})
    radio_hist2= RadioButtons(axes2, physical_options, label_props={'fontsize':[10]*len(physical_options)},
                                        radio_props={'s':[64]*len(physical_options)})
    radio_hist2.on_clicked(histphysicalfunc_tab)

    axes2 = plt.axes([.2,.05,.6,.1])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    plt.show()
        
    global done
    done = False
    while done==False:
        plt.pause(.1)
    return physical
def select_table_catalog():
    global table_cat
    global table_cat_title
   # global cutoff
   # global sign
   # cutoff = .5
    table_cat = ['All Sources']
    table_cat_title = ["all_sources"]
   # sign = ">"
    # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
    colorsel = plt.figure(figsize= (6,5))
        # colorsel.suptitle('Select Color', fontsize = 15)
    colorsel.suptitle('Select Catalog For Table', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
   # startbox_axes10 = plt.axes([.3,.78,.4,.1])
   # cutoffentry10 = TextBox(startbox_axes10, 'Cutoff:')
   # cutoffentry10.on_submit(entrynumber)
   # axes1 = plt.axes([.25,.66,.5,.1])
                                        # radio_props={'s':[64]*len(coloroptions)})
   # radio_hist1= RadioButtons(axes1, cutoff_sign, label_props={'fontsize':[10]*len(cutoff_sign)},
   #                                     radio_props={'s':[64]*len(cutoff_sign)})
   # radio_hist1.on_clicked(cutsign)

    axes = plt.axes([.25,.14,.5,.5])
                                        # radio_props={'s':[64]*len(coloroptions)})
    radio_hist= RadioButtons(axes, table_sortlist, label_props={'fontsize':[10]*len(table_sortlist)},
                                        radio_props={'s':[64]*len(table_sortlist)})
    radio_hist.on_clicked(tablecatfunc)

    axes2 = plt.axes([.2,.02,.6,.1])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    plt.show()
        
    global done
    done = False
    while done==False:
        plt.pause(.1)
    return 
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

def select_cat_o_phys():
    startup5 = plt.figure(figsize= (5,3))
    startup5.suptitle('Select Plot Points', fontsize = 20, y = .9)
    cc_axes5 = plt.axes([.15,.52,.7,.20])
    ccbutton5 = Button(cc_axes5, 'Scatter Plot Half Catalog')
    ccbutton5.on_clicked(table_scatter)
    cc_axes6 = plt.axes([.15,.27,.7,.20])
    ccbutton6 = Button(cc_axes6, 'Scatter Plot Full Catalog')
    ccbutton6.on_clicked(table_scatter_opt)
    table_axes5 = plt.axes([.15,.02,.7,.20])
    tablebutton5 = Button(table_axes5, 'Scatter Plot Quartile')
    tablebutton5.on_clicked(scatter_quar)

    global done
    done = False
    while done==False:
        plt.pause(.1)
    plt.show()
    return 

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
        global phys_title
        physical = ['LRAT']
        physeq = r"Luminosity Ratio [$\log_{10}(L/L_{\mathrm{ssm}})$]"
        phys_title = "Luminosity Ratio"
        # GWC - Changed figsize, fontsize, axes to make room for more colors. 5/12/26
        # colorsel = plt.figure(figsize= (5,4))
        colorsel = plt.figure(figsize= (6,5))
        # colorsel.suptitle('Select Color', fontsize = 15)
        colorsel.suptitle('Select Physical Property For Histogram', fontsize = 20, y = .96)
        # axes = plt.axes([.2,.3,.7,.5])
        # radio_hist= RadioButtons(axes, coloroptions, label_props={'fontsize':[15]*len(coloroptions)},
                                 # radio_props={'s':[64]*len(coloroptions)})
        axes = plt.axes([.25,.3,.5,.6])
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
def physquestion():
    global physanswer
    physanswer = True
    discel1 = plt.figure(figsize=(4,6))
    discel1.suptitle("Filter by Quartile of Physcial Property?")
    #startbox_axes = plt.axes([.2,.8,.4,.1])
    axes14 = plt.axes([.15,.3,.7,.5])
    exsort14= RadioButtons(axes14, ["Yes","No"], label_props={'fontsize':[10]*len(disoption)}, radio_props={'s':[64]*len(disoption)})
    exsort14.on_clicked(physyesorno)
    axes14 = plt.axes([.25,.075,.5,.1])
    contbutton = Button(axes14, 'Continue')
    contbutton.on_clicked(close)
    global done
    done = False

    while not done:
        plt.pause(.1)
    plt.show()
    return
def distanceoption():
    global answer
    answer = True
    discel = plt.figure(figsize=(4,6))
    discel.suptitle("Filter by Distance?")
    #startbox_axes = plt.axes([.2,.8,.4,.1])
    axes7 = plt.axes([.15,.3,.7,.5])
    exsort7= RadioButtons(axes7, ["Yes","No"], label_props={'fontsize':[10]*len(disoption)}, radio_props={'s':[64]*len(disoption)})
    exsort7.on_clicked(yesorno)
    axes8 = plt.axes([.25,.075,.5,.1])
    contbutton = Button(axes8, 'Continue')
    contbutton.on_clicked(close)
    global done
    done = False

    while not done:
        plt.pause(.1)
    plt.show()
    return
def yesorno(label):
    global answer
    answerlst = {"Yes": True, 
                    "No": False,}
    answer = answerlst[label] 
def physyesorno(label):
    global physanswer
    physanswerlst = {"Yes": True, 
                    "No": False,}
    physanswer = physanswerlst[label]  
def actdistance():
    global lmax
    global lmin
    global bmax
    global bmin
    global dismax
    global dismin
    lmax = 360
    lmin = 0
    bmax = 2
    bmin = -2
    dismax = 200
    dismin = 0
    excsel10 = plt.figure(figsize=(10,6))
    excsel10.suptitle('Set Exclusion Parameters')
    startbox_axes10 = plt.axes([.1,.75,.4,.1])
    cutoffentry10 = TextBox(startbox_axes10, 'l Max')
    cutoffentry10.on_submit(entrynumber10)

    startbox_axes11 = plt.axes([.1,.63,.4,.1])
    cutoffentry11 = TextBox(startbox_axes11, 'l Min')
    cutoffentry11.on_submit(entrynumber11)

    startbox_axes12 = plt.axes([.1,.51,.4,.1])
    cutoffentry12 = TextBox(startbox_axes12, 'b Max')
    cutoffentry12.on_submit(entrynumber12)

    startbox_axes13 = plt.axes([.1,.39,.4,.1])
    cutoffentry13 = TextBox(startbox_axes13, 'b Min')
    cutoffentry13.on_submit(entrynumber13)

    startbox_axes14 = plt.axes([.1,.27,.4,.1])
    cutoffentry14 = TextBox(startbox_axes14, 'Distance Max')
    cutoffentry14.on_submit(entrynumber14)

    startbox_axes15 = plt.axes([.1,.15,.4,.1])
    cutoffentry15 = TextBox(startbox_axes15, 'Distance Min')
    cutoffentry15.on_submit(entrynumber15)

    axes9 = plt.axes([.25,.03,.5,.1])
    contbutton4 = Button(axes9, 'Continue')
    contbutton4.on_clicked(close)
    global done
    done = False

    while not done:
        plt.pause(.1)
    plt.show()
    return
def cutsign(label):
    global sign 
    sign = label
    return sign
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
def tablecatfunc(label):
    global table_cat
    global table_cat_title
    tbcat = {'All Sources':['All Sources'], 'RMS':['RMS'], 'WISE C,G,K':['WISE C,G,K'], 'WISE Q':['WISE Q'], 
             'CORNISH': ["CORNISH"], 'No Association':['No Association'] }
    tbcat_title = {'All Sources':['all_sources'], 'RMS':['RMS'], 'WISE C,G,K':['WISE_C,G,K'], 'WISE Q':['WISE Q'], 
             'CORNISH': ["CORNISH"], 'No Association':['no_association'] }
    table_cat = tbcat[label]
    table_cat_title = tbcat_title[label]
    return table_cat, table_cat_title
def histphysicalfunc(label):
    global physical
    global physeq
    global phys_title
    physicaldict = {"Luminosity Ratio": ['LRAT'], 
                    "Bolometric Temperature": ['TBOL'],
                    "Surface Density": ['SIGMA'],
                    "Greybody Temperature": ['TEMP'],
                    "Mass": ["MASS"],
                    "Bolometric Luminosity": ["BLUM"],
                    "Diameter": ["DIAM"],
                    "Bolometric Luminosity/Mass": ["LMRAT"]}
    physicalform = {"Luminosity Ratio": r"Luminosity Ratio [$\log_{10}(L/L_{\mathrm{ssm}})$]",
                    "Bolometric Temperature": r"Bolometric Temperature [$T_{\mathrm{bol}}/\mathrm{K}$]",
                    "Surface Density": r"Surface Density [$\log_{10}(\sum/\mathrm{g\,cm^{-3}})$]",
                    "Greybody Temperature": r"Greybody Temperature [$T_{\mathrm{g}}/\mathrm{K}$]",
                    "Mass": r"Mass [$\log_{10}(M/M_\odot)$]",
                    "Bolometric Luminosity": r"Bolometric Luminosity [$\log_{10}(L/L_\odot)$]",
                    "Diameter": r"Diameter [$\log_{10}(D/\mathrm{pc})$]",
                    "Bolometric Luminosity/Mass": r"Bolometric Luminosity/Mass [$\log_{10}(L/L_\odot \,/\, M/M_\odot)$]"}
    physical = physicaldict[label]
    physeq = physicalform[label]
    phys_title = label
    return physical, physeq
def histphysicalfunc_tab(label):
    global physical
    global phys_title
    physicaldict = {"Luminosity Ratio": ['LR_quar'], 
                    "Bolometric Temperature": ['BT_quar'],
                    "Surface Density": ['SD_quar'],
                    "Greybody Temperature": ['GT_quar'],
                    "Mass": ["MA_quar"],
                    "Bolometric Luminosity": ["BL_quar"],
                    "Diameter": ["DIA_quar"],
                    "Bolometric Luminosity/Mass": ["BLM_quar"]}
    physical = physicaldict[label]
    phys_title = label
    return physical
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
def physicalswitch(label):
    global physcolorcolor
    global physlabel
    physicaldict = {"Luminosity Ratio": ['LRAT'], 
                    "Bolometric Temperature": ['TBOL'],
                    "Surface Density": ['SIGMA'],
                    "Greybody Temperature": ['TEMP'],
                    "Mass": ["MASS"],
                    "Bolometric Luminosity": ["BLUM"],
                    "Diameter": ["DIAM"],
                    "Bolometric Luminosity/Mass": ["LMRAT"]}
    physicalform = {"Temperature": r"Temperature [$T_{\mathrm{bol}}/\mathrm{K}$]",
                    "Mass": r"Mass [$\log_{10}(M/M_\odot)$]"}
    physcolorcolor = physicaldict[label]
    physlabel = label
    #phys_title = label
    return physcolorcolor, physlabel
def quartilefunc(label):
    global quartile_val
    global quar_title
    quartiledict = {"0-25%":[25],
                    "25-50%":[50],
                    "50-75%":[75],
                    "75-100%":[100]}
    quartile_val = quartiledict[label]
    quar_title = label
    return quartile_val, quar_title
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
def entrynumber10(entry):
    global lmax
    lmax = float(entry)
    return lmax
def entrynumber11(entry):
    global lmin
    lmin = float(entry)
    return lmin
def entrynumber12(entry):
    global bmax
    bmax = float(entry)
    return bmax
def entrynumber13(entry):
    global bmin
    bmin = float(entry)
    return bmin
def entrynumber14(entry):
    global dismax
    dismax = float(entry)
    return dismax
def entrynumber15(entry):
    global dismin
    dismin = float(entry)
    return dismin
def excludeoptions():
    excsel = plt.figure(figsize=(10,6))
    excsel.suptitle('Set Exclusion Parameters')
    startbox_axes = plt.axes([.1,.75,.4,.1])
    global cutoff
    cutoffentry = TextBox(startbox_axes, 'Set Cutoff')
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
    cutoffentry = TextBox(startbox_axes, 'Set Cutoff')
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

def physcolor():
    global physcolorcolor
    global physlabel
    physcolorcolor = ["LRAT"]
    physlabel = "Luminosity Ratio"
    excsel = plt.figure(figsize=(4,6))
    excsel.suptitle("Choose Physical Property To Include")
    #startbox_axes = plt.axes([.2,.8,.6,.1])
    axes0 = plt.axes([.15,.3,.7,.5])
    global clicked0
    clicked0 = [False] * len(physoption)
    exsort0= RadioButtons(axes0, physoption, label_props={'fontsize':[10]*len(physoption)}, radio_props={'s':[64]*len(physoption)})
    exsort0.on_clicked(physicalswitch)
    axes2 = plt.axes([.25,.075,.5,.1])
    contbutton = Button(axes2, 'Continue')
    contbutton.on_clicked(close)
    global done
    done = False

    while not done:
        plt.pause(.1)
    plt.show()
    return

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
    if len(longest_list) == 0:
            plt.close(fig)
            excsel2 = plt.figure(figsize=(3,2))
            excsel2.suptitle('No Yellow Balls to Plot')

            axes2 = plt.axes([.25,.03,.5,.1])
            contbutton2 = Button(axes2, 'Try Again')
            contbutton2.on_clicked(restart)

            global done1
            done1 = False

            while not done1:
                plt.pause(.1)
            plt.show()
    mean = statistics.mean(longest_list)
    dev = np.std(longest_list)
    return [mean-4*dev, mean + 4*dev]

def get_rangecc(datacol):
    longest_list = max(datacol, key=len)
    if len(longest_list) == 0:
            plt.close(fig)
            excsel2 = plt.figure(figsize=(3,2))
            excsel2.suptitle('No Yellow Balls to Plot')

            axes2 = plt.axes([.25,.03,.5,.1])
            contbutton2 = Button(axes2, 'Try Again')
            contbutton2.on_clicked(restart)

            global done1
            done1 = False

            while not done1:
                plt.pause(.1)
            plt.show()
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
startup.suptitle('Select Plot Type', fontsize = 18, y = .95)
hist_axes = plt.axes([.15,.65,.7,.15])
histbutton = Button(hist_axes, 'Histogram', )
histbutton.on_clicked(make_histograms)
cc_axes = plt.axes([.15,.45,.7,.15])
ccbutton = Button(cc_axes, 'Color-Color Plot')
ccbutton.on_clicked(make_colorcolor)
table_axes = plt.axes([.15,.25,.7,.15])
tablebutton = Button(table_axes, 'Create Table')
tablebutton.on_clicked(make_table1)
cc_axes2 = plt.axes([.15,.05,.7,.15])
ccbutton2 = Button(cc_axes2, 'Scatter Plot')
ccbutton2.on_clicked(table_scatter)

plttype= 0
plt.show()
while plttype==0:
    plt.pause(0.1)

plt.close()
disoption = ["Yes","No"]

if plttype != 7:
    distanceoption()
    if answer == True:
        actdistance()
    if plttype == 3:
        select_color_physical()

# Step 2: Choose what color(s) you want to plot
coloroptions = ['1100/870','1100/500','1100/350','1100/250','1100/160','1100/70','1100/24',
                '1100/12','1100/8','870/500','870/350','870/250','870/160','870/70','870/24',
                '870/12','870/8','500/350','500/250','500/160','500/70','500/24','500/12','500/8',
                '350/250','350/160','350/70','350/24','350/12','350/8','250/160','250/70',
                '250/24','250/12','250/8',
                '160/70','160/24','160/12','160/8','70/24','70/12','70/8','24/12','24/8','12/8']

colorsep = [['F1100','F870'], ['F1100','F500'], ['F1100','F350'],
                ['F1100','F250'], ['F1100','F160'], ['F1100','F70'],
                ['F1100','F24'], ['F1100','F12'], ['F1100','F8'],
                ['F870','F500'], ['F870','F350'],
                ['F870','F250'], ['F870','F160'], ['F870','F70'],
                ['F870','F24'], ['F870','F12'], ['F870','F8'],
                ['F500','F350'], ['F500','F250'], ['F500','F160'], 
                ['F500','F70'], ['F500','F24'], ['F500','F12'], 
                ['F500','F8'], ['F350','F250'], ['F350','F160'], 
                ['F350','F70'], ['F350','F24'], ['F350','F12'], 
                ['F350','F8'], ['F250','F160'], ['F250','F70'], 
                ['F250','F24'], ['F250','F12'], ['F250','F8'],
                ['F160','F70'], ['F160','F24'], ['F160','F12'], 
                ['F160','F8'],['F70','F24'], ['F70','F12'],
                ['F70','F8'],['F24','F12'], ['F24','F8'], ['F12','F8']]

physical_options = ["Luminosity Ratio", 
                    "Bolometric Temperature",
                    "Surface Density",
                    "Greybody Temperature",
                    "Mass",
                    "Bolometric Luminosity",
                    "Diameter",
                    "Bolometric Luminosity/Mass"]
table_sortlist = ['All Sources', 'RMS', 'WISE C,G,K', 'WISE Q', 'CORNISH', 'No Association']

cutoff_sign = [">","<"]

quartile = ["0-25%","25-50%","50-75%","75-100%"]
# GWC - This assignment needs to point to the first entry in colordict. 5/12/26
# color = ['F70','F24']
color = ['F1100','F870']
if plttype == 6:
    select_table_catalog()
    flagexlist = ['No Obvious Source', 'Poor Confidence', 'Multiple Sources', 
                        'Very Circular']
    physquestion()
    if physanswer == True:
        select_table_physical()
elif plttype == 7:
    if scatopt == 3:
        select_cat_o_phys()
    if scatopt == 4:
       select_table_physical_opt()
else:    
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
        cutoff = 1000

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
    if plttype == 2 :
        physoption = ["Luminosity Ratio", 
                        "Bolometric Temperature",
                        "Surface Density",
                        "Greybody Temperature",
                        "Mass",
                        "Bolometric Luminosity",
                        "Diameter",
                        "Bolometric Luminosity/Mass"]
        physcolor()
    if plttype == 4 :
        #Step 4: Select parameters used to exclude data
        extype0 = ['By Flag']
        flagexlist = ['No Obvious Source', 'Poor Confidence', 'Multiple Sources', 
                    'Very Circular']
        cutoff = 1000

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
 
    distcolspecs=[(0,4),(5,10),(11,16),(17,22),(23,29),(30,36),(37,48),(49,53),(54,59),(60,65),(66,70),(71,76),(77,82),(83,87),(88,92),(93,98)]
    distnames=["ID","DIST","e_DIST","DIST_C","DIST_M","e_DIST_M","STAT_M","PFAR","DIST_R1","e_DIST_R1","PINT_R1","ARM_R1","DIST_R2","e_DIST_R2","PINT_R2","ARM_R2"]
    distdata = pd.read_fwf("MRT-dist.txt",colspecs=distcolspecs,names=distnames, sep=r"\s+", skiprows = 29, usecols=["ID"] + ["DIST"])

    cordcolspecs=[(0,4),(5,14),(15,23),(24,31),(32,39),(40,47),(48,55),(56,60),(60,68),(69,77),(78,85),(86,94),(95,102),(103,110),(111,120),(121,130),(131,133),(134,136),(137,139),(140,141),(142,146),(147,148),(149,153),(154,158),(159,160)]
    cordnames=["ID","GLON","GLAT","MWPR","e_GLON","e_GLAT","e_MWPR","HRATE","F8","e_F8","F12","e_F12","F24","e_F24","F70","e_F70","N8","N12","N24","N70","f_SAT","f_MULTI","f_NOSRC","f_PCONF","f_CEXT"]
    corddata = pd.read_fwf("MRT-phot.txt",colspecs=cordcolspecs, names=cordnames, sep=r"\s+", skiprows = 39, usecols=["ID"] + ["GLON"] + ["GLAT"])

    merged1 = pd.merge(distdata, xmatdata, left_on="ID", right_on="YB", how="inner")
    merged = pd.merge(corddata, merged1, left_on="ID", right_on="ID", how="inner")
    # Remove Rows based on exclusion parameters
    # Changing range from 6176 to 3945 for Herschel-matched objects. GWC 5/8/26.
    excludeidx = []
    for i in range(len(merged)):
        for j in range(len(exclusionheaders)):
            if int(merged[exclusionheaders[j]][i])== 1:
                excludeidx += [i]
        FEvals = [float(merged['e_'+color[0]][i]), float(merged['e_'+color[1]][i])]
        if exclusions[0]<max(FEvals) or min(FEvals)<0:
            excludeidx += [i]
    excludeidx = list(set(excludeidx))
    # Sort into lists based on sorting categories
    if answer == True:
        criteria = ((merged["DIST"] < dismax) & 
                    (merged["DIST"] > dismin) &
                    (merged["GLAT"] < bmax) &
                    (merged["GLAT"] > bmin) &
                    (merged["GLON"] < lmax) &
                    (merged["GLON"] > lmin))
        merged = merged.loc[criteria].reset_index(drop=True)
    categorized = []
    uncategorized = []
    for j in sort[1]:
        cat = []
        uncat = []
        for i in range(len(merged)):
            colornum = float(merged[color[0]][i])
            colornums = float(merged['u_' + color[0]][i])
            colorden = float(merged[color[1]][i])
            colordens = float(merged['u_' + color[1]][i])
            entry = np.log10(colornum/colorden)
            unc2 = ((colornums**2)/(colornum*np.log(10))**2)+((colordens**2)/(colorden*np.log(10))**2)
            unentry = np.sqrt(unc2)
            if np.isnan(entry) == False and np.isnan(unentry) == False and i not in excludeidx:
                if j =='All Sources':
                    cat.append(entry)
                    uncat.append(unentry)
                elif j=='Neither':
                    if merged['Multiple Sources'][i] == 0 and merged['Very Circular'][i]==0:
                        cat.append(entry)
                        uncat.append(unentry)
                elif 'Not ' in j:
                    if merged[j.replace('Not ','')][i]==0:
                        cat.append(entry)
                        uncat.append(unentry)
                else:
                    if merged[j][i]==1:
                        cat.append(entry)
                        uncat.append(unentry)
        categorized.append(cat)
        uncategorized.append(uncat)
    #Make Histograms (Finally)
    dim = get_dimensions(len(categorized))
    colorname = color[0] + '/' + color[1]
    fig= plt.figure(figsize=(8*dim[0],8*dim[1]))
    fig.canvas.header_visible= False
    if exclusions[0] < 1000:
        cut = f"Cutoff {str(exclusions[0])}"
    else:
        cut = "No Cutoff"
    fig.suptitle(r'$log_{10}$'+f'({colorname}) Color Histograms\n{cut}', fontsize = 25)
    plt.axis('off')
    fig.subplots_adjust(left=.2, right=.95, top=.85, bottom=.1)
    fig.text(.5, .02, r'$log_{10}$'+f'({colorname})', fontsize=28, ha='center')
    plt.text(-.1, 0.5, 'Number', fontsize=28, rotation='vertical', va='center')
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
        cnts, bns, ptchs = plt.hist(data, facecolor=colordict[title], bins= binlen, range=(datarng), edgecolor="black")
        minifig.tick_params(labelsize=20)
        y = max(cnts)
        #Average lines for F12/F8 colors, will only plot if those colors are selected
        if colorname == 'F12/F8':
            HIIline= minifig.axvline(x=-0.09, color='black', linestyle='-.', label= 'HII Region Average')
            PAVEline= minifig.axvline(x=-0.43, color='black', linestyle='--', label= 'Pilot Region Average')
        #Other formatting things
        FAVEline= plt.axvline(x=avecolor, color='black', label= title + ' Average')
        minifig.text(datarng[0], .93 *y,'N=' + str(n), fontsize=28)
        minifig.text(datarng[0],.87*y,r'$\bar{x} =$' + str(round(avecolor,2)), fontsize=28)
        minifig.text(datarng[0],.81*y,r'$s =$' + str(round(stdevcolor,3)), fontsize=28)
        minifig.errorbar(datarng[0]+ uncertainty,.65*y,xerr=uncertainty, yerr=None, capsize=10, color='k')
        minifig.vlines(datarng[0]+uncertainty, .61*y, .69*y, colors='k')
        print('Uncertainty ' + sort[1][i] + ': ' + str(uncertainty))
    plt.ioff()
    plt.show()


if plttype == 4:
    hcsccolspecs=[(0,4),(5,9),(10,14),(15,23),(24,35),(36,46),(47,57),(58,64),(65,74),(75,80),(81,85),(86,94),(95,102),(103,109),(110,115),(116,121),(122,129)]
    hcscnames=["ID","DIAM","e_DIAM","MASS","e_MASS","BLUM","e_BLUM","LMRAT","e_LMRAT","TEMP","e_TEMP","LRAT","e_LRAT","TBOL","e_TBOL","SIGMA","e_SIGMA"]
    data_hcsc = pd.read_fwf("MRT-hcsc.txt",colspecs=hcsccolspecs,names=hcscnames, sep=r"\s+", skiprows=28, usecols= physical + ["ID"] + ["e_" + physical[0]])
    
    distcolspecs=[(0,4),(5,10),(11,16),(17,22),(23,29),(30,36),(37,48),(49,53),(54,59),(60,65),(66,70),(71,76),(77,82),(83,87),(88,92),(93,98)]
    distnames=["ID","DIST","e_DIST","DIST_C","DIST_M","e_DIST_M","STAT_M","PFAR","DIST_R1","e_DIST_R1","PINT_R1","ARM_R1","DIST_R2","e_DIST_R2","PINT_R2","ARM_R2"]
    distdata = pd.read_fwf("MRT-dist.txt",colspecs=distcolspecs,names=distnames, sep=r"\s+", skiprows = 29, usecols=["ID"] + ["DIST"])

    sortheaders = [x.replace('Not ','') for x in sort[1] if x != 'All Sources' and x!= 'Neither']
    xmatdata = pd.read_csv("PlotMaster-10fluxes-GWC.csv", usecols=["YB"]+sortheaders)

    merged2 = pd.merge(data_hcsc, xmatdata, left_on="ID", right_on="YB", how="inner")
    merged1 = pd.merge(distdata, merged2, left_on="ID", right_on="ID", how="inner")
    
    cordcolspecs=[(0,4),(5,14),(15,23),(24,31),(32,39),(40,47),(48,55),(56,60),(60,68),(69,77),(78,85),(86,94),(95,102),(103,110),(111,120),(121,130),(131,133),(134,136),(137,139),(140,141),(142,146),(147,148),(149,153),(154,158),(159,160)]
    cordnames=["ID","GLON","GLAT","MWPR","e_GLON","e_GLAT","e_MWPR","HRATE","F8","e_F8","F12","e_F12","F24","e_F24","F70","e_F70","N8","N12","N24","N70","f_SAT","f_MULTI","f_NOSRC","f_PCONF","f_CEXT"]
    corddata = pd.read_fwf("MRT-phot.txt",colspecs=cordcolspecs, names=cordnames, sep=r"\s+", skiprows = 39, usecols=["ID"] + ["GLON"] + ["GLAT"])
    
    merged = pd.merge(corddata, merged1, left_on="ID", right_on="ID", how="inner")
    merged = merged[merged[physical[0]]>0].reset_index(drop=True)
    print("Before exclusions:", len(merged))
    print("Cutoff:", exclusions[0])
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
    if answer == True:
        criteria = ((merged["DIST"] < dismax) & 
                    (merged["DIST"] > dismin) &
                    (merged["GLAT"] < bmax) &
                    (merged["GLAT"] > bmin) &
                    (merged["GLON"] < lmax) &
                    (merged["GLON"] > lmin))
        merged = merged.loc[criteria].reset_index(drop=True)
    if 'Neither' in sort[1]:
        sortheaders.append('Multiple Sources')
        sortheaders.append('Very Circular')
    #Put together a relevant dataframe
    physical_data = merged[physical[0]]
    if physical[0] in ['LRAT', 'SIGMA', "MASS", "BLUM", "DIAM", "LMRAT"]:
        log_physical_data = np.log10(physical_data)
        log_physical_data_tot = np.log10(physical_data).tolist()
    else:
        log_physical_data = physical_data
        log_physical_data_tot = physical_data.tolist()
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
    if exclusions[0] < 1000:
        cut = f"Cutoff {str(exclusions[0])}"
    else:
        cut = "No Cutoff"
    fig.suptitle(f'{phys_title} Histograms\n{cut}', fontsize = 25)
    fig.patch.set_facecolor("White")
    fig.text(.5, .02,f'{physeq}', fontsize=28, ha='center')
    fig.text(.02, 0.5, 'Number', fontsize=28, rotation='vertical', va='center')
    if len(log_physical_data_tot) == 0:
        plt.close(fig)
        excsel2 = plt.figure(figsize=(3,2))
        excsel2.suptitle('No Yellow Balls to Plot')

        axes2 = plt.axes([.25,.03,.5,.1])
        contbutton2 = Button(axes2, 'Try Again')
        contbutton2.on_clicked(restart)

        global done
        done = False

        while not done:
            plt.pause(.1)
        plt.show()

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
        plt.hist(log_physical_data, bins= binlen, range=(datarng), edgecolor="black")
        cnts, bns, ptchs = plt.hist(data, bins= binlen, range=(datarng), edgecolor="black")
        minifig.set_xlim(datarng)
        minifig.tick_params(labelsize=20)
        y = max(cnts)
        #Average lines for F12/F8 colors, will only plot if those colors are selected
        #Other formatting things
        FAVEline= plt.axvline(x=avephys, color='black', label= title + ' Average')
        minifig.text(.62,.93,'N=' + str(n), fontsize=28, transform = minifig.transAxes)
        minifig.text(.62,.87,r'$\bar{x} =$' + str(round(avephys,2)), fontsize=28, transform = minifig.transAxes)
        minifig.text(.62,.81,r'$s =$' + str(round(stdevphys,3)), fontsize=28, transform = minifig.transAxes)
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
    
    hcsccolspecs=[(0,4),(5,9),(10,14),(15,23),(24,35),(36,46),(47,57),(58,64),(65,74),(75,80),(81,85),(86,94),(95,102),(103,109),(110,115),(116,121),(122,129)]
    hcscnames=["ID","DIAM","e_DIAM","MASS","e_MASS","BLUM","e_BLUM","LMRAT","e_LMRAT","TEMP","e_TEMP","LRAT","e_LRAT","TBOL","e_TBOL","SIGMA","e_SIGMA"]
    data_hcsc = pd.read_fwf("MRT-hcsc.txt",colspecs=hcsccolspecs,names=hcscnames, sep=r"\s+", skiprows=28, usecols= ["ID"] + physcolorcolor)
    
    distcolspecs=[(0,4),(5,10),(11,16),(17,22),(23,29),(30,36),(37,48),(49,53),(54,59),(60,65),(66,70),(71,76),(77,82),(83,87),(88,92),(93,98)]
    distnames=["ID","DIST","e_DIST","DIST_C","DIST_M","e_DIST_M","STAT_M","PFAR","DIST_R1","e_DIST_R1","PINT_R1","ARM_R1","DIST_R2","e_DIST_R2","PINT_R2","ARM_R2"]
    distdata = pd.read_fwf("MRT-dist.txt",colspecs=distcolspecs,names=distnames, sep=r"\s+", skiprows = 29, usecols=["ID"] + ["DIST"])
    print(data_hcsc["ID"].dtype)
    print(xmatdata["YB"].dtype)

    print(repr(data_hcsc["ID"].iloc[0]))
    print(repr(xmatdata["YB"].iloc[0]))
    merged2 = pd.merge(data_hcsc, xmatdata, left_on="ID", right_on="YB", how="inner")
    merged1 = pd.merge(distdata, merged2, left_on="ID", right_on="ID", how="inner")
    
    cordcolspecs=[(0,4),(5,14),(15,23),(24,31),(32,39),(40,47),(48,55),(56,60),(60,68),(69,77),(78,85),(86,94),(95,102),(103,110),(111,120),(121,130),(131,133),(134,136),(137,139),(140,141),(142,146),(147,148),(149,153),(154,158),(159,160)]
    cordnames=["ID","GLON","GLAT","MWPR","e_GLON","e_GLAT","e_MWPR","HRATE","F8","e_F8","F12","e_F12","F24","e_F24","F70","e_F70","N8","N12","N24","N70","f_SAT","f_MULTI","f_NOSRC","f_PCONF","f_CEXT"]
    corddata = pd.read_fwf("MRT-phot.txt",colspecs=cordcolspecs,names=cordnames, sep=r"\s+", skiprows = 39, usecols=["ID"] + ["GLON"] + ["GLAT"])
    
    merged = pd.merge(corddata, merged1, left_on="ID", right_on="ID", how="inner")
    
    # Remove Rows based on exclusion parameters
    excludeidx = []
    for i in range(len(merged)):
        for j in range(len(exclusionheaders)):
            if int(merged[exclusionheaders[j]][i])== 1:
                excludeidx += [i]
        cutoff = exclusions[0]
        FEvals = []
        for k in colorx+colory:
            FEvals.append(float(merged['e_'+k][i]))
        if cutoff<max(FEvals) or min(FEvals)<0:
            excludeidx += [i]
    excludeidx = list(set(excludeidx))
    if answer == True:
        criteria = ((merged["DIST"] < dismax) & 
                    (merged["DIST"] > dismin) &
                    (merged["GLAT"] < bmax) &
                    (merged["GLAT"] > bmin) &
                    (merged["GLON"] < lmax) &
                    (merged["GLON"] > lmin))
        merged = merged.loc[criteria].reset_index(drop=True)
        print(len(merged))
    if physcolorcolor[0] in ['LRAT', 'SIGMA', "MASS", "BLUM", "DIAM", "LMRAT"]:
        log_physcolorcolor = np.log10(merged[physcolorcolor])
    else:
        log_physcolorcolor = merged[physcolorcolor]     
    # Sort into lists based on sorting categories
    categorizedx = []
    categorizedy = []
    uncategorizedx = []
    uncategorizedy = []
    catergorizedphyscolor = []
    for j in sort[1]:
        catx = []
        caty = []
        uncatx = []
        uncaty = []
        catphyscolor = []
        for i in range(len(merged)):
            colornumx = float(merged[colorx[0]][i])
            colornumsx = float(merged['u_' + colorx[0]][i])
            colordenx = float(merged[colorx[1]][i])
            colordensx = float(merged['u_' + colorx[1]][i])
            entryx = np.log10(colornumx/colordenx)
            unc2x = ((colornumsx**2)/(colornumx*np.log(10))**2)+((colordensx**2)/(colordenx*np.log(10))**2)
            unentryx = np.sqrt(unc2x)
            colornumy = float(merged[colory[0]][i])
            colornumsy = float(merged['u_' + colory[0]][i])
            colordeny = float(merged[colory[1]][i])
            colordensy = float(merged['u_' + colory[1]][i])
            entryy = np.log10(colornumy/colordeny)
            unc2y = ((colornumsy**2)/(colornumy*np.log(10))**2)+((colordensy**2)/(colordeny*np.log(10))**2)
            unentryy = np.sqrt(unc2y)
            if i not in excludeidx and not np.isnan(entryx) and not np.isnan(entryy) and not np.isnan(unentryx) and not np.isnan(unentryy):
                if j =='All Sources':
                    catx.append(entryx)
                    caty.append(entryy)
                    uncatx.append(unentryx)
                    uncaty.append(unentryy)
                    catphyscolor.append(float(log_physcolorcolor.iloc[i]))
                elif j=='Neither':
                    if xmatdata['Multiple Sources'][i] == 0 and xmatdata['Very Circular'][i]==0:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
                        catphyscolor.append(float(log_physcolorcolor.iloc[i]))
                elif 'Not ' in j:
                    if xmatdata[j.replace('Not ','')][i]==0:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
                        catphyscolor.append(float(log_physcolorcolor.iloc[i]))
                else:
                    if xmatdata[j][i]==1:
                        catx.append(entryx)
                        caty.append(entryy)
                        uncatx.append(unentryx)
                        uncaty.append(unentryy)
                        catphyscolor.append(float(log_physcolorcolor.iloc[i]))
        categorizedx.append(catx)
        categorizedy.append(caty)
        uncategorizedx.append(uncatx)
        uncategorizedy.append(uncaty)
        catergorizedphyscolor.append(catphyscolor)
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
    if cutoff < 1000:
        cut = f"Cutoff {str(cutoff)}"
    else:
        cut = "No Cutoff"
    fig.suptitle(r'$log_{10}$'+f'({colory[0]}/{colory[1]}) v. '+r'$log_{10}$'+f'({colorx[0]}/{colorx[1]})  Color-Color Density'+"\n"+cut, fontsize=20, y=.98)
    plt.axis('off')
    fig.subplots_adjust(left=.2, right=.95, top=.85, bottom=.1)
    plt.text(.5, .02, r'$log_{10}'+f'({colorx[0]}/{colorx[1]})$', fontsize=28, ha='center', transform=fig.transFigure)
    plt.text(.015, .5, r'$log_{10}'+f'({colory[0]}/{colory[1]})$', fontsize=28, rotation='vertical', va='center', transform=fig.transFigure)
    plt.text(.5, 1.075,'Cutoff: '+cut, fontsize = 20, ha='center', transform=fig.transFigure)
    rangex = get_rangecc(categorizedx)
    rangey = get_rangecc(categorizedy)
    for i in range(len(sort[1])):
        title = datatitles[i]
        data = [categorizedx[i],categorizedy[i]]
        physicalcolor = catergorizedphyscolor[i]
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
        sc = minifig.scatter(data[0], data[1], c=physicalcolor, cmap="rainbow", s = 10)
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
        minifig.text(0.05,.94,'N=' + str(n), fontsize=20, transform=minifig.transAxes)
        minifig.text(0.05,.9, r'$\bar{x} =$' + str(avecolor), fontsize=20, transform=minifig.transAxes)
        minifig.text(0.05,.86, r'$s =$' + str(stdevcolor), fontsize=20, transform=minifig.transAxes)
        plt.hlines(rangey[0] + rangey[2], (rangex[1] - rangex[2])-uncertaintyx, (rangex[1] - rangex[2])+uncertaintyx, colors='k', linestyles='dotted')
        plt.vlines(rangex[1] - rangex[2], (rangey[0] + rangey[2])-uncertaintyy, (rangey[0] + rangey[2])+uncertaintyy, colors='k', linestyles='dotted')
       # GWC removed 70/24 and 24/8 from the print statements on 11may26.
       # print('70/24 Uncertainty ' + title + ': '+ str(uncertaintyx))
       # print('24/8 Uncertainty ' + title + ': '+ str(uncertaintyy))
        print('Uncertaintyx ' + title + ': '+ str(uncertaintyx))
        print('Uncertaintyy ' + title + ': '+ str(uncertaintyy))
    cbar = fig.colorbar(sc, ax=fig.axes, label=physlabel)
    cbar.set_label(physlabel, fontsize=20)
    fig.savefig(fname= save_name, transparent=True)
    plt.ioff()
    plt.show()

elif plttype == 6:
    er_cutoff = .5
    hcsccolspecs=[(0,4),(5,9),(10,14),(15,23),(24,35),(36,46),(47,57),(58,64),(65,74),(75,80),(81,85),(86,94),(95,102),(103,109),(110,115),(116,121),(122,129)]
    hcscnames=["ID","DIAM","e_DIAM","MASS","e_MASS","BLUM","e_BLUM","LMRAT","e_LMRAT","TEMP","e_TEMP","LRAT","e_LRAT","TBOL","e_TBOL","SIGMA","e_SIGMA"]
    data_hcsc = pd.read_fwf("MRT-hcsc.txt",colspecs=hcsccolspecs,names=hcscnames, sep=r"\s+", skiprows=28)
    
    distcolspecs=[(0,4),(5,10),(11,16),(17,22),(23,29),(30,36),(37,48),(49,53),(54,59),(60,65),(66,70),(71,76),(77,82),(83,87),(88,92),(93,98)]
    distnames=["ID","DIST","e_DIST","DIST_C","DIST_M","e_DIST_M","STAT_M","PFAR","DIST_R1","e_DIST_R1","PINT_R1","ARM_R1","DIST_R2","e_DIST_R2","PINT_R2","ARM_R2"]
    distdata = pd.read_fwf("MRT-dist.txt",colspecs=distcolspecs,names=distnames, sep=r"\s+", skiprows = 29, usecols=["ID"] + ["DIST"])

    cordcolspecs=[(0,4),(5,14),(15,23),(24,31),(32,39),(40,47),(48,55),(56,60),(60,68),(69,77),(78,85),(86,94),(95,102),(103,110),(111,120),(121,130),(131,133),(134,136),(137,139),(140,141),(142,146),(147,148),(149,153),(154,158),(159,160)]
    cordnames=["ID","GLON","GLAT","MWPR","e_GLON","e_GLAT","e_MWPR","HRATE","F8","e_F8","F12","e_F12","F24","e_F24","F70","e_F70","N8","N12","N24","N70","f_SAT","f_MULTI","f_NOSRC","f_PCONF","f_CEXT"]
    corddata = pd.read_fwf("MRT-phot.txt",colspecs=cordcolspecs, names=cordnames, sep=r"\s+", skiprows = 39, usecols=["ID"] + ["GLON"] + ["GLAT"] + ["F8"]+["e_F8"]+["F12"]+["e_F12"]+["F24"]+["e_F24"]+["F70"]+["e_F70"])

    xmatdata = pd.read_csv("PlotMaster-10fluxes-GWC.csv", usecols= [
    "YB",
    "F160", "u_F160", "e_F160",
    "F250", "u_F250", "e_F250",
    "F350", "u_F350", "e_F350",
    "F500", "u_F500", "e_F500",
    "F870", "u_F870", "e_F870",
    "F1100", "u_F1100", "e_F1100",
    "Multiple Sources",
    "No Obvious Source 8",
    "No Obvious Source 12",
    "No Obvious Source 24",
    "No Obvious Source 70",
    "No Obvious Source 160",
    "No Obvious Source 250",
    "No Obvious Source 350",
    "No Obvious Source 500",
    "No Obvious Source 870",
    "No Obvious Source 1100",
    "Poor Confidence 8",
    "Poor Confidence 12",
    "Poor Confidence 24",
    "Poor Confidence 70",
    "Poor Confidence 160",
    "Poor Confidence 250",
    "Poor Confidence 350",
    "Poor Confidence 500",
    "Poor Confidence 870",
    "Poor Confidence 1100",
    "Very Circular",
    "RMS",
    "WISE Q",
    "WISE C,G,K",
    "CORNISH",
    "No Association"
])
    
    merged2 = pd.merge(data_hcsc, xmatdata, left_on="ID", right_on="YB", how="inner")
    merged1 = pd.merge(distdata, merged2, left_on="ID", right_on="ID", how="inner")
    merged = pd.merge(corddata, merged1, left_on="ID", right_on="YB", how="inner")
    #print("25 in xmatdata:", (xmatdata["YB"] == 25).any())
    tot_table = []
    excludeidx = []
    exclusions = [er_cutoff, ["No Obvious Source", "Poor Confidence"]]
    for i in range(len(merged)):
        for j in range(len(exclusions[1])):
            if exclusions[1][j]:
                flag = exclusions[1][j]
                if flag in merged.columns and merged[flag].iloc[i] == 1:
                    excludeidx.append(i)
    excludeidx = list(set(excludeidx))
    merged = merged.drop(index=excludeidx).reset_index(drop=True)
    table_cat = table_cat[0]
    if table_cat != "All Sources":
        merged = merged[merged[table_cat]==1].reset_index(drop=True)
    if answer == True:
        criteria = ((merged["DIST"] < dismax) & 
                    (merged["DIST"] > dismin) &
                    (merged["GLAT"] < bmax) &
                    (merged["GLAT"] > bmin) &
                    (merged["GLON"] < lmax) &
                    (merged["GLON"] > lmin))
        merged = merged.loc[criteria].reset_index(drop=True) 
    if physanswer == True:
        merged = merged.sort_values(by=physical[0], ascending=False).reset_index(drop=True)             
    for color in colorsep:
    #    HII_lst = []
    #    PNe_lst = []
        table_lst = []
        for i in range(len(merged)):
            colorx = merged[color[0]].iloc[i]
            colory = merged[color[1]].iloc[i]
            color_tot = colorx / colory
           # print(merged["YB"].iloc[i], color,color_tot, (merged["e_"+color[0]].iloc[i]+merged["e_"+color[1]].iloc[i]) / 2)
            if color[0] in ["F8","F12","F24","F70"] and color[1] in ["F8","F12","F24","F70"]:
                if merged["e_"+color[0]].iloc[i] < .5 and merged["e_"+color[1]].iloc[i] < .5:
                    table_lst.append(color_tot) 
            elif color[0] in ["F8","F12","F24","F70"] or color[1] in ["F8","F12","F24","F70"]:
                if color[0] in ["F8","F12","F24","F70"]:
                    if merged["e_"+color[0]].iloc[i] < .5:    
                        table_lst.append(color_tot)
                else: 
                    if merged["e_"+color[1]].iloc[i] < .5:    
                        table_lst.append(color_tot)
            else: 
                table_lst.append(color_tot)
        table_lst = [x for x in table_lst if not pd.isna(x)]
        if physanswer == True:
            quarter = len(table_lst) // 4
            half = len(table_lst) // 2
            threequarter = 3*len(table_lst) // 4
            if quartile_val[0] == 25:
                table_lst = table_lst[:quarter]
            elif quartile_val[0] == 50:
                table_lst = table_lst[quarter:half]
            elif quartile_val[0] == 75:
                table_lst = table_lst[half:threequarter]
            elif quartile_val[0] == 100:
                table_lst = table_lst[threequarter:]
        else:
            quar_title = "100%"
        color_ave = round(statistics.mean(table_lst),3)
        stdevtab = round(np.std(table_lst),3)
        log_color_ave = round(np.log10(color_ave), 3)
        log_stdevtab = round(np.log10(stdevtab), 3)
        #    if sign == ">":
        #        if color_tot > cutoff:
        #           HII_lst.append(color_tot)
         #       else:
         #           PNe_lst.append(color_tot)
         #   elif sign == "<":
         #       if color_tot < cutoff:
        #            HII_lst.append(color_tot)
        #        else:
         #           PNe_lst.append(color_tot)
       # HII_lst = [x for x in HII_lst if not pd.isna(x)]
       # PNe_lst = [x for x in PNe_lst if not pd.isna(x)]
      #  HII_per = round(100*len(HII_lst) / len(merged), 1)
      #  PNe_per = round(100*len(PNe_lst) // len(merged), 1)
      #  if len(HII_lst) > 0:
      #      HII_ave = round(statistics.mean(HII_lst),2)
      #  else:
      #      HII_ave = "No Value"
      #  if len(PNe_lst) > 0:
            
      #      PNe_ave = round(statistics.mean(PNe_lst),2)
      #  else:
      #      PNe_ave = "No Value"
        if table_cat == "WISE C,G,K":
            table_cat = table_cat.replace(",","")
        com_string = f"{table_cat},{color[0]}/{color[1]},{log_color_ave}\u00B1{log_stdevtab}, {len(table_lst)}, {quar_title}"
        tot_table.append(com_string)
    header = [
        "Catalog,Color,log(Avg Color),N Sources,Quartile"]
    connect = np.concatenate((header, tot_table))
    table_cat_title = table_cat_title[0]
    if physanswer == True:
        if phys_title == "Bolometric Luminosity/Mass":
            phys_title = phys_title.replace("/","_")
    if physanswer == False:
        #change do your directory
        np.savetxt(f"/Users/wadevining/YellowBall/Tables/{table_cat_title}{quar_title}.csv", connect, fmt="%s") 
    else:
        np.savetxt(f"/Users/wadevining/YellowBall/Tables/{table_cat_title}{quar_title}{phys_title}.csv", connect, fmt="%s")    

elif plttype == 7:
    catdata_all = pd.read_csv("Tables/all_sources100%.csv", header = [0])
    catdata_RMS = pd.read_csv("Tables/RMS100%.csv", header = [0])
    catdata_WISECGK = pd.read_csv("Tables/WISE_C,G,K100%.csv", header = [0])
    catdata_WISEQ = pd.read_csv("Tables/WISE Q100%.csv", header = [0])
    catdata_CORNISH = pd.read_csv("Tables/CORNISH100%.csv", header = [0])
    catdata_noasso = pd.read_csv("Tables/no_association100%.csv", header = [0])

    BLM_quar_25 = pd.read_csv("Tables/all_sources0-25%Bolometric Luminosity_Mass.csv", header = [0])
    BL_quar_25 = pd.read_csv("Tables/all_sources0-25%Bolometric Luminosity.csv", header = [0])
    BT_quar_25 = pd.read_csv("Tables/all_sources0-25%Bolometric Temperature.csv", header = [0])
    DIA_quar_25 = pd.read_csv("Tables/all_sources0-25%Diameter.csv", header = [0])
    GT_quar_25 = pd.read_csv("Tables/all_sources0-25%Greybody Temperature.csv", header = [0])
    LR_quar_25 = pd.read_csv("Tables/all_sources0-25%Luminosity Ratio.csv", header = [0])
    MA_quar_25 = pd.read_csv("Tables/all_sources0-25%Mass.csv", header = [0])
    SD_quar_25 = pd.read_csv("Tables/all_sources0-25%Surface Density.csv", header = [0])

    BLM_quar_50 = pd.read_csv("Tables/all_sources25-50%Bolometric Luminosity_Mass.csv", header = [0])
    BL_quar_50 = pd.read_csv("Tables/all_sources25-50%Bolometric Luminosity.csv", header=[0])
    BT_quar_50 = pd.read_csv("Tables/all_sources25-50%Bolometric Temperature.csv", header=[0])
    DIA_quar_50 = pd.read_csv("Tables/all_sources25-50%Diameter.csv", header=[0])
    GT_quar_50 = pd.read_csv("Tables/all_sources25-50%Greybody Temperature.csv", header=[0])
    LR_quar_50 = pd.read_csv("Tables/all_sources25-50%Luminosity Ratio.csv", header=[0])
    MA_quar_50 = pd.read_csv("Tables/all_sources25-50%Mass.csv", header=[0])
    SD_quar_50 = pd.read_csv("Tables/all_sources25-50%Surface Density.csv", header=[0])

    BLM_quar_75 = pd.read_csv("Tables/all_sources50-75%Bolometric Luminosity_Mass.csv", header=[0])
    BL_quar_75 = pd.read_csv("Tables/all_sources50-75%Bolometric Luminosity.csv", header=[0])
    BT_quar_75 = pd.read_csv("Tables/all_sources50-75%Bolometric Temperature.csv", header=[0])
    DIA_quar_75 = pd.read_csv("Tables/all_sources50-75%Diameter.csv", header=[0])
    GT_quar_75 = pd.read_csv("Tables/all_sources50-75%Greybody Temperature.csv", header=[0])
    LR_quar_75 = pd.read_csv("Tables/all_sources50-75%Luminosity Ratio.csv", header=[0])
    MA_quar_75 = pd.read_csv("Tables/all_sources50-75%Mass.csv", header=[0])
    SD_quar_75 = pd.read_csv("Tables/all_sources50-75%Surface Density.csv", header=[0])

    BLM_quar_100 = pd.read_csv("Tables/all_sources75-100%Bolometric Luminosity_Mass.csv", header=[0])
    BL_quar_100 = pd.read_csv("Tables/all_sources75-100%Bolometric Luminosity.csv", header=[0])
    BT_quar_100 = pd.read_csv("Tables/all_sources75-100%Bolometric Temperature.csv", header=[0])
    DIA_quar_100 = pd.read_csv("Tables/all_sources75-100%Diameter.csv", header=[0])
    GT_quar_100 = pd.read_csv("Tables/all_sources75-100%Greybody Temperature.csv", header=[0])
    LR_quar_100 = pd.read_csv("Tables/all_sources75-100%Luminosity Ratio.csv", header=[0])
    MA_quar_100 = pd.read_csv("Tables/all_sources75-100%Mass.csv", header=[0])
    SD_quar_100 = pd.read_csv("Tables/all_sources75-100%Surface Density.csv", header=[0])

    BLM_quar = [BLM_quar_25, BLM_quar_50, BLM_quar_75, BLM_quar_100]
    BL_quar = [BL_quar_25, BL_quar_50, BL_quar_75, BL_quar_100]
    BT_quar = [BT_quar_25, BT_quar_50, BT_quar_75, BT_quar_100]
    DIA_quar = [DIA_quar_25, DIA_quar_50, DIA_quar_75, DIA_quar_100]
    GT_quar = [GT_quar_25, GT_quar_50, GT_quar_75, GT_quar_100]
    LR_quar = [LR_quar_25, LR_quar_50, LR_quar_75, LR_quar_100]
    MA_quar = [MA_quar_25, MA_quar_50, MA_quar_75, MA_quar_100]
    SD_quar = [SD_quar_25, SD_quar_50, SD_quar_75, SD_quar_100]
    data_map = {
                "LR_quar": LR_quar,
                "BL_quar": BL_quar,
                "BT_quar": BT_quar,
                "DIA_quar": DIA_quar,
                "GT_quar": GT_quar,
                "MA_quar": MA_quar,
                "SD_quar": SD_quar,
                "BLM_quar": BLM_quar
        }
    
    catdata = [catdata_all,catdata_RMS,catdata_WISECGK,catdata_WISEQ,catdata_CORNISH, catdata_noasso]
    
    if scatopt == 1:
        yax_lst = []
        xax= []
        yax = []
        colorax = []
        for csv in catdata:
            yax_lst.extend(csv["log(Avg Color)"].tolist())
            xax.extend(csv["Color"].tolist())
            colorax.extend(csv["Catalog"].tolist())
        for num in yax_lst:
            yax.append(float(num.split("\u00B1")[0]))
        unique = sorted(set(colorax))
        color_map = {
            name: plt.cm.tab20(i / len(unique))
            for i, name in enumerate(unique)
        }

        point_colors = [color_map[name] for name in colorax]
        fig, minifig = plt.subplots(figsize=(10,7))
        sc = minifig.scatter(xax,yax,c=point_colors,s=10)
        minifig.set_title("Colors in Catalogs")
        plt.xticks(rotation=90, fontsize=12)
        legend_elements = [Line2D([0],[0],marker='o',color='w',label=name,markerfacecolor=color_map[name],markersize=6)for name in unique]
        minifig.legend(handles=legend_elements,title="Color",loc="upper left", labelspacing=.2,fontsize=8,title_fontsize=10,ncol=1)
        plt.subplots_adjust(bottom=.25)
        plt.ioff()
        plt.show()
    elif scatopt == 2:
    
        yax_lst = []
        xax= []
        yax = []
        colorax = []

        for csv in data_map[physical[0]]:
            yax_lst.extend(csv["log(Avg Color)"].tolist())
            xax.extend(csv["Quartile"].tolist())
            colorax.extend(csv["Color"].tolist())
        for num in yax_lst:
            yax.append(float(num.split("\u00B1")[0]))
        unique = sorted(set(colorax))
        color_map = {
            name: plt.cm.tab20(i / len(unique))
            for i, name in enumerate(unique)
        }

        point_colors = [color_map[name] for name in colorax]
        fig, minifig = plt.subplots(figsize=(10,7))
        sc = minifig.scatter(xax,yax,c=point_colors,s=10)
        legend_elements = [Line2D([0],[0],marker='o',color='w',label=name,markerfacecolor=color_map[name],markersize=6)for name in unique]
        minifig.legend(handles=legend_elements,title="Color",loc="center left",bbox_to_anchor=(1.02, 0.5),fontsize=6,title_fontsize=9,ncol=2)
        minifig.set_title(phys_title)
        plt.subplots_adjust(right=.75)
        plt.ioff()
        plt.show()
    
    elif scatopt == 3:
        yax_lst = []
        xax = []
        colors = ['F350/F160', 'F350/F70', 'F350/F24', 'F350/F12', 'F350/F8', 'F250/F160', 'F250/F70', 'F250/F24', 'F250/F12', 'F250/F8', 'F160/F70', 'F160/F24', 'F160/F12', 'F160/F8', 'F70/F24', 'F70/F12', 'F70/F8', 'F24/F12', 'F24/F8', 'F12/F8']
        yax = []
        catax = []
        stddev = []
        catalog_color_vals = {}
        for csv in catdata:
            xax = xax + colors
            for idx, row in csv.iterrows():
                if row["Color"] in xax:
                    val = float(row["log(Avg Color)"].split("\u00B1")[0])
                    yax_lst.append(row["log(Avg Color)"])
                    catax.append(row["Catalog"])
                    catalog_color_vals.setdefault(row["Color"], {})[row["Catalog"]] = val
        print(catalog_color_vals)
        for num in yax_lst:
            split = num.split("\u00B1")
            yax.append(float(split[0]))
        print(sorted(set(catax)))
        color_stdev = {
            color: np.std(list(cat_vals.values()))
            for color, cat_vals in catalog_color_vals.items()
                }
        color_order = sorted(color_stdev, key=color_stdev.get, reverse=True)
        color_map = {
            "All Sources": "o",
            "RMS": "s",
            "WISE CGK" : "^",
            "WISE Q": "p",
            "CORNISH": "x",
            "No Association": "d"
        }

        point_colors = [color_map[name] for name in catax]
        xax = np.array(xax)
        yax = np.array(yax)
        catax = np.array(catax)

        order_index = {c: i for i, c in enumerate(color_order)}
        y_positions = np.array([order_index[c] for c in xax])

        fig, minifig = plt.subplots(figsize=(10,7))
        minifig.set_title("Colors in Catalogs", fontsize=20)
        for name, marker in color_map.items():
            mask = catax == name
            if mask.any():
                minifig.scatter(yax[mask], y_positions[mask], marker=marker, s=25, label=name)
        plt.xticks(fontsize=15)
        minifig.set_yticks(range(len(color_order)))
        minifig.set_yticklabels(color_order, fontsize=15)
        minifig.invert_yaxis()
        minifig.legend(title="Catalog", loc="upper right", labelspacing=0.2,
               fontsize=11, title_fontsize=12, ncol=1)
        plt.subplots_adjust(bottom=.20)
        plt.ioff()
        plt.show()
    
    elif scatopt == 4:
        yax_lst = []
        xax= []
        yax = []
        catax = []
        for csv in data_map[physical[0]]:
            yax_lst.extend(csv["log(Avg Color)"].tolist())
            xax.extend(csv["Color"].tolist())
            catax.extend(csv["Quartile"].tolist())
        for num in yax_lst:
            yax.append(float(num.split("\u00B1")[0]))
        print(sorted(set(catax)))
        color_map = {
            " 0-25%": "red",
            " 25-50%": "green",
            " 50-75%" : "black",
            " 75-100%": "blue",
        }

        point_colors = [color_map[name] for name in catax]

        fig, minifig = plt.subplots(figsize=(14,7))
        sc = minifig.scatter(xax,yax,c=point_colors,s=10)
        plt.title(phys_title)
        plt.xticks(rotation=90, fontsize=15)

        '''
        target = {" 0-25%"," 75-100%"}
        filtered = [(c,v,q) for c,v,q in zip(xax,yax,catax) if q in target]
        color_vals = {}
        for c,v,q in filtered:
            color_vals.setdefault(c,{" 0-25%":[]," 75-100%":[]})[q].append(v)
        diffs = []
        for c,vals in color_vals.items():
            if vals[" 0-25%"] and vals[" 75-100%"]:
                avg_low = sum(vals[" 0-25%"])/len(vals[" 0-25%"])
                avg_high = sum(vals[" 75-100%"])/len(vals[" 75-100%"])
                diffs.append((c,avg_high-avg_low,avg_low,avg_high))
        diffs_sorted = sorted(diffs,key=lambda row:row[1],reverse=True)
        print(f"\n=== {phys_title}: 75-100% minus 0-25% (ranked high to low) ===")
        print(f"{'Rank':<6}{'Color':<25}{'Diff':<12}{'Avg 0-25':<12}{'Avg 75-100':<12}")
        for rank,(color,diff,avg_low,avg_high) in enumerate(diffs_sorted,start=1):
            print(f"{color:<25}")
        '''

        legend_elements = [Line2D([0],[0],marker='o',color='w',label=name,markerfacecolor=color_map[name],markersize=6)for name in sorted(set(catax))]
        minifig.legend(handles=legend_elements,title="Color",loc="center left",bbox_to_anchor=(1.02, 0.5),fontsize=10,title_fontsize=12,ncol=1)
        plt.subplots_adjust(right=.75, bottom=.20)
        plt.ioff()
        plt.show()