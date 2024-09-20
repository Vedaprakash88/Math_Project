# 3. Plotting for Exploratory data analysis (EDA)

# (3.1) Basic Terminology


## Iris Flower dataset


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statsmodels import robust

'''downlaod iris.csv from https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'''
# Load Iris.csv into a pandas dataFrame.
iris = pd.read_csv("D:\\6. STUDY MATERIAL\\CSE\\Projects\\Python\\jupyter_legacy\\iris.csv")

# (Q) how many data-points and features?
print(iris.shape)
# (Q) What are the column names in our dataset?
print(iris.columns)
# (Q) How many data points for each class are present?
# (or) How many flowers for each species are present?

iris["species"].value_counts()
# balanced-dataset vs imbalanced datasets
# Iris is a balanced dataset as the number of data points for every class is 50.

# (3.2) 2-D Scatter Plot
# 2-D scatter plot:
# ALWAYS understand the axis: labels and scale.

iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()

# cannot make much sense out it.
# What if we color the points by thier class-label/flower-type.
# 2-D Scatter plot with color-coding for each flower type/class.
# Here 'sns' corresponds to seaborn. 
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue="species", height=4) \
    .map(plt.scatter, "sepal_length", "sepal_width") \
    .add_legend()
plt.show()

# Notice that the blue points can be easily seperated 
# from red and green by drawing a line. 
# But red and green data points cannot be easily seperated.
# Can we draw multiple 2-D scatter plots for each combination of features?
# How many cobinations exist? 4C2 = 6.


## 3D Scatter plot


#  (3.3) Pair-plot
# pairwise scatter plot: Pair-Plot
# Dis-advantages: 
##Can be used when number of features are high.
##Cannot visualize higher dimensional patterns in 3-D and 4-D. 
# Only possible to view 2D patterns.
plt.close()
sns.set_style("whitegrid")
sns.pairplot(iris, hue="species", height=4)
plt.show()
# NOTE: the diagnol elements are PDFs for each feature. PDFs are expalined below.


# (3.4) Histogram, PDF, CDF
# What about 1-D scatter plot using just one feature?
# 1-D scatter plot of petal-length
import numpy as np

iris_setosa = iris.loc[iris["species"] == "setosa"]
iris_virginica = iris.loc[iris["species"] == "virginica"]
iris_versicolor = iris.loc[iris["species"] == "versicolor"]
# print(iris_setosa["petal_length"])
plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_setosa['petal_length']), '*')
plt.plot(iris_versicolor["petal_length"], np.zeros_like(iris_versicolor['petal_length']), 'o')
plt.plot(iris_virginica["petal_length"], np.zeros_like(iris_virginica['petal_length']), '+')

plt.show()
# Disadvantages of 1-D scatter plot: Very hard to make sense as points
# are overlapping a lot.
# Are there better ways of visualizing 1-D scatter plots?
sns.FacetGrid(iris, hue="species", height=5) \
    .map(sns.histplot, "petal_length") \
    .add_legend()
plt.show()

sns.FacetGrid(iris, hue="species") \
    .map(sns.histplot, "petal_width") \
    .add_legend()
plt.show()
sns.FacetGrid(iris, hue="species") \
    .map(sns.histplot, "sepal_length") \
    .add_legend()
plt.show()
sns.FacetGrid(iris, hue="species", height=5) \
    .map(sns.histplot, "sepal_width") \
    .add_legend()
plt.show()
# Histograms and Probability Density Functions (PDF) using KDE
# How to compute PDFs using counts/frequencies of data points in each window.
# How window width effects the PDF plot.


# Interpreting a PDF:
## why is it called a density plot?
## Why is it called a probability plot?
## for each value of petal_length, what does the value on y-axis mean?
# Notice that we can write a simple if..else condition as if(petal_length) < 2.5 then flower type is setosa.
# Using just one feature, we can build a simple "model" suing if..else... statements.

# Disadv of PDF: Can we say what percentage of versicolor points have a petal_length of less than 5?

# Do some of these plots look like a bell-curve you studied in under-grad?
# Gaussian/Normal distribution.
# What is "normal" about normal distribution?
# e.g: Hieghts of male students in a class.
# One of the most frequent distributions in nature.


# Need for Cumulative Distribution Function (CDF)
# We can visually see what percentage of versicolor flowers have a 
# petal_length of less than 5?
# How to construct a CDF?
# How to read a CDF?

# Plot CDF of petal_length

counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10,
                                 density=True)
pdf = counts / (sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=20,
                                 density=True)
pdf = counts / (sum(counts))
plt.plot(bin_edges[1:], pdf)

plt.show()

# Need for Cumulative Distribution Function (CDF)
# We can visually see what percentage of versicolor flowers have a 
# petal_length of less than 1.6?
# How to construct a CDF?
# How to read a CDF?

# Plot CDF of petal_length

counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10,
                                 density=True)
pdf = counts / (sum(counts))
print(pdf)
print(bin_edges)

# compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

plt.show()
# Plots of CDF of petal_length for various types of flowers.

# Misclassification error if you use petal_length only.

counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10,
                                 density=True)
pdf = counts / (sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

# virginica
counts, bin_edges = np.histogram(iris_virginica['petal_length'], bins=10,
                                 density=True)
pdf = counts / (sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

# versicolor
counts, bin_edges = np.histogram(iris_versicolor['petal_length'], bins=10,
                                 density=True)
pdf = counts / (sum(counts))
print(pdf)
print(bin_edges)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

plt.show()

# (3.5) Mean, Variance and Std-dev
# Mean, Variance, Std-deviation,
print("Means:")
print(np.mean(iris_setosa["petal_length"]))
# Mean with an outlier.
print(np.mean(np.append(iris_setosa["petal_length"], 50)))
print(np.mean(iris_virginica["petal_length"]))
print(np.mean(iris_versicolor["petal_length"]))

print("\nStd-dev:")
print(np.std(iris_setosa["petal_length"]))
print(np.std(iris_virginica["petal_length"]))
print(np.std(iris_versicolor["petal_length"]))

# (3.6) Median, Percentile, Quantile, IQR, MAD
# Median, Quantiles, Percentiles, IQR.
print("\nMedians:")
print(np.median(iris_setosa["petal_length"]))
# Median with an outlier
print(np.median(np.append(iris_setosa["petal_length"], 50)))
print(np.median(iris_virginica["petal_length"]))
print(np.median(iris_versicolor["petal_length"]))

print("\nQuantiles:")
print(np.percentile(iris_setosa["petal_length"], np.arange(0, 100, 25)))
print(np.percentile(iris_virginica["petal_length"], np.arange(0, 100, 25)))
print(np.percentile(iris_versicolor["petal_length"], np.arange(0, 100, 25)))

print("\n90th Percentiles:")
print(np.percentile(iris_setosa["petal_length"], 90))
print(np.percentile(iris_virginica["petal_length"], 90))
print(np.percentile(iris_versicolor["petal_length"], 90))



print("\nMedian Absolute Deviation")
print(robust.mad(iris_setosa["petal_length"]))
print(robust.mad(iris_virginica["petal_length"]))
print(robust.mad(iris_versicolor["petal_length"]))

# (3.7) Box plot and Whiskers

# Box-plot with whiskers: another method of visualizing the  1-D scatter plot more intuitivey.
# The Concept of median, percentile, quantile.
# How to draw the box in the box-plot?
# How to draw whiskers: [no standard way] Could use min and max or use other complex statistical techniques.
# IQR like idea.

# NOTE: IN the plot below, a technique call inter-quartile range is used in plotting the whiskers.
# Whiskers in the plot below donot correposnd to the min and max values.

# Box-plot can be visualized as a PDF on the side-ways.

sns.boxplot(x='species', y='petal_length', data=iris)
plt.show()

# (3.8) Violin plots
# A violin plot combines the benefits of the previous two plots 
# and simplifies them

# Denser regions of the data are fatter, and sparser ones thinner 
# in a violin plot

sns.violinplot(x="species", y="petal_length", data=iris, size=8)
plt.show()

# (3.9) Summarizing plots in english
# (3.10) Univariate, bivariate and multivariate analysis.


## Def: Univariate, Bivariate and Multivariate analysis.


# (3.11) Multivariate probability density, contour plot.

# 2D Density plot, contors-plot
sns.jointplot(x="petal_length", y="petal_width", data=iris_setosa, kind="kde")
plt.show()

# (3.12) Exercise:

iris_virginica_SW = iris_virginica.iloc[:, 1]
iris_versicolor_SW = iris_versicolor.iloc[:, 1]

from scipy import stats

stats.ks_2samp(iris_virginica_SW, iris_versicolor_SW)

x = stats.norm.rvs(loc=0.2, size=10)
stats.kstest(x, 'norm')

x = stats.norm.rvs(loc=0.2, size=100)
stats.kstest(x, 'norm')

x = stats.norm.rvs(loc=0.2, size=1000)
stats.kstest(x, 'norm')
