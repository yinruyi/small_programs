#coding:utf-8
import sys
import math
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class pretreatment():
	"""docstring for pretreatment"""
	def __init__(self, arg):
		super(pretreatment, self).__init__()
		self.arg = arg

	#def 
		


class Methods(tfidf, tf, df, pmi, idf, chi_square, lsi):
    pass

class DataAnalysis(pretreatment, Methods):
    pass



if __name__=='__main__':
    data = DataAnalysis().read_txt(abspath+'//data//ruanjian.txt')