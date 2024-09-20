import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#  FUNCTIONAL PLOT #####################################################################################################

#  This is a simple plot************************************************************************************************

#  Creating x and y axes
x1 = np.linspace(0, 5, 10)  # includes 5
y1 = x1 ** 2  # simple exponential function
plt.plot(x1, y1, label='x/x^2', marker='o')  # This creates a line in the plot
plt.plot(y1, x1, label='x^2/x', marker='*')  # This creates a second line in the plot
plt.title('Days Squared Chart')
plt.xlabel('Days')
plt.ylabel('Days Squared')
plt.legend(
    loc=0)  # Adds legend i.e., line labels; 0 = best place (goto: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)
for i, j in zip(x1, y1):
    plt.text(i + 1, j,
             '(%.2f, %.2f)' % (i, j))  # %.2f --> float point limited to 2 decimals; %s --> string; %i --> Integer
    plt.text(j, i - 1, '(%.2f, %.2f)' % (j, i))
plt.show()
plt.close()
#  Here plt.plot() can function with just one list like plt.plot([1, 2, 3])
#  python will consider the passed list as y-axis and will then assume x-axis values

#  END OF FUNCTIONAL PLOT ##############################################################################################


#  MULTIPLE PLOT #######################################################################################################

plt.subplot(1, 2, 1)  # creates subplots, (1-row, 2-columns/plots, 1st plot selected)
plt.plot(x1, y1, 'r')  # 'r' is the colour of the line
plt.plot(y1, x1, 'g')  # 'g' is the colour of the line
plt.title('Red Plot')
plt.xlabel('Days')
plt.ylabel('Days Squared')
plt.subplot(1, 2, 2)  # (1-row, 2-columns/plots, 2nd plot selected)
plt.plot(x1, y1, 'b')  # 'b' is the colour of the line
plt.plot(y1, x1, '')  # 'g' is the colour of the line
plt.title('Blue Plot')
plt.xlabel('Days')
plt.ylabel('Days Squared')
plt.show()
plt.close()

#  END OF MULTIPLE PLOT ################################################################################################


#  FIGURE OBJECTS ######################################################################################################

# creating and defining a figure. fig size indicates the size of the figure in b*h fashion
# Figure is nothing but a canvas, on which we want to plot, single, multiple plots
fig1 = plt.figure(figsize=(5, 4), dpi=100)  # You don't have to pass arguments here. However, if you have screen space
# constraint, you can prove these arguments.

# now create axes i.e., a plot with the position and amount of canvas/figure we want to use
# ([left, bottom, width and height])- values range from 0 to 1

axes1 = fig1.add_axes([0.05, 0.05, 0.9, 0.9])
axes1.set_xlabel('Days')
axes1.set_ylabel('Days Squared')
axes1.set_title('Days Squared Chart')
axes1.plot(x1, y1, label='x/x^2')
axes1.plot(y1, x1, label='x^2/x')
axes1.plot(x1 * 0.5, y1, label='x*0.5/x')
axes1.legend(loc=0)

# now create 2nd axes i.e., another plot with the position and amount of canvas (figure) we want to use.
# this enables creativity in visualization

axes2 = fig1.add_axes([0.45, 0.45, 0.4, 0.3])
axes2.set_xlabel('Days')
axes2.set_ylabel('Days Squared')
axes2.set_title('Days Squared Chart2')
axes2.plot(x1, y1, label='x/x^2')
axes2.plot(y1, x1, label='x^2/x')
axes2.plot(x1 * 0.5, y1, label='x*0.5/x')
axes2.legend(loc=0)
axes2.text(0, 20, 'Message')  # These are co-ordinates at which the message will be displayed
# plt.show()
plt.close()

#  END OF FIGURE OBJECTS ###############################################################################################


#  SUB PLOTS ###########################################################################################################

#  Just like above, but more elegant way when you know the number of axes you need

fig2, axes3 = plt.subplots(figsize=(6, 4), nrows=3, ncols=3)
plt.tight_layout()  # this will sort plots automatically of there are overlapping plots (more-or-less)
axes3[1][1].set_title('Plot2')
axes3[1][1].set_xlabel('X')
axes3[1][1].set_ylabel('X Squared')
axes3[1][1].plot(x1, y1, label='x to x^2')
axes3[1][1].legend(loc=0)
plt.show()
plt.close()

#  END OF SUB PLOTS ####################################################################################################


#  APPEARANCE OPTIONS ##################################################################################################

# Default colors (b: blue, g: green, r: red, c: cyan, m: magenta,
# y: yellow, k: black, w: white)

# color="0.75" creates a 75% gray
# You can use hexcodes color="#eeefff"
# You can use color names found next like this color="burlywood" (https://en.wikipedia.org/wiki/Web_colors)

# alpha defines the percentage of opacity

# The default line width is 1, so to double it put in 2 and so forth

# There are many line styles
# matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html
# You can also provide a sample like '-.'

# Markers can mark your provided points on the graph
# https://matplotlib.org/3.3.0/api/markers_api.html
# You can change the markersize as well

# markerfacecolor changes the marker fill color
# markeredgecolor changes the marker stroke color
# markeredgewidth changes the markers stroke size

fig3 = plt.figure()
plt.tight_layout()
axes4 = fig3.add_axes([0.05, 0.06, 0.9, 0.9])
axes4.set_title('Appearance')
axes4.set_xlabel('X')
axes4.set_ylabel('X Squared')

#  Here 'color=' is plot line color; 'alpha=' is transparency of the line; 'marker=' is type of dot;
#  'markersize=' size of the marker and so on.

axes4.plot(x1, y1, color='navy', alpha=0.75, lw=2, ls='-.', marker='o', markersize='5',
           markerfacecolor='r', markeredgecolor='b', markeredgewidth=1, label='x to x^2')

# if I want a zoomed in view of the plot
axes4.set_xlim([0, 3])
axes4.set_ylim([0, 8])

# if I want grid; 'dashes=' (points, 2 spaces, 1 point, 2 spaces). Actually, it does not matter as this defines the
# grid style. if I don't give this, the grid will be solid
axes4.grid(True, color='0.6', dashes=(2, 2, 1, 2))

# if I want a color in the background
axes4.set_facecolor('#FAEBD7')
axes4.legend(loc=0)
# plt.show()
plt.close()

#  END OF APPEARANCE OPTIONS ###########################################################################################


#  WORKING WITH PANDAS #################################################################################################

path = f'C:\\Users\\vedap\\Jupyter_Practice\\icecreamsales.csv'
ics_df = pd.read_csv(path)
ics_df = ics_df.sort_values(by='Temperature')

np_arr = ics_df.values
x2 = np_arr[:, 0]  # all rows, column 0
y2 = np_arr[:, 1]  # all rows, column 1

fig4 = plt.figure(figsize=(6, 4))
axes5 = fig4.add_axes([0.05, 0.09, 0.9, 0.9])
axes5.set_title('Temperature vs Ice Cream Sales')
axes5.set_xlabel('Temperature')
axes5.set_ylabel('Ice Cream Sales')
axes5.plot(x2, y2, label='Sales')
axes5.legend(loc=0)

# The following is an advanced version of plt.text
# 'xytext=' will tell where to place the text
# 'xy=' will tell where to place arrowprops
# 'shrink=' will tell at what distance the arrow-pointer needs to be from the point-on-the-plot you want to point-out ;-)

axes5.annotate('Good Month', xytext=(60, 528), xy=(83, 536),
               arrowprops=dict(facecolor='green', shrink=0.03))

# if I want to add bars below the line (this is dirty, just choose one)
# plt.bar(x2, y2)

# plt.show()
plt.close()

# END OF WORKING WITH PANDAS ###########################################################################################


#  TeX MARKUP ##########################################################################################################

# to add special characters / math formulas / symbols
fig5 = plt.figure(figsize=(6, 4))
axes6 = fig5.add_axes([0.05, 0.09, 0.9, 0.9])

axes6.text(0, 23, r'$\alpha \beta \sigma \omega \epsilon \mu \pi \theta \lambda$')

axes6.text(0, 18, r'$\delta_i \gamma^{ij} \sum_{i=0}^\infty x_i \frac{3}{4}$')
# delta_i --> delta symbol with subscript i
# sum_{i=0}^\infty x_i --> sum symbol, i = 0 to infinity x subscript i

axes6.text(0, 13, r'$\frac{8 - \frac{x}{5}} {8} \sqrt{9} \ sin{\pi} \sqrt[3]{8} \acute a \div$')
axes6.text(0, 8, r'$\bar a  \hat a  \tilde a  \vec a  \overline {a}    \lim_{x \to 2}  f(x) = 5$')
axes6.text(0, 3, r'$\geq  \leq  \ne$')

axes6.plot(x1, y1)
# plt.show()
plt.close()

# END OF TeX MARKUP ####################################################################################################

# ######################################################################################################################
# ************************************************** TYPES OF CHARTS ***************************************************
# ######################################################################################################################

#  HISTOGRAM ###########################################################################################################

# # Roll 2 6 sided dies get the sum and plot the histogram
arr1 = np.random.randint(1, 7, 5000)  # 1 to 6 (not including 7); 5000 numbers
arr2 = np.random.randint(1, 7, 5000)
arr3 = arr1 + arr2
counts = plt.hist(arr3, bins=11, density=True, stacked=True, color='orange')
# counts = plt.hist(arr3, bins=11, density=True, stacked=True, cumulative=True, histtype='step', orientation='horizontal')

# plt.show()
plt.close()

# Bins represent the number of options available 2 through 12 = 11
# Density returns the frequency of each bin
# Range gets tuple with bin range interested in
# cumulative=True use a cumulative distribution
# histtype='step' genrates a line plot
# orientation='horizontal'
# color='orange' change bar color

# END OF HISTOGRAM #####################################################################################################


#  BAR CHARTS ##########################################################################################################

# Where France gets its electricity form?

x = ['Nuclear', 'Hydro', 'Coal', 'Gas', 'Solar', 'Wind', 'Other']
per1 = [71, 10, 3, 7, 2, 4, 3]
variance = [8, 3, 1, 3, 1, 2, 1]
plt.bar(x, per1, color='purple', yerr=variance)
# plt.barh(.....) # horizontal bar chart
plt.show()
plt.close()

# Show percentages of males & females in engineering

m_eng = (76, 85, 86, 88, 93)
f_eng = (24, 15, 14, 12, 7)

spc_m = np.arange(5)  # This is for x-axis (could be branches of engineering)
spc_f = np.arange(5) + 0.45
spc = spc_m + 0.225
plt.bar(spc_m, m_eng, width=0.45, label='Male', edgecolor='k')
plt.bar(spc_f, f_eng, width=0.45, label='Female', edgecolor='k')

plt.xticks(spc, ('Aero', 'Chem', 'Civil', 'Elec', 'Mech'))
# plt.show()
plt.close()

# Plot teachers by sex

t_type = ['Kind', 'Elem', 'Sec', 'Spec']
m_teach = np.array([2, 20, 44, 14])
f_teach = np.array([98, 80, 56, 86])
ind = [x for x, _ in enumerate(t_type)]  # enumerate will return tuple with (index , value)

plt.bar(ind, m_teach, width=0.45, label='Male', bottom=f_teach)
plt.bar(ind, f_teach, width=0.45, label='Female')

# 'bottom=' for stacked barplots. bottom of the plot is top of another plot

plt.legend(loc='lower right')
# plt.show()
plt.close()

# END OF BAR CHARTS ####################################################################################################

#  PIE CHARTS ##########################################################################################################

import random

fig6 = plt.figure(figsize=(8, 5))
axes7 = fig6.add_axes([0.05, 0.09, 0.9, 0.9])

# Create a pie chart of the number of Pokemon by type

types = ['Water', 'Normal', 'Flying', 'Grass', 'Psychic', 'Bug', 'Fire', 'Poison',
         'Ground', 'Rock', 'Fighting', 'Dark', 'Steel', 'Electric', 'Dragon', 'Fairy',
         'Ghost', 'Ice']
poke_num = [133, 109, 101, 98, 85, 77, 68, 66, 65, 60, 57, 54, 53, 51, 50, 50, 46, 40]

# I have to generate randoom colours to fit each Pokemon

colors = []
for i in range(len(types)):
    rgb = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    colors.append(rgb)

# random.uniform(0, .5) will generate value between 0 and 0.5. This number will then be used to define the color in
# rgb format. uniform will return floating point numbers
# 0 to 0.5 --> dark colors and 0.5 to 1.0 --> light colors

explode = [0] * 18  # creates a list with 18 zeros
explode[0] = 0.2  # this will change the list's first value to 0.2

wedges, texts, autotexts = plt.pie(poke_num, explode=explode, labels=types,
                                   colors=colors, autopct='%1.0f%%', shadow=True,
                                   startangle=140, textprops=dict(color='w'))

plt.legend(wedges, types, loc='right', bbox_to_anchor=(1, 0.1, 0.2, 0.7))
# plt.show()
plt.close()
# Provide values, what to explode and by how much, labels, colors, pct for values,
# whether to shadow, amount to rotate pie, pie text color

# END OF PIE CHARTS ####################################################################################################

#  TIME SERIES #########################################################################################################
path = f'C:\\Users\\vedap\\Jupyter_Practice\\GOOG.csv'
goog_data = pd.read_csv(path)
goog_data_np = goog_data.to_numpy()  # no need to convert ot numpy array if you want to use pandas
goog_cp = goog_data_np[:, 4]  # all rows in 5th column (index starts at 0)
holidays = [datetime.datetime(2020, 5, 25), datetime.datetime(2020, 8, 19)]
date_arr = pd.bdate_range(start='5/20/2020', end='8/19/2020', freq='C',
                          holidays=holidays)  # freq='C' every 15 days
date_arr_np = date_arr.to_numpy()

fig7 = plt.figure(figsize=(8, 5))
axes8 = fig7.add_axes([0.07, 0.1, 0.9, 0.9])
axes8.plot(date_arr_np, goog_cp)
plt.show()
plt.close()

# END OF TIME SERIES ###################################################################################################


#  TABLES ##############################################################################################################

goog_data['Open'] = pd.Series([round(val, 2) for val in goog_data['Open']], index=goog_data.index)
goog_data['High'] = pd.Series([round(val, 2) for val in goog_data['High']], index=goog_data.index)
goog_data['Low'] = pd.Series([round(val, 2) for val in goog_data['Low']], index=goog_data.index)
goog_data['Close'] = pd.Series([round(val, 2) for val in goog_data['Close']], index=goog_data.index)
goog_data['Adj Close'] = pd.Series([round(val, 2) for val in goog_data['Adj Close']], index=goog_data.index)

stk_data = goog_data[-5:]

# Defining headers

col_head = ('Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume')
stk_data_np = stk_data.to_numpy()

# Add padding around cells in table

plt.figure(linewidth=2, tight_layout={'pad': 0.5}, figsize=(5, 3))

# Get rid of axes and plot box

axes9 = plt.gca
plt.box(on=None)
plt.axis('off')

# np.full returns an array filled with 0.1
# cm is a colormap object we are using to use a default blue color
# matplotlib.org/3.1.0/tutorials/colors/colormaps.html

ccolors = plt.cm.Blues(np.full(len(col_head), 0.2))
the_table = plt.table(cellText=stk_data_np, loc='center', colLabels=col_head,
                      colColours=ccolors, rowLoc='center', colLoc='center')

the_table.set_fontsize(14)
# plt.show()
plt.close()

# END OF TABLES ########################################################################################################


#  SCATTER PLOT ########################################################################################################

# Country array
cnt_arr = np.array(['Australia', 'Brazil', 'Canada', 'Chile', 'France', 'Germany', 'Greece',
                    'Iceland', 'India', 'Iran', 'Italy', 'Mexico', 'New Zealand', 'Nigeria',
                    'Norway', 'Pakistan', 'Peru', 'Russia', 'Saudi Arabia', 'Singapore',
                    'South Africa', 'Spain', 'Sweden', 'Turkey', 'UK', 'US'])
# Death rate per 100k Coronavirus
dr_arr = np.array([1.8, 53, 24.5, 56.5, 45.4, 11.2, 2.2,
                   2.8, 4, 24.6, 58.6, 46.3, .5, .5,
                   4.9, 2.9, 83.3, 11, 10.4, .5,
                   21.5, 61.6, 56.9, 7.3, 62.4, 52.9])
# Daily confirmed cases (Tests)
test_arr = np.array([110, 7197, 600, 1862, 1636, 1103, 35,
                     10, 295, 1658, 1226, 2490, 8, 243,
                     48, 1395, 1101, 4447, 1443, 280,
                     2830, 1602, 447, 1205, 1546, 24988])

# Dot size Confirmed cases
cc_arr = np.array([24236, 3456652, 125408, 390037, 256534, 229706, 7684,
                   2035, 2836925, 350279, 255278, 537031, 1654, 50488,
                   10162, 290445, 549321, 935066, 302686, 56031,
                   596060, 370867, 85411, 253108, 323008, 5529824])

cc_arr_shrinked = cc_arr / 1000
color_arr = np.random.rand(26)
plt.title('Death Rate per 100k vs Confirmed Cases')
plt.xlabel('Death Rate per 100k')
plt.ylabel('Confirmed Cases')
plt.scatter(dr_arr, test_arr, s=cc_arr_shrinked, c=color_arr, alpha=0.5)
# plt.show()
plt.close()
# 's=' --> size of the dots
# 'c=' --> color array
# 'alpha=' --> Transparancy


# END OF SCATTER PLOT ##################################################################################################

#  3D SURFACE ##########################################################################################################

fig8 = plt.figure(figsize=(8, 5))
axes10 = fig8.add_axes([0.05, 0.1, 0.9, 0.9], projection='3d')
# 'projection='3d'' --> inititalizing a 3d figure

z3 = 15 * np.random.random(100)  # generates random 100 numbers between 0 and 1 (not including)
x3 = np.sin(z3) * np.random.random(100)
y3 = np.sin(z3) * np.random.random(100)


# axes10.scatter3D(x3, y3, z3, c=z3, cmap='Blues')
# This prints 3D scatter plot. Notice x, y, z are passed; 'cmap=' color map.
# cmap supported values are:
# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
# 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges',
# 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG',
# 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
# 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds',
# 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r',
# 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn',
# 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool',
# 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth',
# 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow',
# 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r',
# 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma',
# 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
# 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10',
# 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo',
# 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter',
# 'winter_r'

def get_z(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x4 = np.linspace(-6, 6, 30)
y4 = np.linspace(-6, 6, 30)

# np.linspace (start= -6, stop= 6, number= 30), including -6 and 6

x4, y4 = np.meshgrid(x4, y4)
z4 = get_z(x4, y4)
axes10.view_init(45, 55)

# initial view angle (Set the elevation and azimuth of the axes.)

# axes10.contour3D(x4, y4, z4, 100, cmap='Blues')
# This prints 3D contour plot. Notice x, y, z are passed; 'cmap=' color map.
axes10.set_xlabel('X')
axes10.set_ylabel('Y')
axes10.set_zlabel('Z')

# axes10.plot_wireframe(x4, y4, z4, cmap='Blues')
# This prints 3D wireframe plot. Notice x, y, z are passed; 'cmap=' color map.

axes10.plot_surface(x4, y4, z4, cmap='Blues', rstride=1, cstride=1,
                    edgecolor='none')
# plt.show()
plt.close()

# END OF 3D SURFACE ####################################################################################################


# MATPLOTLIB FINANCE ###################################################################################################

import mplfinance as mpf

goog_data = pd.read_csv(path, index_col=0, parse_dates=True)
goog_data.index.name = 'Date'
mpf.plot(goog_data, type='candle', mav=(3, 5, 7), volume=True, show_nontrading=True)
# this will plot dates on x-axis and price on y-axis
# type= line, ohlc etc.
# mav= moving average of x number of days. if mav=4, the line will be plotted tracing average values of last 4 days prices.
# mav= can accept multiple numbers (the tuple needs to be either all odd or even numbers)
# mav = multiple numbers will plot multiple lines based on number of days selected.
# volume=True --> include volume column in y-axis.
# show_nontrading=True --> weekend or holiday were trading did not occur. default->False

# plt.show()
plt.close()

# END OF MATPLOTLIB FINANCE ############################################################################################

#   HEATMAPS ###########################################################################################################

# A heatmap is a color coded representation of data from a 2D list
symptoms = ["Coronavirus", "Influenza", "Pneumonia", "Dyspnea"]
dates = ["Jun28", "Jul05", "Jul12", "Jul19", "Jul26", "Aug02", "Aug09", "Aug16", "Aug21"]
symp_per = np.array([[5.2, 5.5, 5.7, 5.6, 5.3, 5.1, 5.0, 4.9, 5.3],
                     [3.5, 4.0, 4.3, 3.9, 3.5, 3.2, 2.7, 2.2, 2.0],
                     [1.8, 2.2, 2.3, 2.2, 2.1, 1.9, 1.7, 1.4, 1.3],
                     [1.0, 1.1, 1.1, 1.0, 0.9, 0.8, 0.8, 0.8, 0.7]])

fig9, axes11 = plt.subplots()

axes11.imshow(symp_per, cmap='Reds')
#
# Creates an image from a 2-dimensional numpy array. The image will have one square for each element of the array.
# The color of each square is determined by the value of the corresponding array element and
# the color map used by imshow().

axes11.set_xticks(np.arange(len(dates)))  # in order to generate tables, we need only sequential x- and y-axes
axes11.set_yticks(np.arange(len(symptoms)))
axes11.set_xticklabels(dates)
axes11.set_yticklabels(symptoms)

plt.setp(axes11.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
plt.setp(axes11.get_yticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(len(symptoms)):
    for j in range(len(dates)):
        text = axes11.text(j, i, symp_per[i, j], ha='center', va='center', color='k',
                           fontweight='bold')

        # this adds text and assigns properties (e.g., color='k' / 'w' is font color
        # symp_per[i, j] --> same as symp_per[i][j]

# plt.show()
plt.close()

# # END OF HEATMAPS ####################################################################################################


#  SAVE VISUALIZATION TO A FILE ########################################################################################

fig1.savefig('Fig1')
fig2.savefig('Fig2')
fig3.savefig('Fig3')
fig4.savefig('Fig4')
fig5.savefig('Fig5')
fig6.savefig('Fig6')
fig7.savefig('Fig7')

# END OF SAVE VISUALIZATION TO A FILE ##################################################################################

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
########################################################################################################################
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  Creating a template for the heatmap
vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max()) / 2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


fig, ax = plt.subplots()

im, cbar = heatmap(harvest, vegetables, farmers, ax=ax,
                   cmap="YlGn", cbarlabel="harvest [t/year]")
texts = annotate_heatmap(im, valfmt="{x:.1f} t")

fig.tight_layout()
plt.show()
