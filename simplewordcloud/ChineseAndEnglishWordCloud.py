# -*- coding: utf-8 -*-
import wordcloud
import jieba.analyse
f = open('出师表.txt',encoding='utf-8')
txt = f.read()
keywords1=jieba.analyse.textrank(txt,topK=10,withWeight=True)
print(keywords1)
#print('关键词提取'+"/".join(keywords1))#有时不确定提取多少关键词，可利用总词的百分比
# print('总词数{}'.format(len(list(jieba.cut(txt)))))
# txtList = jieba.lcut(txt)
# print(txtList)
# string = "".join(txtList)
# w = wordcloud.WordCloud(width=1000,
#                         height=700,
#                         background_color='white',
#                         font_path='msyh.ttc',)
# w.generate(string)
# w.to_file('out4.png')
