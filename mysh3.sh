#!/bin/bash
#a=深圳宝安国际机场B楼
#a=$1
#awk -F"|" -v arr=${a} '{if($(NF-2)==arr)print $2}' safe_wifi_poi_sample > poiloc
a=$1
b=$2
c=$3
d=$4
./test ${a} ${b} ${c} ${d}
#./test $1 $2 $3 $4
