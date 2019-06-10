import os
import pickle
import numpy as np
import operate_data as od
import ml_model as ml

VECTOR_MODE = {'onehot': 0, 'wordfreq': 1, 'twovec': 2, 'tfidf': 3, 'outofdict': 4}

def save_model(best_vector,best_model):
    """
    存储效果最好的模型
    需要手动指明参数名字
    :param best_vector: 最好的文本->词向量的方法
    :param best_model: 最好的机器学习模型
    :return: info
    """
    od.loadStopwords()
    od.loadEmotionwords()
    od.loadWords(od.stopList)
    od.loadDocument(od.stopList)
    xpath = os.path.join('result', 'vector', 'resultX.npz')
    ypath = os.path.join('result', 'vector', 'resultY.npz')
    resultX = np.load(xpath)
    resultY = np.load(ypath)
    new_x, new_y = od.twoTag(resultX[best_vector], resultY[best_vector])
    model_saved = ml.linearLogistic(new_x, new_y)
    path = os.path.join('model','wordfreq_logistic.ml')
    with open(path,'wb') as f:
        pickle.dump(model_saved,f)
    print("Save over")

class Predictor(object):
    """
    更多的使用说明请去看README.md
    """
    def __init__(self):
        self._model = None
        self.news = None
        self.__tag = None
        self._vec = None
        self.mode = None

    def load_model(self,path=None):
        if not path:
            path = os.path.join('model','wordfreq_logistic.ml')

        with open(path,'rb') as f:
            self._model = pickle.load(f)

    def set_mode(self,mode):
        if isinstance(mode,int):
            assert mode in VECTOR_MODE.values(), "没有这种vector方式"
        if isinstance(mode,str):
            assert mode in VECTOR_MODE.keys(), "没有这种vector方式"
            mode = VECTOR_MODE[mode]
        self.mode = mode

    def set_news(self,news):
        if not len(news):
            print("请输入有效的新闻文本,谢谢")
            return
        self.news = news

    def trans_vec(self):
        vec_list = od.words2Vec(self.news,od.emotionList,od.stopList,od.posList,od.negList,mode=self.mode)
        self._vec = np.array(vec_list).reshape(1,-1)

    # 调用的时候计算函数
    def __call__(self, *args, **kwargs):
        self.__tag = self._model.predict(self._vec)
        return self.__tag

    def get_tag(self):
        return self.__tag


def test(reload=False):
    if reload:
        best_vector = "wordfreq"
        best_model = 1  # linearLogistic
        save_model(best_vector, best_model)
    else:
        od.loadStopwords()
        od.loadEmotionwords()
        od.loadWords(od.stopList)
        od.loadDocument(od.stopList)

    predictor = Predictor()
    predictor.load_model()
    predictor.set_mode(mode="wordfreq")

#    news = "                                                  周二,恒生指数收报20356.24点,跌236.76点,跌幅1.15%;国企指数收报10596.91点,跌148点,跌幅1.38%;大市成交492.76亿港元。美国3月非农就业数据表现疲弱,拖累隔夜欧美股市全线受压。中国3月份CPI同比增长3.6%,令货币政策在短期内放宽预期降低。港股早盘随外围低开两百多点,但是A股在汇金增持内银股刺激下探底回升,对港股起到支持,之后恒指于低位维持窄幅震荡整理,最终跌逾1%。银行股全线走软。四大内银股方面,工商银行跌0.4%,中国银行跌0.64%,建设银行跌0.67%,农业银行跌1.2%;国际金融股方面,汇丰控股跌1.75%,渣打集团跌1.89%。美国就业市场增长放缓及内地通胀反弹,投资者对经济信心下降。中国央行短期内下调存准机会大减,从而利淡大市气氛。预计港股本周将继续在20200至20700点之间震荡。                                                                         "
    news="中國到目前為止都還沒有慢牛，本輪上漲行情得益於估值修復。深圳上善若水資產董事長侯安揚分析，今年以來影響A股市場的利空因素實際上在邊際改善。從整個宏觀經濟層面來說，國家對於股市支持力度會進一步加大，特別是去年四季度以來，為了緩解融資難、融資貴，相關部門採取了很多措施。今年以來，企業融資難、融資貴有相當程度緩解，資金逐漸鬆動對企業形成利好。「隨著房地產銷售與新開工增速的放緩，房地產投資對經濟可能產生較大的拖累。」這是侯安揚認為最大的風險因素。談及今年全年，他繼續看漲並堅定表達了對計算機板塊看好的信心。據侯安揚介紹，上善若水資產的投資思路是以企業家視角去做投資。更願意精選個股，相對集中持股。從公司層面出發，研究標的本身的商業模式，公司生意是什麼？戰略是什麼？如何執行？盈利模式是否能持續？另外，他堅稱自己不會參與概念炒作行情，像邊緣計算這種看不到實質產生行業性機會的就不會參與。"
    predictor.set_news(news=news)
    predictor.trans_vec()

    tag = predictor()
    print("result is",sum(predictor._vec[0]))
    print("tagging result",tag)

if __name__=='__main__':
    test()


