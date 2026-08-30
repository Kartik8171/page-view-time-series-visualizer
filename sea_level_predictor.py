import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope, intercept, _, _, _ = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    years = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years, slope * years + intercept)

    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, slope_recent * years_recent + intercept_recent)

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    fig.savefig('sea_level_plot.png')
    return fig
