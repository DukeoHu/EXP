##############################
#########BP神经网络############
###########第一版单隐含层版(无偏置单元)##############
#coding:utf-8
#time:2017.6.1

#依赖库导入
import numpy as np
import random
#次要函数定义
### 一 双曲函数以及导数 ###
def sigmoid(x):#s型函数
    s_value = 1.0/(1+np.exp(-x))
    return s_value
def sigmoid_deri(x):#s型函数导数
    return sigmoid(x)*(1 - sigmoid(x))
def tanh(x):
    return np.tanh(x)
def tanh_deriv(x):
    return 1.0 - np.tanh(x)*np.tanh(x)
#### 神经网络定义 ####
def NeuralNetwork(train_X, train_y, layers):#train_sample 为2400*50的矩阵
    #初始化，layes表示的是一个list，eg[49,8,8,1]表示第一层49个神经元，第二层8个神经元，第三层8个神经元,第四层1个
    #权重初始随机化
    #初始epsilon为0.1
    num_sample, num_feature = np.shape(train_X)
    #print(num_sample)
    theta_1 = 0.2 * np.random.random((layers[1], layers[0])) -0.1#从输入层到隐含层的theta矩阵(未包含一个偏执单元的theta值)8*49
    theta_2 = 0.2 * np.random.random((layers[2], layers[1])) -0.1#从隐含层到输出层的theta矩阵(未包含一个偏执单元的theta值)8*8
    theta_3 = 0.2 * np.random.random((layers[3], layers[2])) -0.1#从隐含层到隐含层的theta矩阵(未包含一个偏执单元的theta值)1*8


    #学习率初始化
    Hid_learnrate = 0.2#隐藏层学习率
    Out_learnrate = 0.2#输出层学习率
    lamuda = 0.5#正则化的值

    #sigma
    sigma_2 = 0
    sigma_1 = 0
    sigma_3 = 0

    #偏置单元
    bias1 = random.random(1)
    bias2 = random.random(1)

    #神经元训练开始
    for i in range(num_sample):#对每一个样本进行学习,大概2000个左右

        #前向传播
        Hid_one = train_X[i, :] #hid_one 2400*49
        Hid_two = theta_1 * Hid_one.transpose() + bias1#隐层的输入值 8*49 49*1 = 8*1  zhenque
        Hid_two = sigmoid(Hid_two)#s函数处理 8*1
        Hid_three = theta_2 * Hid_two + bias2#8*8 8*1  = 8*1
        Hid_three = sigmoid(Hid_three)#s函数处理 8*1
        Hid_four = theta_3 * Hid_three#1*8 8*1 = 1*1
        Hid_four = sigmoid(Hid_four)

        #反向传播 
        delta_four = Hid_four * (1 - Hid_four) * (train_y[i] - Hid_four) #输出层误差计算 deltawe
        #delta_two = (theta_2.transpose()*delta_three).dot(Hid_two.dot(1 - Hid_two))#计算delta2
        delta_three = np.multiply(theta_3.transpose()*delta_four, np.multiply(Hid_three, 1-Hid_three)) #8*1
        delta_two = np.multiply(theta_2.transpose()*delta_three, np.multiply(Hid_two, 1-Hid_two))
        #print(np.shape(delta_two))#delta_two为8*1矩阵


        sigma_3 += delta_four*(Hid_three.transpose()) #1*8
        sigma_2 = sigma_2 + delta_three*Hid_two.transpose()#第二层sigma计算 1*8
        #print(np.shape(sigma_2))
        sigma_1 = sigma_1 + delta_two*Hid_one#第一层sigma计算 
        #print(np.shape(sigma_1))

        D_value2 = 1/num_sample * (sigma_2 + lamuda*theta_2)#计算第二层误差值的偏导
        D_value1 = 1/num_sample * (sigma_1 + lamuda*theta_1)#计算第一层误差值的偏导

        theta_2 = theta_2 - Out_learnrate*D_value2#更新theta2的值,因为是反向更新所以先更新theta2的值
        theta_1 = theta_1 - Hid_learnrate*D_value1#更新theta1的值

        #梯度检查
        #for i in range(len(the))
    return theta_1,theta_2

#精度计算及统计函数
def prediction(test_X, test_y, theta_1, theta_2):
    num_sample, num_feature = np.shape(test_X)
    count = 0
    for i in range(num_sample):
        #前向传播
        Hid_one = test_X 
        Hid_two = theta_1 * Hid_one[i].transpose()#隐层的输入值
        Hid_two = sigmoid(Hid_two)#s函数处理

        Hid_three = theta_2 * Hid_two#隐层输出值
        Hid_three = sigmoid(Hid_three)#s函数处理

        #精度计算及统计
        p = np.floor(Hid_three*2)
        #print(p)
        if p == test_y[i, 0]:
            count += 1

    accuracy = count/num_sample
    return accuracy


##########################
##改进型数据读取##
def data_read(filesource):#输入数据，输出矩阵归一化后的train_x和train_y
    data_array = np.loadtxt(filesource, delimiter = ',', dtype=float)
    train_y = data_array[:, -1]
    train_x = data_array[:, :-2]
    train_y = train_y.reshape(len(train_y), 1)
    #矩阵华
    
    train_x = np.mat(train_x)
    train_y = np.mat(train_y)
    #矩阵大小
    #m = np.shape(train_x)
    #print(m)
    #n = np.shape(train_y)
    #m_sample, m_feature = m
    #归一化处理
    #mean_x = train_x.sum(axis=1)/m_sample
    #var_x = train_x.max(axis=1) - train_x.min(axis=1)
    #train_x = (train_x-mean_x)/var_x

    #返回矩阵
    return train_x, train_y#train_x=66*50 train_y=66*1


#主函数入口
def main():
    print("step 1:loading datafiles.....\n")
    filesource = "D:\\1.txt"
    train_X, train_y = data_read(filesource)#读取测试数据文件,返回矩阵train_X和train_y

    print("step 2:model training......\n")
    layers = [49, 8, 1]#三层神经网络,节点数未固定,但是层数已经固定,无法更改!!
    theta_1, theta_2 = NeuralNetwork(train_X, train_y, layers)
    np.savetxt("D:\\theta1.txt", theta_1, fmt='%.18e', delimiter=',')
    np.savetxt("D:\\theta2.txt", theta_2, fmt='%.18e', delimiter=',')
    print("theta值文件保存成功!\n")

    print("step 3:predict accuracy........\n")
    filesource2 = "D:\\2.txt"
    test_X, test_y = data_read(filesource2)#读取验证数据文件,返回矩阵test_X和test_y
    accuracy = prediction(test_X, test_y, theta_1, theta_2)#预测精度计算
    print("The classify accurancy is:%.3f%%" % (accuracy*100))

    print("step 4:chart visuality.............\n")



if __name__ == '__main__':
    main()







