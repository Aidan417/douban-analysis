# 豆瓣 Top250 电影数据分析与可视化平台

本项目以豆瓣 Top250 电影数据为基础，结合 **数据分析**、**可视化**、**Web 应用开发**，构建了一个完整的从数据洞察到用户交互的分析平台，支持本地运行分析脚本、交互式浏览（Streamlit）、以及 Web 接口调用（Flask）。

## 项目亮点

数据分析：使用 Pandas、Matplotlib/Seaborn 等工具，深入分析电影类型、评分人数、年份趋势等特征。  
可视化平台（Streamlit）：构建交互式数据探索前端，支持动态筛选、可视化图表等操作。  
后端接口（Flask）：提供 API 接口支持前后端解耦、部署与集成。  
项目可扩展：支持接入更多数据源（如 IMDb、猫眼等）与分析维度。

---

## 快速开始

### 1️安装依赖

建议使用虚拟环境：

```bash
python -m venv venv
source venv/bin/activate   # Windows 用 venv\Scripts\activate
pip install -r requirements.txt
````

### 2️运行分析脚本（可选）

你可以在 `notebooks/` 中逐个运行分析代码：

```bash
jupyter notebook
```

---

## 3Streamlit 可视化平台

项目通过 **Streamlit** 构建交互式数据浏览前端，支持：

* 筛选特定类型/年份的电影；
* 显示评分人数、年份趋势、评分排行榜；
* 图表动态更新与响应式布局。

### 启动 Streamlit：

```bash
cd app
streamlit run app.py
```

然后浏览器中打开 `http://localhost:8501`。

---

## 🔌 Flask API 接口服务

项目还提供基于 **Flask** 的后端接口，供其他应用调用：

### 启动 Flask 接口：

```bash
cd api
python server.py
```

示例接口（GET）：

```
http://localhost:5000/api/top_movies?limit=10
http://localhost:5000/api/score_trend
```

你可以将其部署到云服务器或结合前端框架使用。


##  分析模块一览

| 模块            | 内容概要           |
| ------------- | -------------- |
| 类型分布分析        | 统计并可视化最受欢迎电影类型 |
| 评分人数分析        | 识别热度与口碑的关系     |
| 年份趋势分析        | 探索豆瓣评分随时间的变化趋势 |
| 综合评分排行榜（加权算法） | 构建评分×评分人数的公平排序 |

---

## TODO（可拓展方向）

* [ ] 添加 IMDb / 豆瓣实时接口爬虫模块
* [ ] 增加 Streamlit 多页面支持
* [ ] 添加 ECharts / Plotly 高级图表
* [ ] 多语言版本（中英）

---

## License

本项目遵循 MIT 开源协议，数据仅供学习与研究使用，禁止用于商业用途。
