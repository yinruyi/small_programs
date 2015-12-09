import numpy as np

def readtxt(road):
    data1 = open(road,'r',encoding= 'utf-8').readlines()
    new_data = []
    for i in data1:
        if i[-1] == '\n':#去掉回车符号
            i = i[0:-1]
        new_data.append(i)
    return new_data
if __name__=='__main__':
    data = open('纽约抽取.txt','r',encoding= 'utf-8').readlines()
    
    scence = readtxt('景点.txt')
    #print(len(data))
    #print(len(scence))
    arr = []
    for i in range(len(data)):
        seq = []
        for j in range(len(scence)):
            if scence[j] in data[i]:
                seq.append(1)
            else:
                seq.append(0)
        arr.append(seq)
    x = np.array(arr)#得到的数组
    J = []#景点
    U = []#游客
    j = np.ones((len(scence),1))
    J.append(j)
    u = np.ones((len(data),1))#初始化
    U.append(u)
    k = 1
    while k > 0.001:
        u = np.dot(x,j)/max(np.dot(x,j))
        j = np.dot(x.T,u)/max(np.dot(x.T,u))
        k = sum(U[-1]-u)+sum(J[-1]-j)
        J.append(j)
        U.append(u)
    print(j)
    
    
    





        
        
        
        
        
        
        
        
    
    
    