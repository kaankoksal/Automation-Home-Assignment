import subprocess
import os

def runSpider(
    spider_dir="imdb_cast", 
    spider="cast_spider", 
    f="output.csv"
    ):
    os.chdir(spider_dir)
    subprocess.call(["scrapy", "crawl", spider, "-o", f])
    os.chdir("..")

