import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def plot(data_path, image_dir):
    # 读取CSV数据
    df = pd.read_csv(data_path)

    # 假设电影类型信息存储在“信息”列里，类似 "1994 / 美国 / 犯罪 剧情"
    # 这里我们尝试提取类型关键词，比如“犯罪”“剧情”等
    # 先定义一个辅助函数，提取类型字符串最后一部分（根据实际格式调整）
    def extract_genres(info):
        # 以斜杠分割取最后一段，再用空格分割得到多个类型
        try:
            genres_part = info.split('/')[-1].strip()
            # 分割空格或中文空格
            genres = genres_part.replace('\xa0', ' ').split()
            return genres
        except Exception:
            return []

    # 应用函数，提取所有电影类型
    df['类型列表'] = df['信息'].apply(extract_genres)

    # 统计所有类型出现频率（扁平化列表）
    all_genres = []
    for genres in df['类型列表']:
        all_genres.extend(genres)

    genre_counts = pd.Series(all_genres).value_counts()

    # 设置中文字体，避免乱码（Windows示例）
    font = FontProperties(fname="C:/Windows/Fonts/simhei.ttf", size=12)

    plt.figure(figsize=(12, 6))
    genre_counts.plot(kind='bar', color='skyblue')

    plt.title('豆瓣Top250电影类型分布', fontproperties=font)
    plt.xlabel('电影类型', fontproperties=font)
    plt.ylabel('数量', fontproperties=font)
    plt.xticks(fontproperties=font, rotation=45, ha='right')
    plt.tight_layout()

    # 确保保存目录存在
    os.makedirs(image_dir, exist_ok=True)
    plt.savefig(os.path.join(image_dir, 'genre_distribution.png'))
    plt.close()
