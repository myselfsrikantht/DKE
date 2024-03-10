#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import pandas as pd

def KeywordExtractor(df, x, y):
    df = df[[x, y]]

    def remove_punctuation(text):
        punctuations = string.punctuation
        text_to_punc = ''.join([char for char in text if char not in punctuations])
        return text_to_punc

    df[x] = df[x].apply(remove_punctuation)
    df[x] = df[x].str.replace('\d+', '', regex=True)

    unique_classes = df[y].unique().tolist()

    def split_dataframe_by_class(df, target_column):
        class_dataframes = {}
        for class_value in unique_classes:
            class_df = df[df[target_column] == class_value]
            class_dataframes[class_value] = class_df
        return class_dataframes

    class_dataframes = split_dataframe_by_class(df, y)
    stored_class_dataframes = [class_df for class_df in class_dataframes.values()]

    unique_words = []
    for class_df in stored_class_dataframes:
        words_in_class = class_df[x].str.split().explode().unique().tolist()
        unique_words.append(words_in_class)

    distinct_texts_per_element = []
    for i, element in enumerate(unique_words, start=1):
        distinct_texts = set(element)
        for other_element in unique_words[:i-1] + unique_words[i:]:
            distinct_texts -= set(other_element)
        distinct_texts_per_element.append(list(distinct_texts))
    return distinct_texts_per_element, unique_classes

