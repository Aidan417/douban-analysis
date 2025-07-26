# app/app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

# 页面配置
st.set_page_config(page_title='豆瓣Top250电影分析', layout='wide')

# 自动拼接路径（确保找得到文件）
base_path = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(base_path, '..', 'data', 'douban_top250.csv'))

# 加载数据
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"未找到数据文件，请确认文件存在于: {csv_path}")
    st.stop()

# 数据预处理
df['评分'] = df['评分'].astype(float)

# 提取年份
df['年份'] = df['信息'].apply(
    lambda x: re.search(r'(\d{4})', x).group(1) if re.search(r'(\d{4})', x) else '未知'
)

# 🎉 页面标题
st.title('🎬 豆瓣Top250电影分析仪表盘')

# 🔍 原始数据展示
with st.expander("📄 点击查看原始数据"):
    st.dataframe(df.head(10))

# 📊 评分分布图
st.subheader('🎯 评分分布图')
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.histplot(df['评分'], bins=10, kde=True, ax=ax1, color='skyblue')
ax1.set_xlabel('评分')
ax1.set_ylabel('电影数量')
st.pyplot(fig1)

# 📅 上映年份分布
st.subheader('📆 上映年份分布图')
df['年份'] = df['年份'].astype(str)
year_counts = df['年份'].value_counts().sort_index()

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax2, palette='viridis')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
ax2.set_xlabel('年份')
ax2.set_ylabel('电影数量')
st.pyplot(fig2)

# ✅ 底部说明
st.markdown("---")
st.markdown("📌 数据来源：[豆瓣电影Top250](https://movie.douban.com/top250/)")
st.markdown("👨‍💻 项目作者：Aidan")
