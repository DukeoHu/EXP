###文件MD5对比
##2020/06/03
##dukeohu
####输入两个目录，然后对比两个目录中的文件
##可以用于查找webshell，如果文件被加入webshell，那么其MD5值一定会发生变化


import hashlib
import os

#获取目录下所有文件,以列表形式返回
def path(path):
    try:
        file_list = os.listdir(path)
        res = []
        j = ""
        for i in file_list:
            j = path + str('/') + i
            res.append(j)
        return res
    except:
        print("错误，你输入的目录存在问题!")

#对每一个文件计算MD5值
def md5sum(file):
    m=hashlib.md5()  ##造出hash工厂
    file = str(file)
    #print(file)
    with open(file,'rb') as f:
        for line in f:
            m.update(line)
    f.close()
    return (m.hexdigest())
    ##运送文件中全部字符串至hash工厂

def compare():
    ##
    pass

def app_run():
    dict_1 = {}
    dict_2 = {}
    compare_path_1 = input("目录1路径：")
    compare_path_2 = input("目录2路径：")
    res_1 = path(compare_path_1)
    #print(res_1)
    res_2 = path(compare_path_2)
    #print(res_2)
    res_1_md5 = []
    res_2_md5 = []

    ###获取每个文件的MD5值
    for i in res_1:
        res_1_md5.append(md5sum(i))
    for j in res_2:
        res_2_md5.append(md5sum(j))

    #print(res_1_md5)
    #print(res_2_md5)

    #print(len(res_1))
    for i in range(len(res_1)):
        dict_1[res_1[i]] = res_1_md5[i]
    print(dict_1)

    for i in range(len(res_2)):
        dict_2[res_2[i]] = res_2_md5[i]
    print(dict_2)
    #print(len(res_2))

    ####进行对比，发现差别所在。
    #print('mu'lu len(dict_1))

if __name__ == "__main__":

    app_run()
    #res1 = ['1','2','3','4']
    #for i in range(len(res1)):
        #print(i)