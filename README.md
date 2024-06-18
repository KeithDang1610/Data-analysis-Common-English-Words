# Data-analysis-Common-English-Words
Use various datasets on Kaggle, then aggregate, clean, and analyze them to gain insights into how natives learn and use these words in writing and verbal communication
## Project Objective:
- Explore and gain insights into how the natives use common English words daily and the distribution of the structures of words.
## Method used:
- Data cleaning
- Prepare data
- process data
- Data analysis
- Data visualization
## Tool used:
- Python
## Datasets information
- Using datasets from different sources on Kaggle.
  df1 contains words and the frequency of them.
  ![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/dbf49edf-c264-49bc-b0e3-15901271f5ae)
  
  df2 includes words ordered by ascending alphabet and the examples in the contexts
  ![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/90eb2900-ff99-43d6-ad6e-553f4798cafa)
## After cleaning each data, joining them into a united file, create some essential metrics to figure out insights from them. 
- Using syllapy lib to create a new column of syllable words
- Using nltk lib to create a new column named pos_category representing parts of speech
- Using eng_to_ipa lib to create a phonetic column
### Analyzing and visualization
1. syllable category
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/e893ad05-aae0-47c1-95b1-b1da49a8eb46)
The highest frequency of words used by the native speakers is 2-syllable.
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/16d62389-9e3b-4da6-b7c8-0a73094db54c)
It is directly proportional to the number of distinct syllable words that more words in the list are classified into 1-syllable and 2-syllable.

2. By lexical word (part ò speech)
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/434fd3c2-bb07-4f55-9618-e42f54bc76ea)
Plot a bar chart with stacks representing the syllables, and we can see Noun is the largest group in the list.
To be more clear, I created a heatmap chart.
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/77f9ac1d-ee38-4ed3-a2cb-630393ba476c)
The heatmap shows more information about the relationship and distribution of two variables 


