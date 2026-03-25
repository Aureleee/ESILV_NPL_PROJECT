# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aurele <aurele@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 19:09:57 by aurele            #+#    #+#              #
#    Updated: 2026/03/24 19:10:44 by aurele           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# This files mostly contains functions to load and preprocess the data, 
# as well as to save the results of the project.

import pandas as pd
import re
from collections import Counter
from itertools import islice

def clean_text(text):
    if pd.isna(text):
        return ""
    
    # lower case
    text = text.lower()
    
    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    
    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

def tokenize(text):
    return text.split()

def generate_ngrams(tokens, n):
    return zip(*[tokens[i:] for i in range(n)])

def get_word_frequencies(texts):
    counter = Counter()
    
    for text in texts:
        cleaned = clean_text(text)
        tokens = tokenize(cleaned)
        counter.update(tokens)
    
    return counter