import numpy
import nltk.classify.util
from nltk.classify import NaiveBayesClassifer
from nltk.corpus import movie_reviews

def extract_features(word_list):
     return dict([(word,True) for word in word_list])
     


positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')

features_positive = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in positive_fileids]
features_negative= [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in negative_fileids]

threshold_factor = 0.8
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))