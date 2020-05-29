import numpy as np
from numpy import matrix
import matplotlib.pyplot as plt
def main():
    filesource = r'D:\\速度.txt'
    train_x = []
    train_y = []
    slue = 0
    #flag = 0
    file_object = open(filesource, 'r')
    lines = file_object.readlines()
    print(len(lines))
    file_object.close()
    #train_x.append([1.0,2,3])
    #print(train_x)
    for line in lines:
        linearr = line.strip().split()
        #print(linearr)
        if len(linearr) == 0:
            continue
        else:
        #print((linearr[:-1])[-1])
        #print(type(linearr))
        #print(type(train_y))
            train_y.append(float(linearr[-1]))
            #print(train_y)
        #print(len(linearr))
            flag = len(linearr)-1
            #print(flag)
            for i in range(0, flag):
                slue = slue+float(linearr[i])
        #print(sum)
            mean_x = slue/(len(linearr)-1)
        #flag += 1
        #print(mean_x)
            square_x = mean_x*mean_x
            #print(square_x)
            train_x.append([1.0, mean_x, square_x])
        #print(train_x)
            slue = 0
        #print(len(train_y))
    #print(train_y)
    #print(train_y)
    print(len(train_x))
    train_y = np.mat(train_y)
    train_x = np.mat(train_x)
    v = np.shape(train_y)
    print(v)
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    print(min_x,max_x)
    #print(train_y)

    ##################################################
    #可视化处理

    numSamples, numFeatures = np.shape(train_x)
    print(np.shape(train_x),numSamples,numFeatures)
    train_y = np.transpose(train_y)
    train_y = matrix.getA(train_y)
    theta = np.ones((3,1))
    #图画1:显示所有样本
    for i in range(numSamples):
        if int(train_y[i, 0]) == 0:
            plt.plot(train_x[i, 1], train_x[i, 2], 'or')
        elif int(train_y[i, 0]) == 1:
            plt.plot(train_x[i, 1], train_x[i, 2], 'ob')
    #图画2:绘制分割线
    min_x = min(train_x[:, 1])[0, 0]
    max_x = max(train_x[:, 1])[0, 0]
    theta = matrix.getA(theta)#矩阵转为数组(python中的语法)
    y_min_x = float(-theta[0]-theta[1]*min_x)/theta[2]
    y_max_x = float(-theta[0]-theta[1]*max_x)/theta[2]   
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.xlabel('X1')
    plt.ylabel('X2')
    #plt.show()
main()