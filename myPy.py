#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
cmdArgv = sys.argv
import networkx as nx
import subprocess
import os
#import sys
#sys.path.append('./')
#import example

#从用户纪录中建立用户网络，一天内连接过同一个ap的用户之间建立一条边，
def graph(edges,nodes):
    G = nx.Graph()
    f1 = open(edges,'r')
    f2 = open(nodes,'r')
    for l in f1.readlines():
        l = l.strip('\n')
        l = l.split(',')
        G.add_edge(l[0],l[1])
    for l in f2.readlines():
        l = l.strip('\n')
        G.add_node(l)
    f1.close()
    f2.close()

    numNodes = G.number_of_nodes()
    numEdges = G.number_of_edges()
    if(int(numNodes)==0 or int(numEdges)== 0):
        return "0 nodes"
    else:
        #numEdges = str(G.number_of_edges())
        avgCC = str(nx.average_clustering(G))
        density = str(nx.density(G))
        #print numNodes
        #print numEdges
        #print avgCC
        #print density
        degree = 0
        for v in nx.degree(G).values():
            degree += int(v)
        #print degree/float(numNodes)
        avgDegree = str(degree/float(numNodes))
        #diam = []
        pathLength = []
        for g in nx.connected_component_subgraphs(G):
            if(g.number_of_nodes() > 1):
                pathLength.append(nx.average_shortest_path_length(g))
        #print max(pathLength)
        if(len(pathLength)!=0):
            maxPathLen = str(max(pathLength))
        else:
            maxPathLen = str(0)
        s = str(numNodes)+','+str(numEdges)+','+avgCC+','+density+','+avgDegree+','+maxPathLen
        return s

if __name__=="__main__":
    '''
    fr2 = open('safe_wifi_poi_sample’,'r')
    poiDict = {}
    for l in fr2.readlines():
        l = l.strip('\n')
        l = l.split('|')
        mac = l[1]
        #lon = l[2]
        #lat = l[3]
        loc = l[12]
        if(len(l) == 15):
            if !(loc in poiDict.keys()):
    '''

    fr = open(cmdArgv[1],'r')
    fw = open(cmdArgv[2],'w')

    s1 = "../data/201503";
    s2 = "/safe_wifi_connect_sample_export";
    file = cmdArgv[3] #poiloc
    s3 = cmdArgv[4] #nodes
    s4 = cmdArgv[5] #edges

    for l in fr.readlines():
        l = l.strip('\n')
        l = l.split()
        location = l[0]
        fw.write(l[1]+'\n')
        #print location
        #ret=subprocess.call('awk -F"|" -v arr=${location} '{if($(NF-2)==arr)print $2}' safe_wifi_poi_sample > poiloc',shell=True)
        os.environ['location']=str(location)
        os.environ['file']=str(file)
        os.system("sh mysh.sh $location $file")

        for i in range(16,23):
            s = s1+str(i)+s2
           # example.fact(s)
           # print s
            os.environ['s']=str(s)
            os.environ['s3']=str(s3)
            os.environ['s4']=str(s4)
            os.system("sh mysh3.sh $s $s3 $s4 $file")
            result = graph(s4,s3)
            fw.write(result+'\n')

    fw.close()
    fr.close()
