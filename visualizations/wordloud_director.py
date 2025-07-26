import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('../data/douban_top250.csv')

# 提取导演名（info 中第一个斜杠前的文字）
directors = df['信息'].apply(lambda x: x.split('/')[0].strip())
text = ' '.join(directors)

wc = WordCloud(font_path='msyh.ttc', width=800, height=400, background_color='white').generate(text)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('导演词云')
plt.savefig('../visualizations/导演词云.png')
plt.show()
