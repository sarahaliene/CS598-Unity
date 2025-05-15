###############################################################
#All the imports for sentiment analysis & text processing
import UnityEngine
import nltk
import datetime
import os

#String operations for preprocessing text
import string

#Stopwords to remove
from nltk.corpus import stopwords as stopwords
stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
numbers = ["0","1","2","3","4","5","6","7","8","9"]

#Word tokenizer
#Use nltk.word_tokenize(line of words)
from nltk.tokenize import word_tokenize

#Word stemmer
#from nltk.stem.snowball import EnglishStemmer

#NLTK Sentiment Analyzer tool
from nltk.sentiment import sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from nltk.sentiment.vader import SentiText

#For counting occurences of things in general
from collections import Counter

#nltk.download('punkt_tab')
#nltk.download('stopwords')
nltk.download('subjectivity')
nltk.download('vader_lexicon')

################################################################

#Needs to be set up as class
#Use stemmer.stem(word)
#stemmer = EnglishStemmer()
sia = SentimentIntensityAnalyzer()
#st = SentiText()


def journal_entry(file_name):

    file = open(file_name, "r")

    todays_date = datetime.datetime.now()
    
    #string_today represents the general month day, year
    #This should make it easier to search for entries by date
    string_today = todays_date.strftime("%B %d, %Y")

    content = file.read()

    score = sia.polarity_scores(content)    

    pos = score["pos"]
    neu = score["neu"]
    neg = score["neg"]
    compound = score["compound"]

    #Split up just to make it more readable
    #score_entry1 = "For " + string_today + ", your compound polarity score was " str(compound) + ". "
    #score_entry2 = "Broken down, your positive score was " + str(pos) + ", your negative score was " + str(neg) + ", and your neutral score was " + str(neu) + ". "
    #score_entry3 = "A score of greater than 0.5 indicates positive sentiment, while a score of less than -0.5 indicates negative sentiment. "
    #score_entry4 = "A score of -0.5 through 0.5 indicates neutral sentiment. "
    #score_entry5 = "This score has been calculated using the NLTK Vader Sentiment Intensity Analyzer: "
    #score_entry6 = "Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014."
    #score_text = score_entry1 + score_entry2 + score_entry3 + score_entry4 + score_entry5 + score_entry6

    string_score = str(score)
    UnityEngine.PlayerPrefs.SetString("score", string_score)
    UnityEngine.PlayerPrefs.SetString("date", string_today)
    UnityEngine.PlayerPrefs.SetFloat("compound", compound)
    UnityEngine.PlayerPrefs.SetString("compoundstring", str(compound))
    UnityEngine.PlayerPrefs.SetFloat("pos", pos)
    UnityEngine.PlayerPrefs.SetFloat("neg", neg)
    UnityEngine.PlayerPrefs.SetFloat("neu", neu)
    #UnityEngine.PlayerPrefs.SetString("scoretextentry", score_text)


journal_entry("entry.txt")