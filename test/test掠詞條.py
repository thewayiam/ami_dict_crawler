from unittest.case import TestCase

from crawler import Spider
from scrapy.selector import Selector
import scrapy


class 掠網頁試驗(TestCase):

    #     def test_系統維護中(self):
    #         self.系統維護中回應
    #         self.fail()

    def test_正常詞條(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm', body=self.正常回應.encode(), encoding='utf-8')
        aa = Spider()
        結果 = aa.掠詞條(rr)
        self.assertIn('examples', 結果)
        self.assertEqual(結果['name'], "a:su'")
        self.assertEqual(結果['source'], "asu'")
        self.assertEqual(
            結果['pronounce'], "http://e-dictionary.apc.gov.tw/MultiMedia/Audio/ais/a：su'_{1}.mp3")
        self.assertEqual(結果['frequency'], '詞頻：★(1)')

    def test_有例句詞條(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm', body=self.例句回應.encode(), encoding='utf-8')
        aa = Spider()
        結果 = aa.掠詞條(rr)
        答案 = {
            "source": "ahowid",
            "pronounce": "http://e-dictionary.apc.gov.tw/MultiMedia/Audio/ami/aahowiden_{1}.mp3",
            "frequency": "詞頻：★(1)",
            "examples": [
                {
                    "pronounce": "http://e-dictionary.apc.gov.tw/MultiMedia/Audio/ami/aahowiden_{1}_@_1.1.mp3",
                    "sentence": "O aahowiden no mita ko pasifana'ay a singsi.",
                      "zh_Hant": "教導我們的老師是值得我們感謝的。",
                    "description": "解釋1：值得去感謝者"
                }
            ],
            "name": "aahowiden"
        }
        self.assertEqual(結果,答案)

    系統維護中回應 = '<div align=center>系統維護中，請稍候再試!</div>'
    正常回應 = '''

<div id="oGHC_Deatail">
    <div id="oGHC_FB"></div>
    <div id="oGHC_Term_Area" class="words">
        
        <div id="oGHC_Term" class="term"><span>a:su'</span><a class="play" rel="/MultiMedia/Audio/ais/a：su'_{1}.mp3" href="javascript:void(0);"><img title="播放詞項" class="img_audio" src="/images/speaker.gif" alt="播放詞項" style="border-width:0px;" /></a></div>
        
        <div id="oGHC_Freq" class="freq">詞頻：<span class="term_freq">★</span>(1)</div>
        <div id="oGHC_Source" class="source">來源：<a href="javascript:void(0)" class="ws_term" rel="290876">asu'</a>　/　<a href="javascript:void(0)" class="troot" rel="a:su'">詞根結構▼</a></div>
    </div>
    <hr class="spline" />
    <div class="e_con">
        
        <div class="concon">
            
            <div class="block"><div><strong>解釋1</strong>：很好吃（表示強調語氣）</div><div class="word_detail"><table class="tb06"><tr class="st"><td><a href="javascript:void(0)" title="1.很好吃（表示強調語氣）" rel="293101" class="dsl_term">a:su'</a> <a href="javascript:void(0)" title="1.人名,2.普通名詞主格格位標記" rel="291598,291599" class="dsl_term">ku</a> <a href="javascript:void(0)" title="1.果實" rel="291362" class="dsl_term">heci</a> <a href="javascript:void(0)" title="1.普通名詞屬格格位標記" rel="292006" class="dsl_term">nu</a> <a href="javascript:void(0)" title="1.花蓮縣壽豐鄉月眉村,2.麵包樹" rel="290859,290860" class="dsl_term">apalu</a> pahipuwan.  </td></tr><tr><td>麵包果放小魚干很好吃。</td></tr></table></div></div>
            
            
            
            
            
            
            
            
            
            <div id="oGHC_Opinion" class="op293101"></div>
        </div>
        
        <div class="history">
            
            <div id="oGHC_Image" class="pic"></div>
            <div id="oGHC_History" class="hislist"><table class="tbhis"><th>瀏覽歷程</th><tr><td><a href="javascript:void(0)" rel="292913" class="his_term">aadupen</td></tr><tr><td><a href="javascript:void(0)" rel="293101" class="his_term">a:su'</td></tr><tr><td><a href="javascript:void(0)" rel="292806" class="his_term">aam</td></tr><tr><td><a href="javascript:void(0)" rel="290904" class="his_term">Babah</td></tr><tr><td><a href="javascript:void(0)" rel="291328" class="his_term">gaciw</td></tr><tr><td><a href="javascript:void(0)" rel="295590" class="his_term">masamel</td></tr><tr><td><a href="javascript:void(0)" rel="295168" class="his_term">masamalebulebut</td></tr><tr><td><a href="javascript:void(0)" rel="295586" class="his_term">masaluimeng</td></tr><tr><td><a href="javascript:void(0)" rel="292823" class="his_term">maabibi</td></tr></table></div>
        </div>
        
    </div>
</div>
<div id="oGHC_PopWin" class="pop_up"></div>
<div id="oGHC_TermsTree" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="290876" title="1.好吃">asu'</a>　<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="293101" title="1.很好吃（表示強調語氣）">a:su'</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293102" title="1.好吃的">asu'ay<sub>1</sub></a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293103" title="1.營養的">asu'ay<sub>2</sub></a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293104" title="1.覺得好吃命令）">asu'en</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293105" title="1.難吃">caykaasu'</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293106" title="1.講大話的">paasu'ay</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293107" title="1.最好吃的">saasu'ay</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293108" title="1.有好吃的">siasu'ay</a>　<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeDE" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="290876">asu'</a>　1.好吃<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="293101">a:su'</a>　1.很好吃（表示強調語氣）<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293102">asu'ay<sub>1</sub></a>　1.好吃的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293103">asu'ay<sub>2</sub></a>　1.營養的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293104">asu'en</a>　1.覺得好吃命令）<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293105">caykaasu'</a>　1.難吃<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293106">paasu'ay</a>　1.講大話的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293107">saasu'ay</a>　1.最好吃的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293108">siasu'ay</a>　1.有好吃的<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeSer" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="290876">asu'</a>　1.好吃<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="293101">a:su'</a>　1.很好吃（表示強調語氣）<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293102">asu'ay<sub>1</sub></a>　1.好吃的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293103">asu'ay<sub>2</sub></a>　1.營養的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293104">asu'en</a>　1.覺得好吃命令）<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293105">caykaasu'</a>　1.難吃<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293106">paasu'ay</a>　1.講大話的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293107">saasu'ay</a>　1.最好吃的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="293108">siasu'ay</a>　1.有好吃的<ul></li></ul></li></ul></div>
'''
    例句回應 = '''

<div id="oGHC_Deatail">
    <div id="oGHC_FB"></div>
    <div id="oGHC_Term_Area" class="words">
        
        <div id="oGHC_Term" class="term"><span>aahowiden</span><a class="play" rel="/MultiMedia/Audio/ami/aahowiden_{1}.mp3" href="javascript:void(0);"><img title="播放詞項" class="img_audio" src="/images/speaker.gif" alt="播放詞項" style="border-width:0px;" /></a></div>
        
        <div id="oGHC_Freq" class="freq">詞頻：<span class="term_freq">★</span>(1)</div>
        <div id="oGHC_Source" class="source">來源：<a href="javascript:void(0)" class="ws_term" rel="254511">ahowid</a>　/　<a href="javascript:void(0)" class="troot" rel="aahowiden">詞根結構▼</a></div>
    </div>
    <hr class="spline" />
    <div class="e_con">
        
        <div class="concon">
            
            <div class="block"><div><strong>解釋1</strong>：值得去感謝者</div><div class="word_detail"><table class="tb06"><tr class="st"><td>O <a href="javascript:void(0)" title="1.值得去感謝者" rel="256440" class="dsl_term">aahowiden</a> <a href="javascript:void(0)" title="1.格位標記（屬格）" rel="255742" class="dsl_term">no</a> <a href="javascript:void(0)" title="1.我們（包含式；屬格）" rel="258675" class="dsl_term">mita</a> <a href="javascript:void(0)" title="1.格位標記（主格）" rel="255421" class="dsl_term">ko</a> pasifana'ay a <a href="javascript:void(0)" title="1.老師" rel="256087" class="dsl_term">singsi</a>. <a class="play" rel="/MultiMedia/Audio/ami/aahowiden_{1}_@_1.1.mp3" href="javascript:void(0);"><img title="播放例句" class="img_audio" src="/images/speaker.gif" alt="播放例句" style="border-width:0px;" /></a></td></tr><tr><td>教導我們的老師是值得我們感謝的。</td></tr></table></div></div>
            
            
            
            
            
            
            
            
            
            <div id="oGHC_Opinion" class="op256440"></div>
        </div>
        
        <div class="history">
            
            <div id="oGHC_Image" class="pic"></div>
            <div id="oGHC_History" class="hislist"><table class="tbhis"><th>瀏覽歷程</th><tr><td><a href="javascript:void(0)" rel="254511" class="his_term">ahowid</td></tr><tr><td><a href="javascript:void(0)" rel="256440" class="his_term">aahowiden</td></tr><tr><td><a href="javascript:void(0)" rel="254552" class="his_term">ca</td></tr><tr><td><a href="javascript:void(0)" rel="254622" class="his_term">carekah</td></tr><tr><td><a href="javascript:void(0)" rel="254620" class="his_term">cara</td></tr><tr><td><a href="javascript:void(0)" rel="254623" class="his_term">carofacof</td></tr><tr><td><a href="javascript:void(0)" rel="257117" class="his_term">cariwciw</td></tr><tr><td><a href="javascript:void(0)" rel="254621" class="his_term">carcar</td></tr><tr><td><a href="javascript:void(0)" rel="256455" class="his_term">ma'akokay</td></tr><tr><td><a href="javascript:void(0)" rel="256456" class="his_term">paka'akok</td></tr></table></div>
        </div>
        
    </div>
</div>
<div id="oGHC_PopWin" class="pop_up"></div>
<div id="oGHC_TermsTree" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254511" title="1.感謝；感恩">ahowid</a>　<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="256440" title="1.值得去感謝者">aahowiden</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="256441" title="1.去感謝">ahowiden</a>　<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeDE" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254511">ahowid</a>　1.感謝；感恩<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="256440">aahowiden</a>　1.值得去感謝者<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="256441">ahowiden</a>　1.去感謝<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeSer" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254511">ahowid</a>　1.感謝；感恩<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="256440">aahowiden</a>　1.值得去感謝者<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="256441">ahowiden</a>　1.去感謝<ul></li></ul></li></ul></div>
'''