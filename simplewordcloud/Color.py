# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import imageio
text = open('三国演义.txt',encoding='utf-8').read
mk = imageio.read('wujiaoxing.png')
wc = WordCloud(background_color='white',mask=mk)
wc.generate(text)
image_colors = ImageColorGenerator(mk)
fig,axes = plt.subplots(1,3)
axes[0].imshow(wc)
axes[1].imshow(wc.recolor(color_func=image_colors),interpolation="bilinear")
axes[2].imshow(mk,cmap=plt.cm.gray)
for ax in axes:
    ax.set_axis_off()
    plt.show()
wc_color = wc.recolor(color_func=image_colors)
wc_color.to_file('output6.png')


