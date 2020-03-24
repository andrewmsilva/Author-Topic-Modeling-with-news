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
TFIDF_CORPUS = 'tf-idf.bin'
LDA_MODEL = 'lda-model.bin'

def printExecutionTime(start_time):
  print('Completed in {0:.4f} seconds\n'.format(time.time() - start_time))

def loadData():
  print('Loading data...')
  start_time = time.time()

  try:
    df = pd.read_csv(PROCESSED_CSV)
    is_processed = True
  except:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query('SELECT author, date, year, publication, content FROM longform WHERE content != "" AND content IS NOT NULL', conn)
    conn.commit()
    conn.close()
    is_processed = False
  
  printExecutionTime(start_time)
  return df, is_processed

def preProcess(df, column, is_processed=False):
  print('Pre-processing...')
  start_time = time.time()

  processed_docs = None
  if is_processed:
    processed_docs = [ doc.split() for doc in df[column] ]
  else:
    stop_words = gensim.parsing.preprocessing.STOPWORDS
    simple_preprocess = gensim.utils.simple_preprocess
    stemmer = nltk.SnowballStemmer('english')
    lemmatizer = nltk.WordNetLemmatizer()

    processed_docs = []
    for doc in df[column]:
      processed_doc = []
      for token in simple_preprocess(doc):
        if token not in stop_words:
          token = lemmatizer.lemmatize(token, pos='v')
          token = stemmer.stem(token)
          processed_doc.append(token)
      processed_docs.append(processed_doc)
    
    df[column] = [ ' '.join(doc) for doc in processed_docs ]
    df[column].to_csv(PROCESSED_CSV)

  printExecutionTime(start_time)
  return processed_docs

def extractDictionary(documents):
  print('Extracting dictionary...')
  start_time = time.time()

  try:
    dictionary = gensim.corpora.Dictionary.load(DICTIONARY)
  except:
    dictionary = gensim.corpora.Dictionary(documents)
    dictionary.filter_extremes(no_below=200, no_above=0.8, keep_n=1000)
    dictionary.save(DICTIONARY)

  printExecutionTime(start_time)
  return dictionary

def extractFeatures(documents, dictionary):
  print('Extracting features...')
  start_time = time.time()
  
  try:
    f = open(TFIDF_CORPUS, 'rb')
    tfidf_corpus = pickle.load(f)
  except:
    bow_corpus = [ dictionary.doc2bow(doc) for doc in documents ]
    tfidf = gensim.models.TfidfModel(bow_corpus)
    tfidf_corpus = tfidf[bow_corpus]

    f = open(TFIDF_CORPUS, 'wb')
    pickle.dump(tfidf_corpus, f)
  finally:
    f.close()

  printExecutionTime(start_time)
  return tfidf_corpus

def generateLDA(corpus, dictionary):
  print('Generating LDA...')
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
  
  printExecutionTime(start_time)
  return model

collection = 'content'
author = 'publication'

news_df, is_processed = loadData()
processed = preProcess(news_df, collection, is_processed)

dictionary = extractDictionary(processed)
tfidf_corpus = extractFeatures(processed, dictionary)

lda_model = generateLDA(tfidf_corpus, dictionary)
for idx, topic in lda_model.print_topics(-1):
  print('Topic {}: {}\n'.format(idx, topic))