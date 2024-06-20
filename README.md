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
#### 1. syllable category
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/e893ad05-aae0-47c1-95b1-b1da49a8eb46)
The highest frequency of words used by the native speakers is 2-syllable.
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/16d62389-9e3b-4da6-b7c8-0a73094db54c)
It is directly proportional to the number of distinct syllable words that more words in the list are classified into 1-syllable and 2-syllable.

#### 2. By lexical word (part ò speech)
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/434fd3c2-bb07-4f55-9618-e42f54bc76ea)
Plot a bar chart with stacks representing the syllables, and we can see Noun is the largest group in the list.
To be more clear, I created a heatmap chart.
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/77f9ac1d-ee38-4ed3-a2cb-630393ba476c)
The heatmap shows more information about the relationship and distribution of two variables 

#### 3. The distribution of each syllable segment.
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/ea6ef571-a248-4721-8d43-470f378a0e1f)
The grid of charts shows the distribution of each syllable category, with each chart displaying a similar allocation pattern.

### Deeper analyzing
#### 1. I want to study on a common range from 400 to 4500
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/bcf34432-45b3-45aa-8810-b5c67148657e)
The result indicated a list of the number of words in each syllable group respectively from 1 to 7
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/3e9ed956-871c-441b-b0b3-cbbcefa472e9)

#### 2. I want to investigate in smaller ranges
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/9761f75f-7bb1-4354-8bee-78145f5c3b5a)
There is a slight change of syllable groups in each ranges.

![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/cd05f022-2363-458d-95bb-74914c4a5887)
In the other ranges.

#### 3. Investigate the whole large range:
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/219441b1-38f0-4106-92e5-1cc7c63e2e4a)

### Final table
![image](https://github.com/KeithDang1610/Data-analysis-Common-English-Words/assets/167521177/0deee257-f03b-4c74-8510-e3f4f6fed7f4)

## Conclusion
I used two datasets on Kaggle; however, only one had a credibility score above 7.0, while the other had a low score, which can introduce bias and sometimes lead to misleading results. Nevertheless, it is still useful if they are used as a reference for English learning materials. Both datasets contain numerous errors, Null values, and redundancies, requiring extensive  cleaning and processing to improve the data for analysis and visualization.
I selected a range from 400 to 5000 words based on their frequency of use. This range allows learners to communicate fluently in daily conversation without learning excessive unnecessary words. Throughout my analysis, I concluded that knowing many extraordinary words such as those with 6 or 7 syllables, is superfluous for daily conversation. Instead,  it is more beneficial to learn shorter words, primarily those with 2, 3, and 4 syllables. Additionally, nouns make up the largest proportion of common English words, followed by adjectives and verbs. 
As a non-native English speaker, this aggregated table could be valuable for expanding my vocabulary and focusing essential range of words, ultimately enhancing my communication skills in daily conversation.




