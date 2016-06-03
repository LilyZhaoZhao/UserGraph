#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
cmdArgv = sys.argv

#将finalData转换成可以输入MIC的数据格式MIC.csv：其中对应的catalog用数字代替
if __name__=="__main__":

    with open(cmdArgv[1],'r') as f: # finalData
        datas = f.readlines()
    fw = open(cmdArgv[2],'w')#MIC_finalData.csv
    fw.write("catalog,nodesNum,edgesNum,avgCC,density,avgDegree,maxPathLen\n")

    #catalogDict = {"房产小区":1,"购物":2,"医疗保健":3,"教育学校":4,"酒店宾馆":5,"公司企业":6,"旅游景点":7,"娱乐休闲":8}
    catalogDict = {"房产小区":1,"购物":2,"医疗保健":3,"教育学校":4,"酒店宾馆":5,"公司企业":6,"旅游景点":7,"娱乐休闲":8,"汽车":9,"基础设施":10,"文化场馆":11,"机构团体":12,"生活服务":13,"美食":14,"运动健身":15,"银行金融":16}
    for data in datas:
        data = data.strip('\n')
        #data = data.split(',')
        if(len(data)==12 or len(data)==6):
            #print data
            #data=str(data,'utf-8')
            catalog = catalogDict[data]
        else:
            if(data != "0 nodes"):
                fw.write(str(catalog)+','+data+'\n')
            #fw.write(str(catalog)+",0,0,0,0,0,0\n")


    fw.close()
    f.close()
