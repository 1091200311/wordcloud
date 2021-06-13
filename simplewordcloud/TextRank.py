# -*- coding: utf-8 -*-
import jieba
from jieba import analyse
with open('出师表.txt', encoding="utf-8") as f:
    content = f.read()
    tags = jieba.analyse.extract_tags(content, topK=4, withWeight=True)
print(tags)
