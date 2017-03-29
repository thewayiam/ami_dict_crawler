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
爬阿美語
```
scrapy runspider crawler.py -t json -o data/ami.json 
```
### 其他族語
請將`{代號}`換成需要的族語
```
scrapy runspider crawler.py -t json -o data/{代號}.json -a lang={代號}
```
#### 代號別
```
阿美語 ami
泰雅語 tay
排灣語 pwn
布農語 bnn
卑南語 pyu
魯凱語 dru
鄒語 tsu
賽夏語 xsy
雅美語 tao
邵語 ssf
噶瑪蘭語 ckv
太魯閣語 trv
撒奇萊雅語 ais
賽德克語 sdq
拉阿魯哇語 sxr
卡那卡那富語 xnb
```
