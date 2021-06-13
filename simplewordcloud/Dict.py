# -*- coding: utf-8 -*-
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
with open('出师表.txt', encoding="utf-8") as f:
    content = f.read()
    tags = jieba.analyse.textrank(content, topK=10, withWeight=True)
    wordcloud = WordCloud(font_path='msyh.ttc',
                          background_color="white",
                          width=800,
                          height=600)
    wordcloud.generate_from_frequencies(dict(tags))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
wordcloud.to_file('out8.png')
