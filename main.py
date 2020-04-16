from pandas import read_sql_query
from sqlite3 import connect
from pickle import load, dump
from time import time

from gensim.utils import simple_preprocess
from gensim.models import Phrases
from gensim.models.phrases import Phraser
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora import Dictionary
from gensim.models import TfidfModel, AuthorTopicModel

from nltk import SnowballStemmer, WordNetLemmatizer

import numpy as np
np.random.seed(59)

DB_NAME = 'all-the-news.db'

SOURCES_FILE = 'sources.bin'
YEARS_FILE = 'years.bin'
NEWS_FILE = 'news.bin'
PROCESSED_NEWS_FILE = 'processed-news.bin'

DICTIONARY_FILE = 'dictionary.bin'
TFIDF_FILE = 'tf-idf.bin'
MODEL_FILE = 'model.bin'

def printExecutionTime(start_time):
  print('Completed in {0:.4f} seconds\n'.format(time() - start_time))

def loadData():
  print('Loading data...')
  start_time = time()

  try:
    # Loading if possible
    sources_file = open(SOURCES_FILE, 'rb')
    sources = load(sources_file)

    years_file = open(YEARS_FILE, 'rb')
    years = load(years_file)

    news_file = open(NEWS_FILE, 'rb')
    news = load(news_file)
  except:
    conn = connect(DB_NAME)
    df = read_sql_query('SELECT publication, year, content FROM longform WHERE content != "" AND content IS NOT NULL AND publication != "" AND publication IS NOT NULL', conn)
    conn.commit()
    conn.close()
    
    sources = dict()
    years = dict()
    news = list()
    for index, row in df.iterrows():
      # Populating sources
      if row.publication not in sources.keys():
        sources[row.publication] = list()
      sources[row.publication].append(index)
      # Populating years
      if row.year not in years.keys():
        years[row.year] = list()
      years[row.year] = index
      # Populating news
      news.append(row.content)
    del df

    # Saving sources to file
    sources_file = open(SOURCES_FILE, 'wb')
    dump(sources, sources_file)

    # Saving years to file
    years_file = open(YEARS_FILE, 'wb')
    dump(years, years_file)

    # Saving news to file
    news_file = open(NEWS_FILE, 'wb')
    dump(news, news_file)
  finally:
    sources_file.close()
    years_file.close()
    news_file.close()
  
  printExecutionTime(start_time)
  return sources, years, news

def preProcess(docs):
  print('Pre-processing...')
  start_time = time()

  try:
    # Loading if possible
    f = open(PROCESSED_NEWS_FILE, 'rb')
    processed_docs = load(f)
  except:
    stop_words = STOPWORDS
    stemmer = SnowballStemmer('english')
    lemmatizer = WordNetLemmatizer()

    processed_docs = []
    for doc in docs:
      processed_doc = []
      for token in simple_preprocess(doc, deacc=True):
        if token not in stop_words and len(token) > 2:
          token = lemmatizer.lemmatize(token, pos='v')
          #token = stemmer.stem(token)
          processed_doc.append(token)
      processed_docs.append(processed_doc)

    # Saving results to file
    f = open(PROCESSED_NEWS_FILE, 'wb')
    dump(processed_docs, f)
  finally:
    f.close()

  printExecutionTime(start_time)
  return processed_docs

def extractDictionary(documents):
  print('Extracting dictionary...')
  start_time = time()

  try:
    # Loading if possible
    dictionary = Dictionary.load(DICTIONARY_FILE)
  except:
    dictionary = Dictionary(documents)
    dictionary.filter_extremes(no_below=200, no_above=0.8, keep_n=4000)

    # Saving to file
    dictionary.save(DICTIONARY_FILE)

  printExecutionTime(start_time)
  return dictionary

def extractFeatures(documents, dictionary):
  print('Extracting features...')
  start_time = time()
  
  try:
    # Loading if possible
    f = open(TFIDF_FILE, 'rb')
    tfidf_corpus = load(f)
  except:
    bow_corpus = [ dictionary.doc2bow(doc) for doc in documents ]
    tfidf = TfidfModel(bow_corpus)
    tfidf_corpus = tfidf[bow_corpus]

    # Saving to file
    f = open(TFIDF_FILE, 'wb')
    dump(tfidf_corpus, f)
  finally:
    f.close()

  printExecutionTime(start_time)
  return tfidf_corpus

def generateAuthorTopicModel(corpus, dictionary, authors):
  print('Generating author-topic model...')
  start_time = time()

  try:
    # Loading if possible
    model = AuthorTopicModel.load(MODEL_FILE)
  except:
    model = AuthorTopicModel(
      corpus,
      num_topics=20,
      id2word=dictionary,
      author2doc=authors
    )

    # Saving to file
    model.save(MODEL_FILE)
  
  printExecutionTime(start_time)
  return model

if __name__ == '__main__':
  sources, years, news = loadData()
  processed_news = preProcess(news)
  del news

  dictionary = extractDictionary(processed_news)
  tfidf = extractFeatures(processed_news, dictionary)
  del processed_news

  model = generateAuthorTopicModel(tfidf.corpus, dictionary, sources)
  del tfidf

  print('Topics')
  for idx, topic in model.print_topics(-1):
    print('Topic {}: {}'.format(idx, topic))

  print('\nAuthors')
  for author in model.id2author.values():
    print('{}: {}'.format(author, model.get_author_topics(author)))