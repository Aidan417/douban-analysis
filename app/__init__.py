from flask import Flask, render_template, request
import pandas as pd
import math
import os

def find_csv_file(filename='douban_top250.csv', search_dir=None):
    if search_dir is None:
        search_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for root, dirs, files in os.walk(search_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

DATA_PATH = find_csv_file()
if DATA_PATH is None:
    raise FileNotFoundError("找不到 douban_top250.csv 文件，请确认文件存在项目目录下。")

print(f"自动找到文件路径：{DATA_PATH}")

app = Flask(__name__)
df = pd.read_csv(DATA_PATH)

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('keyword', '').strip()
    sort = request.args.get('sort', 'score_desc')
    page = int(request.args.get('page', 1))
    per_page = 10

    if keyword:
        filtered_df = df[df['标题'].str.contains(keyword, case=False, na=False)]
    else:
        filtered_df = df

    sort_map = {
        'title_asc': ('标题', True),
        'title_desc': ('标题', False),
        'score_asc': ('评分', True),
        'score_desc': ('评分', False),
    }
    sort_column, ascending = sort_map.get(sort, ('评分', False))
    sorted_df = filtered_df.sort_values(by=sort_column, ascending=ascending)

    total = len(sorted_df)
    total_pages = math.ceil(total / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    page_data = sorted_df.iloc[start:end]

    movies = page_data.to_dict(orient='records')

    return render_template(
        'index.html',
        movies=movies,
        movie_count=total,
        keyword=keyword,
        sort=sort,
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=True)
