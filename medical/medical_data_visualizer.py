import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv', delimiter=',')

# 2
df['overweight'] = None

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1 , 1, 0)
df['gluc'] = np.where(df['gluc'] > 1 , 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars='cardio', value_vars=['overweight', 'cholesterol', 'active','gluc','smoke','alco'], var_name='variable', value_name='value')




    # 6
    df_cat = df_melt.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    sns.catplot(data=df_cat, x="variable", y='total', hue="value", col = 'cardio', kind="bar")


    # 8
    fig = plt.show()


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] >= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] >= df['weight'].quantile(0.975))]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # 14
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.title('correlacion')

    # 15
    sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", center=0)
    # 16
    fig.savefig('heatmap.png')
    return fig
