import wordcloud
import jieba
import imageio
f = open('出师表.txt',encoding='utf-8')
txt = f.read()
txtList = jieba.lcut(txt)
string = "".join(txtList)
mk = imageio.imread("wujiaoxing.png")
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15
                        )
w.generate(string)
w.to_file('out3.png')

