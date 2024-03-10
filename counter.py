#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def KeywordCounter(df, x, y, keyword_list, unique_classes):
    def count_elements(sentence, keyword_list):
        return sum(1 if word in keyword_list else 0 for word in sentence.split())

    for i, key in enumerate(unique_classes):
        df[key] = df[x].apply(lambda x: count_elements(x, keyword_list[i]))

    return df

