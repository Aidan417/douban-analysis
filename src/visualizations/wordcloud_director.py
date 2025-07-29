import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import re
from matplotlib.font_manager import FontProperties

def plot(csv_path, image_dir):
    df = pd.read_csv(csv_path)

    # 提取导演名字（示例正则，可能需根据实际数据调整）
    pattern = re.compile(r'导演:\s*([^  ]+)')  # 中文全角空格
    directors = []
    for info in df['信息']:
        match = pattern.search(info)
        if match:
            directors.append(match.group(1))
        else:
            directors.append('未知')
    df['导演'] = directors

    text = " ".join(df['导演'].dropna().tolist())

    font_path = "C:/Windows/Fonts/simhei.ttf"

    wordcloud = WordCloud(
        font_path=font_path,
        width=800, height=400,
        background_color='white'
    ).generate(text)

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(os.path.join(image_dir, 'director_wordcloud.png'))
    plt.close()
