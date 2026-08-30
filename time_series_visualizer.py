import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    low = df['value'].quantile(0.025)
    high = df['value'].quantile(0.975)
    df = df[(df['value'] >= low) & (df['value'] <= high)]
    return df


def draw_line_plot():
    df = load_and_clean_data().copy()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    df = load_and_clean_data().copy()
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'month'], observed=False)['value'].mean().unstack()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.reindex(columns=month_order)

    fig = df_bar.plot(kind='bar', figsize=(15, 8)).get_figure()
    ax = fig.axes[0]
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df = load_and_clean_data().copy()
    df_box = df.reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
