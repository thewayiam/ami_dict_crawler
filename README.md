# ami_dict_crawler
crawler of http://e-dictionary.apc.gov.tw/ami/Search.htm

JSON output: https://thewayiam.github.io/ami_dict_crawler/data/data.json

## 抓

裝[chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)，而且放佇`PATH`
```
sudo apt-get install -y xvfb
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install scrapy selenium pyvirtualdisplay
```
下載
```
scrapy runspider crawler.py -t json -o ami.json
 
```
