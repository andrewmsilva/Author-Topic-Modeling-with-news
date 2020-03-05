import pandas as pd
import sqlite3
import gensim
import nltk
import time
import pickle
# nltk.download('stopwords')
# nltk.download('wordnet')

import numpy as np
np.random.seed(59)

DB_NAME = 'all-the-news.db'
PROCESSED_CSV = 'processed.csv'
DICTIONARY = 'dictionary.bin'
BOW_CORPUS = 'bag-of-words.bin'
TFIDF_CORPUS = 'tf-idf.bin'
LDA_MODEL = 'lda-model.bin'

def loadData():
  start_time = time.time()

  try:
    df = pd.read_csv(PROCESSED_CSV)
    is_processed = True
  except:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query('SELECT title, content FROM longform WHERE content IS NOT NULL', conn)
    conn.commit()
    conn.close()
    is_processed = False
  
  print('Data loading: {0:.4f} seconds'.format(time.time() - start_time))
  
  return df, is_processed

def preProcess(df, column, is_processed=False):
  start_time = time.time()

  if not is_processed:
    stop_words = gensim.parsing.preprocessing.STOPWORDS
    simple_preprocess = gensim.utils.simple_preprocess
    stemmer = nltk.SnowballStemmer('english')
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
    df[column].to_csv(PROCESSED_CSV)

  print('Pre-processing: {0:.4f} seconds'.format(time.time() - start_time))

def extractFeatures(df, column):
  start_time = time.time()

  texts = [ text.split() for text in df[column] if type(text) is str ]

  try:
    dictionary = gensim.corpora.Dictionary.load(DICTIONARY)
  except:
    dictionary = gensim.corpora.Dictionary(texts)
    dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
    dictionary.save(DICTIONARY)

  try:
    f = open(BOW_CORPUS, 'rb')
    bow_corpus = pickle.load(f)
  except:
    bow_corpus = [dictionary.doc2bow(doc) for doc in texts]

    f = open(BOW_CORPUS, 'wb')
    pickle.dump(bow_corpus, f)
  finally:
    f.close()
  
  try:
    f = open(TFIDF_CORPUS, 'rb')
    tfidf_corpus = pickle.load(f)
  except:
    tfidf = gensim.models.TfidfModel(bow_corpus)
    tfidf_corpus = tfidf[bow_corpus]

    f = open(TFIDF_CORPUS, 'wb')
    pickle.dump(tfidf_corpus, f)
  finally:
    f.close()

  print('Feature extraction: {0:.4f} seconds'.format(time.time() - start_time))

  return dictionary, bow_corpus, tfidf_corpus

def generateLDA(corpus, dictionary):
  start_time = time.time()

  try:
    model = gensim.models.LdaMulticore.load(LDA_MODEL)
  except:
    model = gensim.models.LdaMulticore(
      corpus,
      num_topics=50,
      id2word=dictionary,
      workers=2
    )
    model.save(LDA_MODEL)
  
  print('LDA generating: {0:.4f} seconds'.format(time.time() - start_time))
  
  return model

news_df, is_processed = loadData()
preProcess(news_df, 'content', is_processed)
dictionary, bow_corpus, tfidf_corpus = extractFeatures(news_df, 'content')

lda_model = generateLDA(tfidf_corpus, dictionary)
for idx, topic in lda_model.print_topics(-1):
  print('Topic {}: {}\n'.format(idx, topic))