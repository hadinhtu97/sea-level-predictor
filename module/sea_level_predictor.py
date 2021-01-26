import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('./data/data.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    l = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = [i for i in range(df['Year'].iloc[0], 2051)]
    y = [l.intercept + l.slope*year for year in x]
    plt.plot(x, y)

    df_2000 = df[df['Year'] >= 2000]
    l = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x = [i for i in range(2000, 2051)]
    y = [l.intercept + l.slope*year for year in x]
    plt.plot(x, y)

    plt.savefig('./img/sea_level_plot.png')
