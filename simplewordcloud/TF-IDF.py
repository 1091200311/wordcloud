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
import re #�������
import collections #��Ƶͳ�ƿ�
import wordcloud #����
from PIL import Image # ͼ�����
import matplotlib.pyplot as plt # ͼ��չʾ��
