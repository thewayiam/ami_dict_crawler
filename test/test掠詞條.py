from unittest.case import TestCase

from crawler import Spider
from scrapy.selector import Selector
import scrapy


class 掠網頁試驗(TestCase):

    def setUp(self):
        self.要求 = scrapy.http.Request(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            meta={'詞條名': '詞條名'},
        )

    def test_正常詞條(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.正常回應.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        結果 = Spider().掠詞條(rr)
        self.assertIn('examples', 結果)
        self.assertEqual(結果['name'], "a:su'")
        self.assertEqual(結果['source'], "asu'")
        self.assertEqual(
            結果['pronounce'], "http://e-dictionary.apc.gov.tw/MultiMedia/Audio/ais/a：su'_{1}.mp3")
        self.assertEqual(結果['frequency'], '詞頻：★(1)')

    def test_有例句詞條(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.例句回應.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        結果 = Spider().掠詞條(rr)
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
        self.assertEqual(結果['examples'], 答案['examples'])
        self.assertEqual(結果, 答案)

    def test_兩句例句(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.無source有兩句.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        結果 = Spider().掠詞條(rr)
        答案 = [
            {
                "pronounce": None,
                "sentence": "O 'opo no panay kora ma'araway no mita i potal na Mayaw.",
                "zh_Hant": "在Mayaw家的庭院我們看到的是堆積如山的稻穀。",
                "description": "解釋1：堆集晒過的穀子"
            },
            {
                "pronounce": None,
                "sentence": "'Opo han no mita ko iraay a sito.",
                "zh_Hant": "我們把學生集合起來。",
                "description": "解釋2：集中；集合"
            },
            {
                "pronounce": None, "sentence": None, "zh_Hant": None, "description": "解釋3：會議"
            }
        ]
        self.assertEqual(結果['examples'], 答案)

    def test_無source(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.無source有兩句.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        結果 = Spider().掠詞條(rr)
        self.assertEqual(結果['source'], None)

    def test_無發音回應(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.無發音回應.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        結果 = Spider().掠詞條(rr)
        self.assertEqual(結果['pronounce'], None)

    def test_系統維護中(self):
        rr = scrapy.http.TextResponse(
            'http://e-dictionary.apc.gov.tw/ais/Term.htm',
            body=self.系統維護中回應.encode(),
            encoding='utf-8',
            request=self.要求,
        )
        self.assertIsNone(Spider().掠詞條(rr))

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
    無source有兩句 = '''

<div id="oGHC_Deatail">
    <div id="oGHC_FB"></div>
    <div id="oGHC_Term_Area" class="words">
        
        <div id="oGHC_Term" class="term"><span>'opo</span></div>
        
        <div id="oGHC_Freq" class="freq">詞頻：<span class="term_freq">★</span>(2)</div>
        <div id="oGHC_Source" class="source">詞根　/　<a href="javascript:void(0)" class="troot" rel="'opo">詞根結構▼</a></div>
    </div>
    <hr class="spline" />
    <div class="e_con">
        
        <div class="concon">
            
            <div class="block"><div><strong>解釋1</strong>：堆集晒過的穀子</div><div class="word_detail"><table class="tb06"><tr class="st"><td>O <a href="javascript:void(0)" title="1.堆集晒過的穀子,2.集中；集合,3.會議" rel="254485" class="dsl_term">'opo</a> <a href="javascript:void(0)" title="1.格位標記（屬格）" rel="255742" class="dsl_term">no</a> <a href="javascript:void(0)" title="1.稻子；穀子" rel="255837" class="dsl_term">panay</a> <a href="javascript:void(0)" title="1.那個（主格）" rel="255473" class="dsl_term">kora</a> ma'araway <a href="javascript:void(0)" title="1.格位標記（屬格）" rel="255742" class="dsl_term">no</a> <a href="javascript:void(0)" title="1.我們（包含式；屬格）" rel="258675" class="dsl_term">mita</a> <a href="javascript:void(0)" title="1.介系詞" rel="255205" class="dsl_term">i</a> <a href="javascript:void(0)" title="1.外面；庭院；曬穀場；廣場" rel="255902" class="dsl_term">potal</a> na Mayaw. </td></tr><tr><td>在Mayaw家的庭院我們看到的是堆積如山的稻穀。</td></tr></table></div></div><div class="block"><div><strong>解釋2</strong>：集中；集合</div><div class="word_detail"><table class="tb06"><tr class="st"><td><a href="javascript:void(0)" title="1.堆集晒過的穀子,2.集中；集合,3.會議" rel="254485" class="dsl_term">'Opo</a> han <a href="javascript:void(0)" title="1.格位標記（屬格）" rel="255742" class="dsl_term">no</a> <a href="javascript:void(0)" title="1.我們（包含式；屬格）" rel="258675" class="dsl_term">mita</a> <a href="javascript:void(0)" title="1.格位標記（主格）" rel="255421" class="dsl_term">ko</a> iraay a sito. </td></tr><tr><td>我們把學生集合起來。</td></tr></table></div></div><div class="block"><div><strong>解釋3</strong>：會議</div></div>
            
            
            
            
            
            
            
            
            
            <div id="oGHC_Opinion" class="op254485"></div>
        </div>
        
        <div class="history">
            
            <div id="oGHC_Image" class="pic"></div>
            <div id="oGHC_History" class="hislist"><table class="tbhis"><th>瀏覽歷程</th><tr><td><a href="javascript:void(0)" rel="259489" class="his_term">'opiren</td></tr><tr><td><a href="javascript:void(0)" rel="254485" class="his_term">'opo</td></tr><tr><td><a href="javascript:void(0)" rel="254271" class="his_term">'a'am</td></tr><tr><td><a href="javascript:void(0)" rel="255776" class="his_term">ocong</td></tr><tr><td><a href="javascript:void(0)" rel="256440" class="his_term">aahowiden</td></tr><tr><td><a href="javascript:void(0)" rel="254511" class="his_term">ahowid</td></tr><tr><td><a href="javascript:void(0)" rel="254552" class="his_term">ca</td></tr><tr><td><a href="javascript:void(0)" rel="254622" class="his_term">carekah</td></tr><tr><td><a href="javascript:void(0)" rel="254620" class="his_term">cara</td></tr><tr><td><a href="javascript:void(0)" rel="254623" class="his_term">carofacof</td></tr></table></div>
        </div>
        
    </div>
</div>
<div id="oGHC_PopWin" class="pop_up"></div>
<div id="oGHC_TermsTree" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254485" title="1.堆集晒過的穀子,2.集中；集合,3.會議">'opo</a>　<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="259491" title="1.聚集的">masa'opoay</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259492" title="1.集合的">misa'opoay</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259493" title="1.集合起來">pasa'opoen</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259494" title="1.去聚集">pisa'opo</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259495" title="1.會議,2.聚集；集合">sa'opo</a>　<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeDE" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254485">'opo</a>　1.堆集晒過的穀子,2.集中；集合,3.會議<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="259491">masa'opoay</a>　1.聚集的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259492">misa'opoay</a>　1.集合的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259493">pasa'opoen</a>　1.集合起來<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259494">pisa'opo</a>　1.去聚集<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259495">sa'opo</a>　1.會議,2.聚集；集合<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeSer" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254485">'opo</a>　1.堆集晒過的穀子,2.集中；集合,3.會議<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="259491">masa'opoay</a>　1.聚集的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259492">misa'opoay</a>　1.集合的<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259493">pasa'opoen</a>　1.集合起來<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259494">pisa'opo</a>　1.去聚集<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="259495">sa'opo</a>　1.會議,2.聚集；集合<ul></li></ul></li></ul></div>
'''
    無發音回應 = '''
    

<div id="oGHC_Deatail">
    <div id="oGHC_FB"></div>
    <div id="oGHC_Term_Area" class="words">
        
        <div id="oGHC_Term" class="term"><span>dopohen</span></div>
        
        <div id="oGHC_Freq" class="freq">詞頻：<span class="term_freq">★</span>(0)</div>
        <div id="oGHC_Source" class="source">來源：<a href="javascript:void(0)" class="ws_term" rel="254870">dopoh</a>　/　<a href="javascript:void(0)" class="troot" rel="dopohen">詞根結構▼</a></div>
    </div>
    <hr class="spline" />
    <div class="e_con">
        
        <div class="concon">
            
            <div class="block"><div><strong>解釋1</strong>：孜孜不倦；勤奮</div><div class="word_detail"><table class="tb06"><tr class="st"><td>”Dopohen a <a href="javascript:void(0)" title="1.工作；上班" rel="260336" class="dsl_term">matayal</a>! ” saan <a href="javascript:void(0)" title="1.格位標記（主格）" rel="255421" class="dsl_term">ko</a> tawki. </td></tr><tr><td>老闆說：「工作要勤奮！」</td></tr></table></div></div>
            
            
            
            
            
            
            
            
            
            <div id="oGHC_Opinion" class="op257456"></div>
        </div>
        
        <div class="history">
            
            <div id="oGHC_Image" class="pic"></div>
            <div id="oGHC_History" class="hislist"><table class="tbhis"><th>瀏覽歷程</th><tr><td><a href="javascript:void(0)" rel="254787" class="his_term">da'at</td></tr><tr><td><a href="javascript:void(0)" rel="256440" class="his_term">aahowiden</td></tr><tr><td><a href="javascript:void(0)" rel="254271" class="his_term">'a'am</td></tr><tr><td><a href="javascript:void(0)" rel="254485" class="his_term">'opo</td></tr><tr><td><a href="javascript:void(0)" rel="259489" class="his_term">'opiren</td></tr><tr><td><a href="javascript:void(0)" rel="255776" class="his_term">ocong</td></tr><tr><td><a href="javascript:void(0)" rel="254511" class="his_term">ahowid</td></tr><tr><td><a href="javascript:void(0)" rel="254552" class="his_term">ca</td></tr><tr><td><a href="javascript:void(0)" rel="254622" class="his_term">carekah</td></tr><tr><td><a href="javascript:void(0)" rel="254620" class="his_term">cara</td></tr></table></div>
        </div>
        
    </div>
</div>
<div id="oGHC_PopWin" class="pop_up"></div>
<div id="oGHC_TermsTree" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254870" title="1.殷勤工作；勤奮">dopoh</a>　<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="257456" title="1.孜孜不倦；勤奮">dopohen</a>　<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="257457" title="1.孜孜不倦；勤奮">madopoh</a>　<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeDE" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254870">dopoh</a>　1.殷勤工作；勤奮<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="257456">dopohen</a>　1.孜孜不倦；勤奮<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="257457">madopoh</a>　1.孜孜不倦；勤奮<ul></li></ul></li></ul></div>
<div id="oGHC_TermsTreeSer" class="terms_tree"><ul id="tree"><li><a href="javascript:void(0)" class="tree_term" rel="254870">dopoh</a>　1.殷勤工作；勤奮<ul><li>　<a href="javascript:void(0)" class="tree_term" rel="257456">dopohen</a>　1.孜孜不倦；勤奮<ul></li><li>　<a href="javascript:void(0)" class="tree_term" rel="257457">madopoh</a>　1.孜孜不倦；勤奮<ul></li></ul></li></ul></div>
'''
