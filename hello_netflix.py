# %%
from os.path import dirname, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

project_path = dirname(__file__)
input_path = join(project_path,'input')
output_path = join(project_path,'reports')


# %%
netflix_file = join(input_path,'netflix.csv')
df = pd.read_csv(netflix_file)
df.head()

# %%
df.shape
df.columns

# %%    >>> Check & visualize null values in dataset

empty_val = df.isna()

plt.figure(figsize=(10, 8))
sns.heatmap(empty_val.transpose(),
    cmap='YlGnBu',
    cbar_kws={'label': 'Missing Values'})
plt.show()



# sns.pairplot(df)
# %%
plt.figure(figsize=(10, 8))
sns.displot(
    data=empty_val.melt(value_name='missing'),
    y='variable',
    hue='missing',
    multiple='fill',
    aspect= 1.25    )
plt.show()

# %%
