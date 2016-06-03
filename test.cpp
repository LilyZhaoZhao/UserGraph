#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cstring>
#include <ctime>

using namespace std;
map<string, string> filter;
map<string, set<string> > userLog;
map<string, set<string> > macUser;
map<string, set<int> > userTime;

typedef pair<string, set<string> > PAIR;

bool cmp_by_value(const PAIR& lhs, const PAIR& rhs){
    return lhs.second.size() > rhs.second.size();
}


//目标函数
void fact(string whichDay,string s2, string s3,string s4){
      userTime.clear();
      macUser.clear();
      userLog.clear();
      //  printf("this is fact function...");
      ifstream ifs2(whichDay.c_str()); // 0316/safe_wifi_connect_sample_export

      //string s2 = "nodes";
      //string s3 = "edges";
      ofstream ofs1(s2.c_str());//nodes
      ofstream ofs2(s3.c_str());//edges

      //ifstream ifs1("poiloc");
      ifstream ifs1(s4.c_str());//poiloc
      string mac, no="a";
      string token,line;
      int count = 0;
      while(getline(ifs1, line)){
  		    istringstream iss(line);
  		    count=0;
  		    while(getline(iss, token, ' ')){
  			      count ++;
              switch(count){
              case 1:
                  mac = token;
                  break;
              case 2:
                  no = token;
                  break;
              }
          }
          filter[mac] = no;
      }
      ifs1.close();

      string guid, bssid, connect_time;
      time_t t;
      while(getline(ifs2, line)){
  		    istringstream iss(line);
  		    count=0;
  		    while(getline(iss, token, '|')){
  			      count ++;
              switch(count){
              //case 1:
              //    gotime = token;
              //    break;
              case 2:
                  guid = token;
                  break;
              case 4:
                  bssid = token;
                  break;
              case 6:
                  connect_time = token.substr(0,10);
                  t  = atoi(connect_time.c_str());
              //    struct tm* tm = localtime(&t);
              //    char date[50];
              //    strftime(date, sizeof(date), "%Y-%m-%d %T", tm);
              //    connect_time = string(date);
                  break;
              }
  		    }
          if(filter.find(bssid)!=filter.end() && macUser[bssid].find(guid) == macUser[bssid].end()&&
              userTime[guid].find(t/900) == userTime[guid].end()){
              //userLog[guid].insert(gotime+','+bssid+','+connect_time+','+filter[bssid]);
              userLog[guid].insert(filter[bssid]);
              //userMac[guid].insert(bssid);
              userTime[guid].insert(t/900);
              macUser[bssid].insert(guid);
          }
  	  }

      float macNum = 0.0;
      for(map<string,set<string> >::const_iterator it=userLog.begin(); it!=userLog.end(); ++it){
        macNum += it->second.size();
      }
      macNum = macNum/userLog.size();
    //  ofs<<','<<macNum;   //一天内每个用户访问的mac数量的平均值
     // ofs<<','<<userLog.size(); // 一天内的用户数


      vector<PAIR > cPair(macUser.begin(),macUser.end());
      sort(cPair.begin(), cPair.end(), cmp_by_value);

      for(int i = 0; i<cPair.size();++i){
        if(cPair[i].second.size() >= 2){
          //for(set<string>::const_iterator it=cPair[i].second.begin();it!=cPair[i].second.end(); ++it){
            vector<string> v(cPair[i].second.begin(),cPair[i].second.end());
            for(int j=0; j<v.size()-1;j++){
              for(int h=j+1;h<v.size();h++){
                  ofs2<<v[j]<<','<<v[h]<<endl;
              }
            }
          }
        else{
          for(set<string>::const_iterator it=cPair[i].second.begin();it!=cPair[i].second.end(); ++it){
            ofs1<<*it<<endl;
          }
        }
      }

      ifs2.close();
      ofs1.close();
      ofs2.close();

}

int main(int argc, char* argv[]){
   // string s1 = "des3/201503";
   // string s2 = "/safe_wifi_connect_sample_export";
    string s,s2,s3,s4;
   // for(int i=16;i<=22;i++)
   // {
        s = argv[1];
        s2 = argv[2];
        s3 = argv[3];
        s4 = argv[4];
        //fact("des3/20150316/safe_wifi_connect_sample_export");
        fact(s,s2,s3,s4);
   // }

}
