# -*- coding: utf-8 -*-
import jieba.analyse
f = open('1.txt',encoding='utf-8')
txt = f.read()
keywords = jieba.analyse.extract_tags(txt, topK=5, withWeight=True, allowPOS=())
print(keywords)

