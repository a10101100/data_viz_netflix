# %%
from os.path import dirname, join
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import ast


project_path = dirname(__file__)
input_path = join(project_path,'input')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['figure.figsize'] = (20, 16)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# %%
titles = pd.read_csv(join(input_path,'titles.csv'))
titles.head()

# %%
titles.shape
titles.info()


# region >>> Check & visualize null values in dataset
# %%    
empty_val = titles.isna()
# null values via heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(empty_val.transpose(),
    cmap='RdYlBu_r',
    cbar_kws={'label': 'Missing Values'})
plt.show()


# %%
# null values via displot
plt.figure(figsize=(10, 8))
sns.displot(
    data=empty_val.melt(value_name='missing'),
    y='variable',
    hue='missing',
    multiple='fill',
    palette='RdYlBu_r',
    aspect= 1.25)
plt.show()

# endregion

# %%

## data cleaning -- null values
titles['age_certification'].fillna('', inplace=True)
titles['seasons'].fillna(0, inplace=True)
titles['imdb_score'].fillna(0, inplace=True)
titles['imdb_votes'].fillna(0, inplace=True)




# %%

## data cleaning -- multiple values in list


def repair_array_bound_categories(arr):
    
    arr = ast.literal_eval(arr)
    
    if len(arr) == 0:
        return np.nan
    
    elif len(arr) >= 1:
        return arr[0]
    


## just get the first item in list for simplified analysis, assuming in order of importance
titles["production_countries"] = titles["production_countries"].apply(repair_array_bound_categories)
titles["genres"] = titles["genres"].apply(repair_array_bound_categories)
titles

# %%

## stats on dataframe
titles.describe()


## release year analysis

showsByYears=titles.groupby('release_year').title.count()
showsByYears=pd.DataFrame(showsByYears)
count_shows=showsByYears['title'].to_numpy()
years=titles['release_year'].unique()

sns.pointplot(x=years,y=count_shows,color='b')
plt.xticks(rotation=90)
plt.title('# Netflix Shows Released Timeline')
plt.xlabel('Year')
plt.ylabel('# Netflix Shows')

## flat since 1945 but exponential growth from 2011
## peak was at 2019 pre-Covid ,, max content
## huge dip in 2021 presumbly standstill due to the worldwide impacts from the global pandemic Covid-19
## resumed to normal levels the following years


# %%
## countries analysis
production_countries = titles['production_countries'].value_counts()
production_countries = pd.DataFrame(production_countries)
production_countries



sns.countplot(x='production_countries'
    , data=titles
    , order=titles['production_countries'].value_counts().index)
plt.xticks(rotation=45)
plt.title('# Netflix Shows by Production Countries')
plt.show()



# %%
top10countries = titles['production_countries'].value_counts().nlargest(10)
top10countries = pd.DataFrame(top10countries)

plt.pie(top10countries['production_countries'], labels=top10countries.index, autopct='%1.1f%%')
plt.axis('equal')
# plt.legend(title='production countries')
plt.show()

# %%
sns.countplot(y='genres'
    , data=titles
    , order=titles['genres'].value_counts().index)
plt.xticks(rotation=45)
plt.title('# Netflix Shows by Genres')
plt.show()

# %%
certifications=titles.groupby('age_certification')['title'].count()
certifications=pd.DataFrame(certifications)


sns.catplot(x='age_certification',kind="count",data=titles)
plt.xticks(rotation=45)
plt.title('# Netflix shows by Ratings (Age certification)')


# %%
