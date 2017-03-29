# ami_dict_crawler
crawler of http://e-dictionary.apc.gov.tw/ami/Search.htm

JSON output: https://thewayiam.github.io/ami_dict_crawler/data/data.json

## 抓
### Chrome driver
裝[chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)，而且放佇`PATH`
```
echo 'check latest version of driver:'
curl "http://chromedriver.storage.googleapis.com/LATEST_RELEASE"
sudo mkdir /var/chromedriver && cd /var/chromedriver
echo 'replace version number in below link, we use 2.28 in this moment'
sudo wget "http://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip"
sudo unzip chromedriver_linux64.zip
```
### 安裝
```
sudo apt-get install -y xvfb libpython3-dev
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip # 設置環境檔
pip install scrapy selenium pyvirtualdisplay
```
爬阿美語
```
scrapy runspider crawler.py -t json -o data/ami.json 
```

### 其他族語
請將`{代號}`換成需要的族語，預設為`阿美語`
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
#### 阿美語 ami
```
scrapy runspider crawler.py -t json -o data/ami.json -a lang=ami
```
#### 泰雅語 tay
```
scrapy runspider crawler.py -t json -o data/tay.json -a lang=tay
```
#### 排灣語 pwn
```
scrapy runspider crawler.py -t json -o data/pwn.json -a lang=pwn
```
#### 布農語 bnn
```
scrapy runspider crawler.py -t json -o data/bnn.json -a lang=bnn
```
#### 卑南語 pyu
```
scrapy runspider crawler.py -t json -o data/pyu.json -a lang=pyu
```
#### 魯凱語 dru
```
scrapy runspider crawler.py -t json -o data/dru.json -a lang=dru
```
#### 鄒語 tsu
```
scrapy runspider crawler.py -t json -o data/tsu.json -a lang=tsu
```
#### 賽夏語 xsy
```
scrapy runspider crawler.py -t json -o data/xsy.json -a lang=xsy
```
#### 雅美語 tao
```
scrapy runspider crawler.py -t json -o data/tao.json -a lang=tao
```
#### 邵語 ssf
```
scrapy runspider crawler.py -t json -o data/ssf.json -a lang=ssf
```
#### 噶瑪蘭語 ckv
```
scrapy runspider crawler.py -t json -o data/ckv.json -a lang=ckv
```
#### 太魯閣語 trv
```
scrapy runspider crawler.py -t json -o data/trv.json -a lang=trv
```
#### 撒奇萊雅語 ais
```
scrapy runspider crawler.py -t json -o data/ais.json -a lang=ais
```
#### 賽德克語 sdq
```
scrapy runspider crawler.py -t json -o data/sdq.json -a lang=sdq
```
#### 拉阿魯哇語 sxr
```
scrapy runspider crawler.py -t json -o data/sxr.json -a lang=sxr
```
#### 卡那卡那富語 xnb
```
scrapy runspider crawler.py -t json -o data/xnb.json -a lang=xnb
```
