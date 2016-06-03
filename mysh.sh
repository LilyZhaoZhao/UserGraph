#!/bin/bash
#kaige 2013-07-02
#a=深圳宝安国际机场B楼
a=$1
b=$2
#for(i=0;i<${#a[@]})i in 1 .. $((${#a[@]}-1))
#do
#awk -F"[\t]" 'BEGIN{sum=0}{if($15=="'${a}'"){sum=sum+1}}END{print "'${a}'",sum}' require.t
awk -F"|" -v arr=${a} '{if($(NF-2)==arr)print $2}' ../data/safe_wifi_poi_sample > ${b}

#done

