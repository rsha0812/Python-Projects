# -*- coding: utf-8 -*-
"""DataVisualisation of Weather Reporting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1isWz6CQs0IE8NqDew1DVX27sUkw15l1_
"""

!pip install matplotlib

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd

#Raw Data
df1 = pd.read_csv("/content/sample_data/Weather Mentoring.csv")
print(df1)

#Data Info after Data Cleaning
df = pd.read_csv("/content/sample_data/Main Weather Data Reportnew.csv")
print(df)

"""#Plotting Graph"""

# Plotting the graph#January
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [-4.1708,2.386,-2.0752,-3.67736,-4.308,-2.1939,-1.961,-1.7551,0.24792,-0.7825,-3.02]
y2 = [0.834,0.81358,0.8195,0.8675,0.8759,0.922,0.797,0.883,0.8463,0.831,0.865]
fig1 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of January")
fig1.savefig('Januarydata.png')

#February Data
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [-2.986,2.625,1.903,-1.645,-1.679,-2.852,-8.829,0.4193,2.7207,0.003,4.1406]
y2 = [0.843,0.815,0.682,0.821,0.851,0.854,0.762,0.869,0.8123,0.8034,0.836]
fig2 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of February")

#Saving Figure

fig2.savefig('Februarydata.png')

#March-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [7.182,7.182,5.008,4.258,4.587,4.572,6.585,1.966,8.400,5.4272,5.8875]
y2 = [0.713,0.7136,0.668,0.968,0.669,0.782,0.5366,0.5366,0.6406,0.6698,0.76514]
fig3 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of March")
fig3.savefig('Marchdata.png')

#April-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [12.086,11.885,11.159,14.268,11.6112,12.9634,11.747,11.983,12.476,10.630,12.472]
y2 = [0.7295,0.536,0.692,0.567,0.707,0.592,0.650,0.678,0.6907,0.5474,0.6593]
fig4 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of April")
fig4.savefig('Aprildata.png')

#May-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [15.55,17.439,17.098,17.699,16.419,16.634,16.606,17.234,15.794,17.0612,16.178]
y2 = [0.7209,0.652,0.663,0.596,0.772,0.687,0.672,0.734,0.698,0.7022,0.7025]
fig5 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of May")
fig5.savefig('Maydata.png')

#June-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [19.5,21.876,21.5115,19.498,20.313,21.155,22.139,20.335,19.867,20.509,21.454]
y2 = [0.746,0.616,0.679,0.675,0.778,0.677,0.622,0.7624,0.6021,0.6552,0.7332]
fig6 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of June")
fig6.savefig('Junedata.png')

#July-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [23.587,23.350,21.761,23.084,23.703,21.641,24.535,22.525,21.896,23.809,22.836]
y2 = [0.656,0.491,0.616,0.6,0.7549,0.707,0.580,0.636,0.6628,0.6229,0.6695]
fig7 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of July")
fig7.savefig('Julydata.png')

#August-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [19.543,23.069,22.45,22.814,21.852,22.876,23.374,23.019,20.784,23.727,21.396]
y2 = [0.761,0.562,0.552,0.596,0.743,0.631,0.5,0.596,0.7854,0.659,0.674]
fig8 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of August")
fig8.savefig('Augustdata.png')

# September-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [18.156,14.344,15.5,19.326,15.569,19.906,19.318,15.319,17.284,18.346,18.366]
y2 = [0.688,0.682,0.689,0.596,0.826,0.6113,0.602,0.6919,0.826,0.713,0.688]
fig9 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of September")
fig9.savefig('Septemberdata.png')

# October-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [12.423,9.67,12.244,10.4501,8.0154,9.422,11.465,12.4474,12.3878,10.172,8.938]
y2 = [0.8125,0.741,0.754,0.763,0.815,0.701,0.794,0.749,0.826,0.84,0.799]
fig10 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of October")
fig10.savefig('Octoberdata.png')

# November-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [5.316,1.2375,5.427,6.161,7.443,1.372,6.607,6.447,6.638,5.548,3.056]
y2 = [0.734,0.813,0.766,0.865,0.858,0.8,0.871,0.824,0.839,0.817,0.848]
fig11 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of November")
fig11.savefig('Novemberdata.png')

# December-Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [0.012,-2.965,0.339,-0.163,-3.474,0.623,-3.663,-0.688,0.577,0.846,-2.0162]
y2 = [0.905,0.856,0.828,0.844,0.9136,0.866,0.886,0.824,0.836,0.925,0.888]
fig12 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Temperature and Humidity Variation over 10 years for month of December")
fig12.savefig('Decemberdata.png')

"""#Final Average Calculation of 10 Years data"""

# Final Data-Analysis
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
y1 = [10.517,11.008,11.028,11.006,10.004,10.51,10.66,10.769,11.589,11.274,10.807]
y2 = [0.7622,0.68,0.701,0.73,0.797,0.724,0.689,0.732,0.755,0.732,0.76]
fig13 = plt.figure()
plt.bar(x,y1,color="green",linewidth = 0.1, label = "Average Temperature")
plt.plot(x,y1,color="red",linewidth = 2.0)
plt.bar(x,y2,color="blue",linewidth = 0.1, label = "Average Humidity")
plt.plot(x,y2,color="yellow",linewidth = 2.0)
plt.ylabel("Numbers")
plt.xlabel("Years")
plt.legend()
plt.legend()
plt.title("Average Temperature and Average Humidity Variation over 10 years")
fig13.savefig('FinalDataAnalysis.png')