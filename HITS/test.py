def readtxt(road):
    data1 = open(road,'r',encoding= 'utf-8').readlines()
    new_data = []
    for i in data1:
        if i[-1] == '\n':#去掉回车符号
            i = i[0:-1]
        new_data.append(i)
    return new_data



if __name__=='__main__':
    data = open('纽约抽取tttttt.txt','r',encoding= 'utf-8').readlines()
    scence = readtxt('景点.txt')
    print(data[0])
    print(scence)
    for i in range(len(data)):
        temp = data[i].split()
        for j in range(len(temp)):
            h = temp[j].split('/')
            if len(h) == 2:
                if h[0] in scence:
                    temp[j] = h[0]
                else:
                    temp[j] = ' '
            else:
                temp[j] = ' '
        data[i] = ' '.join(temp)
    print(data[0])
    
    
    write_file=open('out.txt','w',encoding= 'utf-8')
    for i in range(len(data)):
        write_file.writelines(data[i])
        write_file.writelines('\n')
    write_file.close()
    
    
    
    