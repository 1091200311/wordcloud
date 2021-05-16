import pandas as pd
import time
import lightgbm as lg
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import os
import os.path
import jieba
import re #正则表达库
import collections #词频统计库
import wordcloud #词云
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
