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

import jieba.analyse
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

def fix(words):
	drop = ['...','&#']
	result = []
	for i in range(len(words)):
		if words[i] not in drop:
			result.append(words[i])
	return result[0:20]



def tfidf_feature():
    bookId,bookContent = preprocess().transtxt(abspath+'//dataset//dataset.txt')
    # tfidf = tfidf().tfidf(bookContent[bookId[1]],10)
    # print tfidf
    result = []
    for i in range(len(bookId)):
    	temp = [bookId[i]]
        s = ','.join(bookContent[bookId[i]])
        words = jieba.analyse.extract_tags(s, topK=22, withWeight=False, allowPOS=())
        words = fix(words)
        temp.extend(words)
        result.append(temp)
        #break
    preprocess().writeMatrix(result,'tfidf2.txt')    

def textrank_feature():
    bookId,bookContent = preprocess().transtxt(abspath+'//dataset//dataset.txt')
    # tfidf = tfidf().tfidf(bookContent[bookId[1]],10)
    # print tfidf
    result = []
    for i in range(len(bookId)):
    	temp = [bookId[i]]
        s = ','.join(bookContent[bookId[i]])
        # print s
        for x, w in jieba.analyse.textrank(s, withWeight=True):
            # print('%s %s' % (x, w))
            temp.append(x)

        # print words
        # temp.extend(words)
        result.append(temp)
        # break
    preprocess().writeMatrix(result,'textrank.txt')    


if __name__=='__main__':
    tfidf_feature()
