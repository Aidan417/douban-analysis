import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DATA_PATH

import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

def main():
    movies = []
    for start in range(0, 250, 25):
        url = f"https://movie.douban.com/top250?start={start}"
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.find_all('div', class_='item')

        for item in items:
            title = item.find('span', class_='title').text
            rating = item.find('span', class_='rating_num').text
            info = item.find('div', class_='bd').p.text.strip().replace('\n', ' ')
            movies.append([title, rating, info])

        time.sleep(1)  # 防止被封

    # 保存数据
    with open(DATA_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['标题', '评分', '信息'])
        writer.writerows(movies)

    print("✅ 数据爬取完成，已保存至 data/douban_top250.csv")

if __name__ == "__main__":
    main()
