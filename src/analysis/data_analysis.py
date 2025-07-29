import pandas as pd
from config import DATA_PATH

def analyze():
    df = pd.read_csv(DATA_PATH)
    print(f"数据读取成功，共有电影数量： {len(df)}")
    print(df[['标题', '评分', '信息']].head())
