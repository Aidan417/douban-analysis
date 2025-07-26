import pandas as pd
import re

df = pd.read_csv('../data/douban_top250.csv')

# 提取年份
df['年份'] = df['信息'].apply(lambda x: re.search(r'(\d{4})', x).group(1) if re.search(r'(\d{4})', x) else None)

# 显示前几行
print(df[['标题', '评分', '年份']].head())
