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
    df = df.dropna(subset=['年份'])
    df['年份'] = df['年份'].astype(int)

    font = FontProperties(fname="C:/Windows/Fonts/simhei.ttf")

    year_counts = df['年份'].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    plt.plot(year_counts.index, year_counts.values, marker='o')
    plt.title('豆瓣Top250电影年份分布趋势', fontproperties=font)
    plt.xlabel('年份', fontproperties=font)
    plt.ylabel('电影数量', fontproperties=font)
    plt.grid(True)

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    plt.tight_layout()
    plt.savefig(os.path.join(image_dir, 'year_trend.png'))
    plt.close()
