import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():

    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')


    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = np.arange(df['Year'].min(), 2051)
    y_pred1 = res1.slope * x_pred1 + res1.intercept
    plt.plot(x_pred1, y_pred1, 'r', label='Fit: all data')


    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = np.arange(2000, 2051)
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'green', label='Fit: from 2000')


    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show()

  
    plt.savefig('sea_level_plot.png')
    return plt.gca()
