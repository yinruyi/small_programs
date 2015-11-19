#coding:utf-8
import sys
import numpy
import codecs
import os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class pretreatment():
    """预处理"""
    def __init__(self):
        pass
    def read_txt(self,txtPath,coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        f[0] = f[0].replace(u"\ufeff",u"")
        dataset = []
        for line in f:
            line = line.replace(u"\r\n",u"")
            line = line.replace(u"\n",u"")
            dataset.append(line)
        return dataset

    def writefile(self, dataset):
        pass

    def test():
    	pass		


class Methods():
    def __init__(self):
        pass
    def makeMatrix(self, dataset, mark = u" "):
        for i in xrange(len(dataset)):
            dataset[i] = dataset[i].split(mark)
        return dataset
    def makeFloat(self, matrix):
    	return [float(i) for i in matrix]
    def getResult(self, dataset):
    	dataset = self.makeMatrix(dataset,"\t")
    	#print dataset[0][4:104]
    	print len(dataset[0])
    	for i in xrange(len(dataset)):
    		if len(dataset[i]) != 101:
    			print dataset[i]
    		dataset[i] = [dataset[i][0],self.makeFloat(dataset[i][1:])]
    	print len(dataset)
    	#dataset = [1,-22,3,4]
    	#print abs(dataset[1])
    	new_dataset = []
    	for i in xrange(len(dataset)-1):
    		for j in xrange(i+1,len(dataset)):
    			temp1 = "/".join([dataset[i][0],dataset[j][0]])
    			temp2 = [abs(dataset[i][1][k] - dataset[j][1][k]) for k in xrange(len(dataset[i][1]))]
    			new_dataset.append([temp1, temp2])
    	print len(new_dataset)
    	print new_dataset[0]

#   	def cosine(self, v2, v1):
#		n1 = numpy.linalg.norm(v1)
#		n2 = numpy.linalg.norm(v1)
#    	ip = numpy.dot(v1, v2)
#    	return ip / (n1 * n2)

	


class DataAnalysis(pretreatment, Methods):
    pass

def main():
	dataset = DataAnalysis().read_txt(abspath+'//dataset//dataset.txt')
	Methods().getResult(dataset)
	

if __name__=='__main__':
    main()
    