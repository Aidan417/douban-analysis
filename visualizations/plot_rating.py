import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/douban_top250.csv')
df['评分'] = df['评分'].astype(float)

plt.figure(figsize=(8, 5))
sns.histplot(df['评分'], bins=10, kde=True)
plt.title('豆瓣Top250评分分布')
plt.xlabel('评分')
plt.ylabel('电影数量')
plt.grid(True)
plt.tight_layout()
plt.savefig('../visualizations/评分分布图.png')
plt.show()
