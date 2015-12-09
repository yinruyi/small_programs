from sklearn.cluster import KMeans
import numpy as np

def makedict(f):
    a = [line.split() for line in f]
    data_dict = {}
    for i in range(len(a)):
        data_dict[i] = a[i]
    return data_dict

def kmeans(data):
    data = np.array(data)
    computer=KMeans(n_clusters=2)
    computer.fit(data)
    labels = computer.labels_
    one_class = []
    zero_class = []
    for i in range(len(labels)):
        if labels[i] == 1:
            one_class.append(i)#0类的行号
        else:
            zero_class.append(i)#1类的行号
    centers = computer.cluster_centers_#找到中心
    cohesion_0,cohesion_1 = 0,0#初始化，自己和自己的cos是1
    for i in zero_class:
        cohesion_0 += judge_cos(data[i],centers[0])
    for i in one_class:
        cohesion_1 += judge_cos(data[i],centers[1])
    return zero_class,one_class,cohesion_0,cohesion_1

def judge_cos(x,y):
    af,bf,ab = 0,0,0
    for i in range(len(x)):
        af = float(x[i])*float(x[i])
        bf = float(y[i])*float(y[i])
        ab = float(x[i])*float(y[i])
    if af == 0 or bf == 0:
        print('error')
        return 0
    else:
        cos_value = ab/(np.sqrt(af)*np.sqrt(bf))
        return cos_value

def gettransdict(split_set,split_number):
    a = split_set[split_number][0]
    transdict = {}
    for i in range(len(a)):
        transdict[i] = a[i]
    return transdict

def getsplitset(split_set,split_number):
    new_split_set = []
    for i in range(len(split_set)):
        if i == split_number:
            pass
        else:
            new_split_set.append(split_set[i])
    return new_split_set

def getsplitnumber(split_set):
    split_number = 0
    temp = []
    for i in range(len(split_set)):
        temp.append(split_set[i][1])
    for i in range(len(temp)):
        if temp[split_number] < temp[i]:
            split_number = i
    return split_number

def main():
    f = open('train.txt','r',encoding='utf-8').readlines()
    data_dict = makedict(f)
    #print(data_dict)
    k = 45
    #sse = 0.001
    split_set = [[[i for i in range(90)],0]]
    split_number = 0#需要分类的簇标号
    while len(split_set) != k:
        transdict = gettransdict(split_set,split_number)#转换字典
        array2kmeans = [data_dict[i] for i in split_set[split_number][0]]#获取二分kmeans计算矩阵
        zero_class,one_class,cohesion_0,cohesion_1 = kmeans(array2kmeans)
        real_zero_class = [transdict[i] for i in zero_class]
        real_one_class = [transdict[i] for i in one_class]
        split_set = getsplitset(split_set,split_number)
        split_set.append([real_zero_class,cohesion_0])
        split_set.append([real_one_class,cohesion_1])
        split_number = getsplitnumber(split_set)
    for i in split_set:
        print(i)
    haha = []
    for i in split_set:
        haha.append(i[1])
    print(sum(haha)/k)


if __name__ == '__main__':
    main()