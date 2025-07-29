from spider import douban_spider
from analysis import data_analysis
from visualizations import plot_rating, plot_year_trend, plot_genre, plot_score_vs_year
from config import DATA_PATH, IMAGE_DIR

def run_all():
    print("✅ 数据爬取完成，已保存至", DATA_PATH)
    print("DATA_PATH:", DATA_PATH)
    print("DEBUG:", True)
    print("Step 1: 正在抓取数据...")
    douban_spider.main()  # 假设你爬虫有main函数

    print("Step 2: 数据分析中...")
    data_analysis.analyze()

    print("Step 3: 生成评分直方图...")
    plot_rating.plot(DATA_PATH, IMAGE_DIR)

    print("Step 4: 生成年份趋势图...")
    plot_year_trend.plot(DATA_PATH, IMAGE_DIR)

    print("Step 5: 生成类型分布饼图...")
    plot_genre.plot(DATA_PATH, IMAGE_DIR)

    print("Step 6: 生成评分和年份关系散点图...")
    plot_score_vs_year.plot(DATA_PATH, IMAGE_DIR)

    print("✅ 全部步骤完成")

if __name__ == '__main__':
    run_all()
