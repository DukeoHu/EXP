import numpy as np
#加速度读入
##########################
def sigmoid(z):
    s_value = 1.0/(1+np.exp(-z))
    return s_value
##改进型数据读取##
def data_read(filesource):#输入数据，输出矩阵归一化后的train_x和train_y
    data_array = np.loadtxt(filesource, delimiter = ',', dtype=float)
    train_x = data_array[:, :-2]
    print(np.shape(train_x))
    return train_x

def test(model, train_x):
    num_sample, num_feature = np.shape(train_x)
    count = []
    W1, b1, W2, b2= model['W1'], model['b1'], model['W2'], model['b2'] 
    #forward propagation to calculate our predictions
    #print(np.shape(W1))
    #print(np.shape(b2))
    #b1 = b1.reshape((1, 8))
    #b2 = b2.reshape((1, 8))
    z1 = train_x.dot(W1) + b1
    #print(np.shape(z1))
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2#
    a2 = sigmoid(z2) #2000*1
    a2 = np.floor(a2 * 2)
    #print(np.shape(a2))
    for i in range(len(a2)):
        if a2[i] == 0:
            count.append(i+1)
    return count

def main():
    print("step 1: loading data...\n")
    filesource = "D:\\100000.txt"
    train_x = data_read(filesource)
    W1 = np.loadtxt("/media/hi-fi/W1.txt", delimiter=',', dtype=float) #需要填入你训练好的theta值
    W2 = np.loadtxt("/media/hi-fi/W2.txt", delimiter=',', dtype=float) #需要填入你训练好的theta值
    b1 = np.loadtxt("/media/hi-fi/b1.txt", delimiter=',', dtype=float) #需要填入你训练好的theta值
    b2 = np.loadtxt("/media/hi-fi/b2.txt", delimiter=',', dtype=float) #需要填入你训练好的theta值
    model = {'W1':W1, 'b1':b1, 'W2':W2, 'b2':b2}

    print("step 2:starting.............\n")
    count = test(model, train_x)
    np.savetxt("D:\\92.2.txt", count, delimiter='\n', fmt='%d')
    print("step 3:file have saved!")

main()


