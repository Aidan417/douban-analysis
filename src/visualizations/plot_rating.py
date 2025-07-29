import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib.font_manager import FontProperties
from config import IMAGE_DIR

def plot(csv_path, image_dir=IMAGE_DIR):
    df = pd.read_csv(csv_path)

    font = FontProperties(fname="C:/Windows/Fonts/simhei.ttf")

    plt.figure(figsize=(8, 6))
    plt.hist(df['评分'].astype(float), bins=10, edgecolor='black')
    plt.title('豆瓣Top250电影评分分布', fontproperties=font)
    plt.xlabel('评分', fontproperties=font)
    plt.ylabel('电影数量', fontproperties=font)

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    plt.savefig(os.path.join(image_dir, 'rating_hist.png'))
    plt.close()
