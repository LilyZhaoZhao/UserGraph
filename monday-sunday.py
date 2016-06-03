#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
cmdArgv = sys.argv

def monday_sunday(daylist):

    if(len(daylist)>=6):
        monday = daylist[0]
        sunday = daylist[-1]
        monday = monday.split(',')
        sunday = sunday.split(',')
        nodes_edges = float(monday[0])/float(monday[1])
        monday.append(nodes_edges)#在最后添加一项：节点数/边数
        nodes_edges = float(sunday[0])/float(sunday[1])
        sunday.append(nodes_edges)
        monlength = len(monday)
        sunlength = len(sunday)
        if(monlength == sunlength):
            outputList = [[] for i in range(monlength)]
            for i in range(monlength):
                if(float(sunday[i])==0):   #如果周日的数据中有0值，那么就令比值为0
                    outputList[i] = 0
                else:
                    outputList[i] = float(monday[i])/float(sunday[i])
            return outputList
        else:
            return 0
    else:
        return 0




#处理finalData中的数据：用第一天的/最后一天的（即周一／周日，因为有的可能没有7天，所以是粗略统计）
if __name__=="__main__":

    with open(cmdArgv[1],'r') as f: # finalData
        datas = f.readlines()
    fw = open(cmdArgv[2],'w')#finalData_mon_sun.csv
    fw.write("catalog,nodesNum,edgesNum,avgCC,density,avgDegree,maxPathLen,nodesNum2edgesNum\n")

    daylist = []
    count = 0
    catalogDict = {"房产小区":1,"购物":2,"医疗保健":3,"教育学校":4,"酒店宾馆":5,"公司企业":6,"旅游景点":7,"娱乐休闲":8,"汽车":9,"基础设施":10,"文化场馆":11,"机构团体":12,"生活服务":13,"美食":14,"运动健身":15,"银行金融":16}
    for data in datas:
        data = data.strip('\n')
        #data = data.split(',')
        if(len(data)==12 or len(data)==6):

            if(count != 0):
                result = monday_sunday(daylist)
                if(result != 0):
                    fw.write(str(catalog))
                    for i in range(len(result)):
                        fw.write(','+str(result[i]))
                    fw.write('\n')
                catalog = catalogDict[data]
                daylist = []
            else:
                catalog = catalogDict[data]
                #lastCatalog = catalog
                #fw.write(str(catalog))
                count = 1
        else:
            if(data != "0 nodes"):
                daylist.append(data)

    result = monday_sunday(daylist)
    if(result != 0):
        fw.write(str(catalog))
        for i in range(len(result)):
            fw.write(','+str(result[i]))
        fw.write('\n')

    fw.close()
    f.close()
