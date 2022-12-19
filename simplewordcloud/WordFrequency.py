# -*- coding: utf-8 -*-
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import collections
with open('出师表.txt', encoding="utf-8") as f:
    content = f.read()
    txt=jieba.cut(content)
wc = WordCloud(font_path='msyh.ttc',
             background_color='white',
             max_words=100,
             max_font_size=100,
             width=1000,height=800,margin=2)
wc.generate_from_frequencies(txt)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
wc.to_file("wordCount.png")
