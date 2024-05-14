#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:59:47 2024

@author: vidushaadira
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re


data = pd.read_csv("/Users/vidushaadira/Downloads/political_social_media.csv", encoding='latin1')
def remove_urls(text):
    return re.sub(r'http://t.co', '', text)

data['text'] = data['text'].apply(remove_urls)

words_to_filter = ['a ', 'Û', 'amp', ' u ', ' a ', 'U ', ' a.']

def filter_words(text):
    for word in words_to_filter:
        text = re.sub(word, '', text)
    return text

data['text'] = data['text'].apply(filter_words)


neutral_subset = data[data["bias"] == "neutral"]["text"]
text_data = ' '.join(neutral_subset)


neutral_wordcloud = WordCloud().generate(text_data)
plt.imshow(neutral_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

partisan_subset = data[data["bias"] == "partisan"]["text"]
partisan_text_data = ' '.join(partisan_subset)


partisan_wordcloud = WordCloud().generate(partisan_text_data)
plt.imshow(partisan_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


histogram = plt.hist(data['message'])
plt.show(histogram)

attack_subset = data[data["message"] == "attack"]["text"]
attack_text_data = ' '.join(attack_subset)
attack_wordcloud = WordCloud().generate(attack_text_data)
plt.imshow(attack_wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

