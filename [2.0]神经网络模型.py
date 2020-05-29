##############################
#########BP神经网络############
###########第二版单隐含层版##############
#coding:utf-8
#time:2017.6.3
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

def sigmoid(z):
    s_value = 1.0/(1+np.exp(-z))
    return s_value

def sigmoid_deri(x):#s型函数导数
    return sigmoid(x)*(1 - sigmoid(x))
#参数设置
class Config:
    nn_input_dim = 49 # 输入层维度
    nn_output_dim = 1 #输出层维度

    #gradient descent parameter
    epsilon = 0.000005#learning rate
    reg_lambda = 0.000005#regularization strength


#loading data
def data_read(filesource):#输入数据，输出矩阵归一化后的train_x和train_y
    data_array = np.loadtxt(filesource, delimiter = ',', dtype=float)
    train_y = data_array[:, -1]
    train_x = data_array[:, :-2]
    X = train_x
    y = train_y
    #返回矩阵
    #print(type(y))
    return X, y

#calculate the total loss on the dataset
def calculate(model, X, y):#################################暂时用不上
    num_example, num_feature = np.shape(X)# training set size
    error = 0
    W1, b1, W2, b2= model['W1'], model['b1'], model['W2'], model['b2']

    #forward propagation to calculate our predictions
    z1 = X.dot(W1) + b1
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2#2000*8 8*1 = 2000*1
    a2 = sigmoid(z2) #2000*1

    error = (np.sum(y) - np.sum(a2)) / num_example
    return error


# build the NeuralNetwork Model
def NeuralNetwork(X, y, nn_hdim, num_passes=40000, print_loss=False):
    #initialize the parameters to random values. 
    num_example, num_feature = np.shape(X)
    np.random.seed(0)#random seed set
    W1 = np.random.randn(Config.nn_input_dim, nn_hdim) / np.sqrt(Config.nn_input_dim)#weights of layers1 set 49*8
    b1 = np.zeros((1, nn_hdim))#偏置单元设置 1*8
    W2 = np.random.randn(nn_hdim, Config.nn_output_dim) / np.sqrt(nn_hdim) #weights of layer2 set 8*1
    b2 = np.zeros((1, Config.nn_output_dim))#隐层偏置单元设置 1*1

    #This is what we will return at the end  initalize the model
    model = {} #dictionary type
    y = y.reshape((num_example, 1))
    #Gradient descent .For each batch 每一批次的更新
    for i in range(num_passes):
        
        #forward propagation
        #print(np.shape(X))
        z1 = X.dot(W1) + b1
        #print(np.shape(z1))
        a1 = sigmoid(z1)
        z2 = a1.dot(W2) + b2#2000*8 8*1 = 2000*1
        a2 = sigmoid(z2) #2000*1
        #print(np.shape(a1))
        #print(np.sum(a2))
        #print(np.sum(y))
        #print(np.shape(y))
        
        

        #back propagation
        delta3 = a2 - y
        #print(np.shape(delta3))
        #delta3[range(num_example), y] -= 1#用处暂不明白
        dW2 = (a1.T).dot(delta3) #8*1
        #print(np.shape(dW2))
        db2 = np.sum(delta3, axis=0, keepdims=True)
        #print(np.shape(db2))
        
        delta2 = delta3.dot(W2.T) * sigmoid_deri(a2) #后半部分为tanh函数的导数
        #print(np.shape(delta2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)


        #Add regularization terms 针对权重
        dW2 += Config.reg_lambda * W2
        dW1 += Config.reg_lambda * W1

        #gradient descent parameter update
        W1 += -Config.reg_lambda * dW1
        b1 += -Config.reg_lambda * db1
        W2 += -Config.reg_lambda * dW2
        b2 += -Config.reg_lambda * db2
        #print(np.shape(b2))

        #Assign new parameters to the model
        model = {'W1':W1, 'b1':b1, 'W2':W2, 'b2':b2}#每次都会更新model
        #print(W2)

        #costfunction loss value
        if print_loss and i % 10000 == 0:
            print("Loss after iteration %i: %f" %(i, calculate(model, X, y)))#每一千次打印一次当前的误差值

    return model

def prediction(model, test_x, test_y):
    num_sample, num_feature = np.shape(test_x)
    count = 0
    W1, b1, W2, b2= model['W1'], model['b1'], model['W2'], model['b2'] 
    #forward propagation to calculate our predictions
    z1 = test_x.dot(W1) + b1
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2#2000*8 8*1 = 2000*1
    a2 = sigmoid(z2) #2000*1
    a2 = np.floor(a2 * 2)
    for i in range(len(a2)):
        if a2[i] == test_y[i]:
            count += 1
    accuracy = count/len(a2)
    return accuracy

def main():
    print("step 1:loading datafiles.....\n")
    filesource = "/media/hi-fi/1.txt"
    X, y = data_read(filesource)

    print("step 2:model training......\n")
    model = NeuralNetwork(X, y, 8, print_loss=True)
    #print(model)
    #np.savetxt("D:\\theta1.txt", model['W1'], fmt='%.18e', delimiter=',')
    #np.savetxt("D:\\theta2.txt", model['W2'], fmt='%.18e', delimiter=',')
    #print("theta值文件保存成功!\n")
    print("step 3:model prediction..........")
    filesource2 = "/media/hi-fi/2.txt"
    test_x, test_y = data_read(filesource2)
    accuracy = prediction(model, test_x, test_y)
    np.savetxt("/media/hi-fi/W1.txt", model['W1'], fmt='%.18e', delimiter=',')
    np.savetxt("/media/hi-fi/b1.txt", model['b1'], fmt='%.18e', delimiter=',')
    np.savetxt("/media/hi-fi/W2.txt", model['W2'], fmt='%.18e', delimiter=',')
    np.savetxt("/media/hi-fi/b2.txt", model['b2'], fmt='%.18e', delimiter=',')
    print("The classify accurancy is:%.3f%%" % (accuracy*100))


if __name__ == "__main__":
    main()





