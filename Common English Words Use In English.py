#!/usr/bin/env python
# coding: utf-8

# ## DATA ANALYSIS TO FIGURE OUT THE DISTRIBUTION OF ENGLISH WORDS

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Read the table of dataset 1
df1 = pd.read_csv('words_fre.csv')


# In[3]:


# Read the table of dataset 2
df2 = pd.read_csv('Phrases_Fre.csv')


# ### 1. Check the data

# In[4]:


df2.isnull().sum()


# In[5]:


import seaborn as sns
sns.heatmap(df2.isnull())


# In[6]:


get_ipython().system('pip install missingno')


# In[7]:


import missingno as msno
msno.matrix(df2)


# In[8]:


msno.heatmap(df2)


# In[9]:


df1.head(100)


# In[10]:


df2.head(20)


# In[11]:


df2.info()


# In[12]:


df1.info()


# ### Process Steps

# #### Cleaning data and correct the data formats

# In[13]:


# import pyplot and seaborn libraries
from matplotlib import pyplot as plt
import seaborn as sns


# In[14]:


# the best way to find null values
sns.heatmap(data=df2.isnull())


# In[15]:


df2.isnull().sum()


# In[16]:


# Lower strings in Word column
df2['Word']=df2['Word'].str.lower()


# In[17]:


df2[df2['Word'].str.contains('a ')]


# In[18]:


# Check again
df1.head(100)


# In[19]:


# drop 50 initial words 
df1=df1.drop(df1.index[:50]).reset_index(drop=True)


# In[20]:


# Create the copies of two tables
df1_copy =df1.copy()
df2_copy = df2.copy()


# In[21]:


# Check the string values in Word columns, then figured out the spacings in the values. Removing them
df2_copy['Word']=df2_copy['Word'].apply(lambda x: x.replace(' ',''))


# In[22]:


# Remove duplicates
df2_copy=df2_copy.drop_duplicates()


# In[23]:


df2_copy


# In[24]:


df_merge= df2_copy.merge(df1_copy, left_on='Word', right_on ='word', how='left')


# In[25]:


df_merge


# In[26]:


# order data
df_merge.sort_values(by=['Word','count'], ascending =[True,False])


# In[27]:


# Check the N/A values of count column
sns.heatmap(data=df_merge['count'].isna().values.reshape(-1, 1))


# In[28]:


df_merge['count'] =df_merge['count'].dropna()


# In[29]:


sns.heatmap(data=df_merge['count'].isna().values.reshape(-1, 1))


# In[30]:


# drop na values only consider the 'count' column to determine which rows to drop.
df_merge.dropna(subset=['count'], inplace=True)


# In[31]:


df_merge.sort_values(by=['count','Word'], ascending =[False,True])


# In[32]:


df_merge = df_merge.sort_values(by='count', ascending =False)


# In[33]:


# Use syllapy to classify words into syllable groups
import syllapy


# In[34]:


# apply to Word column
df_merge['syllables']= df_merge['Word'].apply(lambda x: syllapy.count(x))


# In[35]:


# Examine the result, These words below are correctly clasified 
df_merge[df_merge['syllables']==4]


# In[36]:


# Check N/A values. There is no N/A. 
sns.heatmap(df_merge['Word'].isna().values.reshape(-1, 1))


# In[37]:


# Drop these column because of useless
df_merge = df_merge.drop(['Examples/6','Examples/7','Examples/8','Examples/9'], axis=1)


# In[38]:


# drop word column
df_merge = df_merge.drop('word', axis=1)


# In[39]:


df = df_merge.groupby('syllables')


# In[40]:


# Sum the frequency of each syllable group
sum_df = df.sum()
print(sum_df)


# df_merge.sort_values(by=['syllables','count'], ascending =[True,False])

# ### Data Visualization

# In[41]:


# Plot a number words by syllables chart
plt.figure(figsize=(10, 6))
sns.barplot(x=df_merge['syllables'].value_counts().index, 
            y=df_merge['syllables'].value_counts())
plt.title('Frequency of Syllables')
plt.xlabel('Syllables')
plt.ylabel('Frequency')


# In[42]:


# The frequency of each syllable group
df_merge['syllables'].value_counts()


# In[43]:


sum_counts = df_merge.groupby('syllables')['count'].sum()
print("Sum of counts for each syllable:")
print(sum_counts)


# In[44]:


# Frequency of Words by Syllables in Use
# The words with the most frequency are the ones with two syllables.
sorted_df = df_merge.groupby('syllables')['count'].sum().reset_index().sort_values(by='count', ascending=False)

# Plot the data
sns.barplot(x='syllables', y='count', data=sorted_df)

# Show the plot
plt.show()


# In[45]:


import nltk
from nltk.tokenize import word_tokenize


# In[46]:


# Function to categorize words based on part of speech
def categorize_pos(word):
    pos_tag = nltk.pos_tag([word])[0][1]
    if pos_tag.startswith('N'):
        return 'N'
    elif pos_tag.startswith('J'):
        return 'Adj'
    elif pos_tag.startswith('V'):
        return 'V'
    elif pos_tag.startswith('R'):
        return 'Adv'
    elif pos_tag.startswith('WDT'):
        return 'wh-determiner'
    elif pos_tag.startswith('MD'):
        return 'modal'
    elif pos_tag.startswith('CC'):
        return 'CC'
    elif pos_tag.startswith('PRP$'):
        return 'PRP'
    elif pos_tag.startswith('WRB'):
        return 'Wh-adverb'       
    else:
        return 'other'

# Assuming df is your DataFrame and 'words' is the column containing the words
df_merge['pos_category'] = df_merge['Word'].apply(categorize_pos)



# In[47]:


df_merge.sort_values(by=['syllables','count','pos_category'], ascending =[True, False, True])


# In[48]:


plt.figure(figsize=(16,8))
sns.histplot(data=df_merge, x='pos_category', hue='syllables', multiple="stack", palette='Blues')


# In[49]:


# unstack() method reshapes the Series with a multi-level index into a DataFrame.
# transform the type of data
# The size() method counts the number of rows in each group created by groupby.
heatmap_data = df_merge.groupby(['pos_category', 'syllables']).size().unstack(fill_value=0)
plt.figure(figsize=(10, 6))
sns.heatmap(data=heatmap_data, cmap='viridis')


# In[50]:


# Ranking the words by their count
df_merge['rank'] = df_merge['count'].rank(ascending=False)


# In[51]:


df_merge['rank'] = df_merge['rank'].astype(int)


# In[52]:


df_merge


# In[53]:


df_merge.columns


# In[54]:


df_merge.head()


# In[55]:


columns_name_reordered = ['rank', 'Word', 'pos_category','Meaning', 'Examples/0', 'Examples/1',
       'Examples/2', 'Examples/3', 'Examples/4', 'Examples/5', 'count',
       'syllables']


# In[56]:


df_merge=df_merge[columns_name_reordered]


# In[57]:


df_merge.columns


# In[58]:


columns_renamed = ['Rank', 'Word', 'Lexical words', 'Meaning', 'Examples 1',
       'Examples 2', 'Examples 3', 'Examples 4', 'Examples 5', 'Examples 6',
       'Frequency', 'Syllables']


# In[59]:


df_merge.columns = columns_renamed


# In[60]:


df_merge=df_merge.sort_values(by=['Syllables','Rank','Lexical words'], ascending =[True, True, True])


# In[61]:


df_merge=df_merge.drop(['Frequency','Examples 6'], axis=1)


# In[62]:


df_merge


# In[63]:


import eng_to_ipa as p


# In[64]:


df_merge=df_merge.drop('Phonetics', axis=1)


# In[ ]:


df_merge['Word'][11131][-1:]


# In[ ]:


def change(word):
    ipa = p.convert(word)
    if ipa[-1:]!= "*":
        return ipa
    else:
        return "unknown"

df_merge['Phonetics'] = df_merge['Word'].apply(change)   


# In[ ]:


df_merge


# In[ ]:


df_merge=df_merge[df_merge["Phonetics"] != "unknown"]


# In[ ]:


## Find the most common range of eng


# In[ ]:


df_common = df_merge.copy()


# In[ ]:


df_common.sort_values("Rank" ,ascending = True)[:7000][df_common["Syllables"]==6]


# In[ ]:


len(df_common.sort_values("Rank" ,ascending = True)[:000][df_common["Syllables"]==2])


# In[ ]:


# Create a FacetGrid with Seaborn
g = sns.FacetGrid(df_common, col="Syllables")

# Map the histogram plot onto the grid
g.map(sns.histplot, "Rank", kde=True, bins=20)


# In[ ]:


# Show in rank(0-400) how many values have syllables equal 1
df_common.sort_values("Rank" ,ascending = True)[:400][df_common["Syllables"]==1]


# In[ ]:


# Show in from lists of Syllables having values =1, sorted by Rank and get 400 individuals
df_common[df_common["Syllables"]==1].sort_values("Rank" ,ascending = True)[:400]


# In[ ]:


len(df_common.loc[(df_common["Rank"] <= 300) & (df_common["Syllables"] == 2), :].sort_values("Rank", ascending=True))


# In[ ]:


df_common.to_csv(r'C:\Users\DELL\Desktop\Words(En) Project\edit_eng_words.csv')


# In[ ]:


df_common = pd.read_csv(r'C:\Users\DELL\Desktop\Words(En) Project\edit_eng_words.csv')


# In[ ]:


df_common


# In[ ]:


one= len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 1), :].sort_values("Rank", ascending=True))
print(one)
two=len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 2), :].sort_values("Rank", ascending=True))
print(two)
three=len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 3), :].sort_values("Rank", ascending=True))
print(three)
four= len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 4), :].sort_values("Rank", ascending=True))
print(four)
five=len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 5), :].sort_values("Rank", ascending=True))
print(five)
six=len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == 6), :].sort_values("Rank", ascending=True))
print(six)


# In[ ]:


counts = []
for syllable_count in range(1, 7):
    count = len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500) & (df_common["Syllables"] == syllable_count), :])
    counts.append(count)

syllable_counts = range(1, 7)
plt.bar(syllable_counts, counts)
plt.xlabel('Number of Syllables')
plt.ylabel('Count')
plt.title('Count of Words by Syllable Count')
plt.show()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

# Filter the DataFrame based on conditions
filtered_df = df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500)]

# Create countplot
sns.countplot(x="Syllables", data=filtered_df)
plt.xlabel('Number of Syllables')
plt.ylabel('Count')
plt.title('Count of Words by Syllable Count')
plt.show()


# In[ ]:


# Filter the DataFrame based on conditions
filtered_df = df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 4500)]

# Create countplot
ax = sns.countplot(x="Syllables", data=filtered_df)

# Add count labels on top of each bar
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'center', 
                xytext = (0, 5), 
                textcoords = 'offset points')

plt.xlabel('Number of Syllables')
plt.ylabel('Count')
plt.title('Count of Words by Syllable Count')
plt.show()


# In[ ]:



# Define the filter conditions
filter_conditions = [
    ("Rank 400-1000", (400 <= df_common["Rank"]) & (df_common["Rank"] <= 1000)),
    ("Rank 1001-2500", (1001 <= df_common["Rank"]) & (df_common["Rank"] <= 2500)),
    ("Rank 2501-4500", (2501 <= df_common["Rank"]) & (df_common["Rank"] <= 4500))
]

# Create subplots
fig, axes = plt.subplots(nrows=1, ncols=len(filter_conditions), figsize=(15, 5))

# Plot countplots for each filter condition
for i, (title, condition) in enumerate(filter_conditions):
    filtered_df = df_common.loc[condition]
    ax = sns.countplot(x="Syllables", data=filtered_df, ax=axes[i])
    ax.set_title(title)
    ax.set_xlabel('Number of Syllables')
    ax.set_ylabel('Count')

plt.tight_layout()
plt.show()


# In[ ]:


# Define the filter conditions
filter_conditions = [
    ("Rank 400-3000", (400 <= df_common["Rank"]) & (df_common["Rank"] <= 3000)),
    ("Rank 3001-5500", (3001 <= df_common["Rank"]) & (df_common["Rank"] <= 5500)),
    ("Rank 5501-7000", (5501 <= df_common["Rank"]) & (df_common["Rank"] <= 7000))
]

# Create a new column to represent the rank range
for title, condition in filter_conditions:
    df_common.loc[condition, "Filter"] = title

# Create a FacetGrid with hue
g = sns.FacetGrid(df_common, col="Filter", hue="Filter", col_wrap=len(filter_conditions), sharey=False)

# Map countplot onto the grid
g.map(sns.countplot, "Syllables", order=[1, 2, 3, 4, 5, 6])

# Annotate each bar with its count
for ax in g.axes.flat:
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 5), 
                    textcoords = 'offset points')

# Set labels
g.set_axis_labels("Number of Syllables", "Count")

plt.tight_layout()
plt.show()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

# Define the filter conditions
filter_conditions = [
    ("Rank 400-3000", (400 <= df_common["Rank"]) & (df_common["Rank"] <= 5000)),
    ("Rank 3001-5500", (3001 <= df_common["Rank"]) & (df_common["Rank"] <= 7500)),
    ("Rank 5501-7000", (5501 <= df_common["Rank"]) & (df_common["Rank"] <= 7000)),
    ("Rank 7001-11000", (7001 <= df_common["Rank"]) & (df_common["Rank"] <= 11000))
]

# Create a new column to represent the rank range
for title, condition in filter_conditions:
    df_common.loc[condition, "Filter"] = title

# Create a FacetGrid with hue
g = sns.FacetGrid(df_common, col="Filter", col_wrap=len(filter_conditions), sharey=False)

# Map countplot onto the grid with custom color palette
g.map(sns.countplot, "Syllables", order=[1, 2, 3, 4, 5, 6], palette="husl")

# Annotate each bar with its count
for ax in g.axes.flat:
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 5), 
                    textcoords = 'offset points')

# Set labels
g.set_axis_labels("Number of Syllables", "Count")

plt.tight_layout()
plt.show()


# In[ ]:


for syllable_count in range(1, 7):
    count = len(df_common.loc[(400 <= df_common["Rank"]) & (df_common["Rank"] <= 5500) & (df_common["Syllables"] == syllable_count), :].sort_values("Rank", ascending=True))
    print(f"{syllable_count}: {count}")


# In[ ]:


df_common[(df_common["Rank"]<=200) & (df_common["Syllables"]==1)]


# In[ ]:


df_common.drop(df_common[(df_common["Rank"] <= 200) & (df_common["Syllables"] == 1)].index, inplace=True)


# In[ ]:


df_common[:5000].drop_duplicates()


# In[ ]:


df_common = pd.read_csv(r'C:\Users\DELL\Desktop\Words(En) Project\edit_eng_words.csv')


# In[ ]:


df_common.drop


# In[ ]:


df_common.drop(df_common[(df_common["Rank"] <= 200) & (df_common["Syllables"] == 1)].index, inplace=True)


# In[ ]:


df_common = df_common.sort_values("Rank", ascending=True)


# In[ ]:


df_common_cut = df_common[:5000]


# In[ ]:


df_common_cut


# In[ ]:


for syllable_count in range(1, 7):
    count = len(df_common_cut.loc[(400 <= df_common_cut["Rank"]) & (df_common_cut["Rank"] <= 4500) & (df_common_cut["Syllables"] == syllable_count), :])
    print(count)


# In[ ]:


df_common_cut.to_csv(r'C:\Users\DELL\Desktop\Words(En) Project\new_cut_eng_words.csv')


# In[ ]:


df_common_cut


# In[ ]:




