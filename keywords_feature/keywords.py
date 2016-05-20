#coding:utf-8
import os
import sys
import string
import codecs
import jieba
import jieba.posseg as pseg
import json
import sys
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import math
from gensim import corpora, models, similarities
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class preprocess(object):
    """预处理"""
    def __init__(self):
        pass
    def read_txt(self, txtPath, coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        f[0] = f[0].replace(u"\ufeff",u"")
        dataset = []
        for line in f:
            line = line.replace("\r\n","")
            line = line.replace("\n","")
            line = line.split('\t')
            dataset.append(line)
        return dataset

    def read_txt2(self, txtPath, coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        f[0] = f[0].replace(u"\ufeff",u"")
        dataset = []
        for line in f:
            line = line.replace("\r\n","")
            line = line.replace("\n","")
            dataset.append(line)
        return dataset

    def transtxt(self, txtPath, coding = 'utf-8'):
        dataset = self.read_txt(txtPath)

        bookContent = {}
        bookId = []
        for i in range(len(dataset)):
            if len(dataset[i]) != 2:
                print dataset[i]
            else:
                bookId.append(dataset[i][1])
                if dataset[i][1] not in bookContent:
                    bookContent[dataset[i][1]] = [dataset[i][0]]
                else:
                    temp = bookContent[dataset[i][1]]
                    temp.append(dataset[i][0])
                    bookContent[dataset[i][1]] = temp
        bookId = list(set(bookId))
        return bookId,bookContent

    def writeMatrix(self, dataset, Path, coding = "utf-8"):
        for i in xrange(len(dataset)):
            temp = dataset[i]
            temp = [str(temp[j]) for j in xrange(len(temp))]
            temp = ",".join(temp)
            dataset[i] = temp
        string = "\n".join(dataset)
        f = open(Path, "a+")
        line = f.write(string+"\n")
        f.close()

    def cutWords(self, dataset, stop_words_path="None"):
        #分词/去停用词
        result = []
        if stop_words_path == "None":
            for i in xrange(len(dataset)):
                temp = " ".join(jieba.cut(dataset[i]))
                result.append(temp)
            return result
        else:
            stop_words = self.read_txt2(stop_words_path)
            # print stop_words
            for i in xrange(len(dataset)):
                tup = []
                temp = " ".join(jieba.cut(dataset[i]))
                temp = temp.split()
                # print temp
                if len(temp) != 0:
                    for j in range(len(temp)):
                        # print j
                        # print stop_words
                        if temp[j] not in stop_words:
                            tup.append(temp[j])
                tup = " ".join(tup)
                result.append(tup)
                break
            return result

    def count(self, dataset):
        #计数
        count = {}
        for i in dataset:
            if i in count:
                count[i] += 1
            else:
                count[i] =1
        return count


class tfidf(preprocess):
    def __init__(self):
        pass
    def tfidf(self, dataset, num):
        stop_words_path = abspath+"//dataset//Stopword-Chinese.txt"
        corpus = self.cutWords(dataset,stop_words_path)
        vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
        transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
        #print vectorizer.fit_transform(corpus)
        try:
            tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
            #第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
        except:
            return []
        #print tfidf
        word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
        weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
        for i in xrange(len(weight[0])):
            word[i] = (word[i],sum(weight[:,i])) 
        # print word,len(word)
        word = sorted(word,key=lambda word_tuple:word_tuple[1],reverse=1)[0:num]
        word = [i[0]+' '+str(i[1]) for i in word]
        result = []
        for i in range(len(word)):
            temp = word[i].split()
            result.append(temp[0])
        return result

def tfidf_feature():
    bookId,bookContent = preprocess().transtxt(abspath+'//dataset//dataset.txt')
    # tfidf = tfidf().tfidf(bookContent[bookId[1]],10)
    # print tfidf
    result = []
    for i in range(len(bookId)):
        temp = [bookId[i]]
        temp.extend(tfidf().tfidf(bookContent[bookId[i]],10))
        result.append(temp)
    preprocess().writeMatrix(result,'tfidf.txt')    

if __name__=='__main__':
    tfidf_feature()




