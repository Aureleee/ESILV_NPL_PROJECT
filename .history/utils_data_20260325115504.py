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

def get_ngram_frequencies(texts, n=2):
    counter = Counter()
    
    for text in texts:
        cleaned = clean_text(text)
        tokens = tokenize(cleaned)
        ngrams = generate_ngrams(tokens, n)
        counter.update(ngrams)
    
    return counter



# =========================
# TOPIC MODELING (LDA)
# =========================

from gensim import corpora
from gensim.models import LdaModel


def prepare_texts_for_lda(texts):
    """
    Clean + tokenize all texts
    """
    texts_clean = []
    
    for text in texts:
        cleaned = clean_text(text)
        tokens = tokenize(cleaned)
        texts_clean.append(tokens)
    
    return texts_clean


def build_dictionary(texts_clean):
    """
    Create word dictionary (word → id)
    """
    return corpora.Dictionary(texts_clean)


def build_corpus(texts_clean, dictionary):
    """
    Convert texts into Bag-of-Words format
    """
    return [dictionary.doc2bow(text) for text in texts_clean]


def train_lda_model(corpus, dictionary, num_topics=5, passes=10):
    """
    Train LDA model
    """
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes
    )
    
    return lda_model


