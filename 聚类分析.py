import numpy as np
from sklearn.cluster import KMeans#加载Kmeans算法


def main():
    file_data, row, col = file_open('D:\\速度.txt')

    #聚类获得每个像素所属的类别
    label = KMeans(n_clusters=2).fit_predict(file_data)
    label = label.reshape([row, col])
    print(len(label))
    SpeedClu = [[],[]]
    for i in range(row):
        SpeedClu[label[i]].append(i)
    for i in range(len(SpeedClu)):
        print(SpeedClu[i])

    #
    #center = np.sum(km.cluster_centers_,axis =1)






def file_open(filesource):
#filesource = r'D:\\速度.txt'
    train_x = []
    #train_y = []
    slue = 0
    flag = 0
    #xm_l = 1
    file_object = open(filesource, 'r')
    lines = file_object.readlines()
    print(len(lines))
    file_object.close()
    for line in lines:
        linearr = line.strip().split()
            #print(linearr)
        if len(linearr) == 0:
            continue
        else:
            flag = len(linearr)-1
                #print(flag)
            for i in range(0, flag):
                slue = slue+float(linearr[i])
            mean_x = slue/(len(linearr)-1)
            train_x.append([mean_x])
            slue = 0
            #num.append(xm_l)
            #xm_l = xm_l+1

    train_x = np.mat(train_x)
    mp2, np3 = np.shape(train_x)
    return train_x, mp2, np3
main()