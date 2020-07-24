
###通过ES中索引大小统计ES数据量
##time：2020/07/07
##author: dukeohu

import requests
res = []
kb = []
mb = []
gb = []
b = []
def query(es_url):
    m = ''
    o = []
    s = requests.get(es_url,timeout=600)
    #print(s.text)
    s1 = s.text.split("\n")
    for i in s1[1:-1]:
        ##如果本行含有close，说明该索引已被关闭，不在统计范围内
        if "close" in i:
            continue

        m = i.split(" ")
        #print(m)
        for j in m:
            if j == "":
                continue
            else:
                o.append(j)
                ###['green', 'open', '.monitoring-kibana-7-2020.07.03', 'Qamoma9VRQ6l_zgqOqyzNg', '1', '1', '728', '0', '502.5kb', '244.2kb']
        #print(o)
        res.append(o[-2])
        print(o)
        o = []

##计算大小
def num_count():
    bytes = 0
    kb = 0
    mb = 0
    gb = 0
    for line in res:
        if 'gb' in line:
            gb += float(line.replace("gb",""))
        elif 'mb' in line:
            mb += float(line.replace("mb",""))
        elif 'kb' in line:
            kb += float(line.replace("kb", ""))
        elif 'b' in line:
            bytes += float(line.replace("b", ""))
        else:
            continue
    #print("Bytes KB MB GB")
    print("索引大小为：%f Bytes %f KB %f MB %f GB 的总和" %(bytes, kb, mb, gb))
    #print(kb/1024/1024+mb/1024+gb)

if __name__ == "__main__":
    url = 'http://xx.xx.xx.xx:9200/_cat/indices?v'
    query(es_url=url)
    print(res)
    num_count()
