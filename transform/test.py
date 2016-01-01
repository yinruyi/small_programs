#coding:utf-8
import os
import sys
import string
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class pretreatment():
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
            dataset.append(line)
        return dataset

    def makeList(self, dataset):
    	for i in range(len(dataset)):
    		dataset[i] = dataset[i].split("\t")
    	return dataset

class Methods():
	def getWord(self, dataset):
		temp = []
		for j in range(len(dataset)):
			for i in range(16):
				temp.append(dataset[j][2*i])
		temp = list(set(temp))
		return temp

	def makeResult(self, dataset, words):
		result = []
		for i in range(16):
			temp = []
			candidate = {}
			for j in range(len(dataset)):
				candidate[dataset[j][2*i]] = dataset[j][2*i+1]
			#print candidate
			for kk in range(len(words)):
				if candidate.has_key(words[kk]):
					temp.append(str(candidate[words[kk]]))
				else:
					temp.append(str(0))
			#print temp,len(temp)
			result.append(temp)
		return result





class DataAnalysis(pretreatment, Methods):
    pass



if __name__=='__main__':
    data = DataAnalysis().read_txt(abspath+'//data.txt')
    data = data[1:]
    data = DataAnalysis().makeList(data)
    words = DataAnalysis().getWord(data)
    result = DataAnalysis().makeResult(data, words)

    print words,len(words)
    print result,len(result[0])
    string1 = ",".join(words)
    result = [",".join(tt) for tt in result]
    print result,len(result)
    string2 = "\n".join(result)
    f = open("result.txt","a+")
    line = f.write(string1+"\n")
    f.close()
    f = open("result.txt","a+")
    line = f.write(string2+"\n")
    f.close()
