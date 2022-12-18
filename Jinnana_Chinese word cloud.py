Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Put this python file into the same folder with Chinese txt files for creating word clouds.
... 
... import os
... import pynlpir
... from nltk import FreqDist
... import matplotlib.pyplot as plt
... import wordcloud
... from wordcloud import WordCloud
... from wordcloud import ImageColorGenerator
... import numpy as np
... from PIL import Image
... 
... filelist = os.listdir()
... 
... ## Chinese txt file separated into words (#filename)
... with open('#filename.txt',encoding='utf-8') as f:
...     words=f.read()
...     bow = words.split()
... 
... ## User's stopwords as txt file (#stopwords.txt)  
... with open('#stopwords.txt',encoding='utf-8') as f:
...     stopwords = f.read().splitlines()
... 
... ## Can use custom stopwords when you need more stopwords in each wordcloud (#stopword) 
...     custom_stopwords = ['#stopword','#stopword','#stopword','#stopword','#stopword']
... 
...     
... bow_new = [word for word in bow if word not in stopwords + custom_stopwords]
... 
... 
... plt.rcParams['font.family'] = ['simsun']
... fdist = FreqDist(bow_new)
... 
... ## Put specific path(#path) of the image file(#img_name.png) 
##(e.g.C:\Users\Username\imgfolder\image_name.png)
mask = np.array(Image.open(r'#path\#img_name.png')) 
image_colors = ImageColorGenerator(mask)

wc = WordCloud(font_path=r'C:\Windows\Fonts\simsun.ttc',
               width=2000, height=1000,mask=mask, color_func=image_colors,
               repeat=True, background_color='rgba(255, 255, 255, 200)', mode='RGBA',
## You can adjust the random_state number(usually from 24 to 80) to change random arrangement of words in the wordcloud. 
               random_state=60,
               max_font_size=200, min_font_size=20).generate_from_frequencies(fdist)

fig = plt.figure(figsize=(20,10))

plt.imshow(wc, interpolation='hanning')
plt.tight_layout(pad=0)

plt.axis('off')

plt.show()
## Put a new name of the wordcloud as saving (#save_as_wordcloud)
fig.savefig('#save_as_wordcloud.png')
