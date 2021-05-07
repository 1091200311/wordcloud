# -*- coding: utf-8 -*-
import wordcloud
import jieba
f = open('中英文本.txt',encoding='utf-8')
txt = f.read()
txtList = jieba.lcut(txt)
string = "".join(txtList)
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',)
w.generate(string)
w.to_file('out4.png')
