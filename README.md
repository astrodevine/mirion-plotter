The most up-to-date variant of Maya’s code is make_plots-10fluxes-GWC.py, which can be used with the input file PlotMaster-10fluxes-GWC.csv to create histograms and color-color plots for any of the 45 combinations that can be made from the 8, 12, 24, 70, 160, 250, 350, 500, 870, & 1100 um fluxes. I adjusted the sizes of the color selection boxes, but not the font sizes in the actual plots (no big deal there.) 

Note - I created columns for the Herschel fractional flux errors (‘e_’)  from the ratio of the flux uncertainties (‘u_’, the ‘D…’ columns in the Herschel catalog) to fluxes at each wavelength.

I am running this code using Spyder 5.5.1, python 3.11.7, matplotlib 3.10.0, pandas 2.3.1, and seaborn 0.13.2.

NOTE: The current PlotMaster is dated 5/18/26. Maya pointed out a problem with the previous version (the u_F24 column was incorrect and identical to the u_F70 column). This seems to have fixed the problem with the uncertainty calculations.


Vining additions:

Code now needs data tables to run:
MRT-dist.txt
MRT-hcsc.txt
MRT-phot.txt
PlotMaster-10fluxes-GWC.csv

The program now includes a physical property histogram option. All graphs now can have a parameter of distance. The cutoff was changed so it has to be specified. There is a failsafe that restarts the program in the event that there is no data points to plot. 

The color color plot can be plotted displaying a physical property through the color of the point. 
The physical histogram is overplotted on all sources but both follow the same parameters. 
