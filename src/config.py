import os
from dotenv import load_dotenv

# 加载 .env 文件（要确保你有 .env 文件放在项目根目录）
load_dotenv()

# 读取路径变量，默认值是data/douban_top250.csv（相对路径）
DATA_PATH = os.getenv("CSV_PATH", "data/douban_top250.csv")

# DEBUG 读取环境变量，转换成布尔值
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 项目根目录（一般是config.py的上上级目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径，绝对路径更安全
LOG_PATH = os.path.join(BASE_DIR, "logs", "project.log")

# 输出文件目录（相对路径），并确保目录存在
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 图片文件夹绝对路径，并确保目录存在
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)
