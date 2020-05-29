import numpy as np
#加速度读入
##########################
##改进型数据读取##
def data_read(filesource):#输入数据，输出矩阵归一化后的train_x和train_y
    data_array = np.loadtxt(filesource, delimiter = ',', dtype=float)
    #train_y = data_array[:, -1]
    train_x = data_array[:, :-2]
    #train_y = train_y.reshape(len(train_y), 1)
    #矩阵华
    train_x = np.mat(train_x)
    #train_y = np.mat(train_y)
    #矩阵大小
    m = np.shape(train_x)
    #n = np.shape(train_y)
    m_sample, m_feature = m
    #归一化处理
    #mean_x = train_x.sum(axis=1)/m_sample
    #var_x = train_x.max(axis=1) - train_x.min(axis=1)
    #train_x = (train_x-mean_x)/var_x

    #返回矩阵
    print(np.shape(train_x))
    return train_x, m_sample#train_x=66*50 train_y=66*1

def sigmoid(z):
    s_value = 1.0/(1+np.exp(-z))
    return s_value

def prediction(train_x, theta_1, theta_2, m_sample):
    print(train_x)
    num_sample = m_sample
    result_array = []
    for i in range(num_sample):#对每一个样本进行预测,大概100000个左右

        #前向传播
        Hid_one = train_x[i, :] #hid_one 100000*49
        #Hid_one = sigmoid(Hid_one)
        Hid_two = theta_1 * Hid_one.transpose()#隐层的输入值 8*49 49*1 = 8*1
        #print(np.shape(Hid_two)) #8*1
        Hid_two = sigmoid(Hid_two)#s函数处理 8*1
        #print(np.shape(Hid_two))
        Hid_three = theta_2 * Hid_two#隐层输出值 1*1
        #print(Hid_three)
        Hid_three = sigmoid(Hid_three)#s函数处理 1*1
        print(Hid_three)
        #print(Hid_three)
        if Hid_three < 0.5:
            result_array.append(i)
        else:
            continue
    return result_array

def main():
    print("step 1:loading data....\n")
    filesource1 = "D:\\100000.txt"
    filesource2 ="D:\\theta1.txt"
    filesource3 ="D:\\theta2.txt"
    train_x, m_sample = data_read(filesource1)
    theta_1 = np.loadtxt(filesource2, delimiter=',', dtype=float)
    theta_2 = np.loadtxt(filesource3, delimiter=',', dtype=float)
    theta_2 = np.mat(theta_2)

    print("step 2:classiffer working!.....\n")
    result_array = prediction(train_x, theta_1, theta_2, m_sample)
    print("共检测到机器轨迹个数为:%d,占十万组数据的:%.3f" % (len(result_array),len(result_array)/100000))
    np.savetxt("D:\\Neuralresult.txt", result_array, delimiter='\n', fmt='%d')
    print("Neural Network Prediction success!\n")

main()

