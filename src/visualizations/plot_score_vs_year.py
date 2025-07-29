import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from matplotlib.font_manager import FontProperties
from config import IMAGE_DIR

def extract_year(info):
    matches = re.findall(r'(\d{4})', info)
    if matches:
        return int(matches[-1])
    return None

def plot(csv_path, image_dir=IMAGE_DIR):
    df = pd.read_csv(csv_path)

    df['年份'] = df['信息'].apply(extract_year)
    df = df.dropna(subset=['年份', '评分'])
    df['年份'] = df['年份'].astype(int)
    df['评分'] = df['评分'].astype(float)

    font = FontProperties(fname="C:/Windows/Fonts/simhei.ttf")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['年份'], df['评分'], alpha=0.7)
    plt.title('豆瓣Top250电影评分与年份关系', fontproperties=font)
    plt.xlabel('年份', fontproperties=font)
    plt.ylabel('评分', fontproperties=font)
    plt.grid(True)

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    plt.savefig(os.path.join(image_dir, 'score_vs_year.png'))
    plt.close()
