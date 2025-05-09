import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', delimiter=',', index_col='date')

# Clean data
df = df['value'] = df[(df['value'] >= df['value'].quantile(0.025)) | (df['value'] <= df['value'].quantile(0.975)) ]
df = df.sort_values('date')


def draw_line_plot():
    # Draw line plot
    fig = plt.plot(df.index,df['value'])

    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #df_bar = 
    df['year'] = df.index.year
    df['month'] = df.index.month
    # Draw bar plot
    fig = plt.bar(df['year'], df['value'])
    df['month'] = df.index.month_name()

    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_grouped = df_grouped[months_order]
    df_grouped.plot(kind='bar', figsize=(12, 8))

    plt.title('Average Page Views per Month per Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = df_box['month'].sort_values()
    df_box.head()
    df_box[df_box['year'] == 2016]['value'].sum()

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(20, 8))
    sns.boxplot(data=df_box, x="year", y="value", ax=axs[0])
    axs[0].ticklabel_format(style='plain', axis='y')
    axs[0].set_ylim(0, 200000)
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Page Views")

    sns.boxplot(data=df_box, x="month", y="value", ax=axs[1], order=month_order)
    axs[1].ticklabel_format(style='plain', axis='y')
    axs[1].set_ylim(0, 200000)
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_xlabel("Month")
    axs[1].set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
