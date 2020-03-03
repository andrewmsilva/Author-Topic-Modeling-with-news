import pandas as pd
import sqlite3
import gensim
import nltk
import time
# nltk.download('stopwords')
# nltk.download('wordnet')

import numpy as np
np.random.seed(59)

DB_NAME = 'all-the-news.db'
PROCESSED_NAME = 'processed.csv'

def loadData():
  start_time = time.time()

  df = None
  is_processed = False
  try:
    df = pd.read_csv(PROCESSED_NAME)
    is_processed = True
  except:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query('SELECT title, content FROM longform WHERE content IS NOT NULL', conn)
    conn.commit()
    conn.close()
  
  print('Data loading: {0:.4f} seconds'.format(time.time() - start_time))
  
  return df, is_processed

def preProcess(df, column, is_processed=False):
  start_time = time.time()

  if not is_processed:
    stop_words = gensim.parsing.preprocessing.STOPWORDS
    simple_preprocess = gensim.utils.simple_preprocess
    stemmer = nltk.PorterStemmer()
    lemmatizer = nltk.WordNetLemmatizer()

    processed_texts = []
    for text in df[column]:
      processed_text = []
      for token in simple_preprocess(text):
        if token not in stop_words and len(token) > 3:
          token = lemmatizer.lemmatize(token, pos='v')
          token = stemmer.stem(token)
          processed_text.append(token)
      processed_texts.append(' '.join(processed_text))
    
    df[column] = processed_texts
    df[column].to_csv(PROCESSED_NAME)

  print('Pre-processing: {0:.4f} seconds'.format(time.time() - start_time))

def extractFeatures(df, column):
  start_time = time.time()

  texts = [ text.split() for text in df[column] if type(text) is str ]
  dictionary = gensim.corpora.Dictionary(texts)
  dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

  bow_corpus = [dictionary.doc2bow(doc) for doc in texts]

  tfidf = gensim.models.TfidfModel(bow_corpus)
  tfidf_corpus = tfidf[bow_corpus]

  print('Feature extraction: {0:.4f} seconds'.format(time.time() - start_time))

  return dictionary, bow_corpus, tfidf_corpus

def generateLDA(corpus, dictionary):
  start_time = time.time()

  model = gensim.models.LdaMulticore(
    bow_corpus,
    num_topics=20,
    id2word=dictionary,
    workers=2
  )

  print('LDA generating: {0:.4f} seconds'.format(time.time() - start_time))
  
  return model

news_df, is_processed = loadData()
preProcess(news_df, 'content', is_processed)
dictionary, bow_corpus, tfidf_corpus = extractFeatures(news_df, 'content')

lda_model_bow = generateLDA(bow_corpus, dictionary)
for idx, topic in lda_model_bow.print_topics(-1):
  print('Topic {}: {}\n'.format(idx, topic))

lda_model_tfidf = generateLDA(tfidf_corpus, dictionary)
for idx, topic in lda_model_tfidf.print_topics(-1):
  print('Topic {}: {}\n'.format(idx, topic))