import time
import getproxy
import json,requests,urllib.request
from traceback import print_exc
from ast import literal_eval
import pprint

def push_to_git():
    #Import dependencies
    from subprocess import call
    #Commit Message
    commit_message = "Updating json files"
    #Stage the file
    call('git add .', shell = True)
    # Add your commit
    call('git commit -m "'+ commit_message +'"', shell = True)
    #Push the new or update files
    call('git push origin master', shell = True)

def get_proxy():
    proxies=[]
    user_agent = {'User-agent': 'Mozilla/5.0'}
    '''
    proxy_url='http://sumanjay.ooo/jsonproxy/proxy.json'
    resp = requests.get(url=proxy_url,headers=user_agent)
    proxy=resp.json()
    proxy=proxy['data']
    '''

    i,j=0,0
    proxy=["182.74.190.66:3128", "103.69.220.11:3128", "117.255.222.65:8080", "43.225.169.55:8080", "117.254.218.69:8080", "103.250.167.227:8080", "103.76.253.156:3128", "43.229.95.243:8080", "115.249.145.202:80", "139.59.7.241:3128", "139.59.7.241:3128", "139.59.41.245:3128", "13.127.244.13:80", "43.230.157.153:56252", "117.239.251.135:80", "139.59.41.245:3128", "43.230.157.153:56252", "117.239.251.133:80", "117.239.251.142:80", "202.3.72.177:55848", "49.128.160.42:33792", "202.61.120.98:30387", "103.89.253.249:3128", "117.254.219.144:23500", "117.196.237.248:8080", "117.206.148.115:8080", "59.145.117.26:3128", "103.251.58.51:61489", "103.250.158.23:32227", "202.91.75.52:8080", "202.160.175.1:40096", "103.46.241.170:55824", "117.252.71.51:8080", "103.15.83.78:8080", "103.109.176.81:47495", "103.54.97.229:53281", "123.201.20.246:50327", "103.209.140.158:53281", "14.142.122.134:8080", "210.212.31.215:8080", "49.128.160.42:33792", "103.209.140.158:53281", "123.201.20.246:50327", "112.133.247.139:8080", "117.206.148.115:8080", "103.251.58.51:61489", "202.160.175.1:40096", "103.54.97.229:53281", "117.254.219.144:23500", "103.109.176.81:47495", "112.133.247.139:8080", "202.61.120.98:30387", "103.250.158.23:32227", "103.194.249.251:48557", "49.249.251.86:53281", "103.15.83.78:8080", "117.196.237.248:8080", "43.224.8.114:50333", "202.3.72.177:55848", "202.91.75.52:8080", "117.252.71.51:8080", "103.46.241.170:55824", "103.87.104.137:8080", "103.44.139.87:54743", "103.65.24.127:49651", "103.70.145.43:8080", "103.99.196.10:34589", "223.196.83.182:53281", "103.43.43.25:40215", "117.196.232.222:8080", "43.229.73.130:51504", "14.142.122.134:8080", "103.194.251.37:58934", "103.106.148.203:60227", "103.58.251.172:8080", "103.69.216.136:8080", "203.115.97.106:31070", "110.172.135.234:34472", "117.197.41.41:42620", "103.106.148.200:55655", "103.242.184.160:58571", "117.239.218.229:3128", "103.194.249.251:48557", "103.87.104.137:8080", "103.194.251.37:58934", "223.196.83.182:53281", "110.172.135.234:34472", "210.212.31.215:8080", "203.115.97.106:31070", "103.65.24.127:49651", "103.99.196.10:34589", "103.70.145.43:8080", "103.58.251.172:8080", "103.44.139.87:54743", "103.69.216.136:8080", "125.16.128.118:3128", "117.196.232.222:8080", "103.89.253.246:3128", "103.106.148.203:60227", "43.229.73.130:51504", "103.105.237.1:32883", "117.212.92.141:8080", "103.106.148.200:55655", "117.252.68.172:32431", "45.116.106.98:8080", "103.43.43.25:40215", "125.21.43.122:8080", "117.232.103.242:56594", "117.212.92.141:8080", "103.206.131.213:39569", "103.216.82.44:8080", "103.105.237.1:32883", "117.232.103.242:56594", "117.254.216.5:8080", "117.240.210.155:53281", "122.102.28.170:53281", "103.54.28.26:61774", "45.116.106.98:8080", "103.242.184.160:58571", "117.197.41.41:42620", "117.254.219.116:8080", "103.212.128.82:8080", "103.206.131.213:39569", "203.192.195.14:31062", "117.240.210.155:53281", "103.240.35.229:54743", "103.218.102.22:8080", "122.102.28.170:53281", "117.254.216.5:8080", "103.98.79.42:46525", "43.229.73.245:38708", "103.198.172.4:50820", "203.192.195.14:31062", "103.89.253.246:3128", "45.112.56.2:46224", "103.54.28.26:61774", "103.218.102.22:8080", "117.254.219.116:8080", "103.198.172.4:50820", "103.98.79.42:46525", "125.21.43.122:8080", "43.229.73.245:38708", "103.240.161.59:48809", "27.116.20.209:36630", "1.186.151.206:36253", "103.100.168.1:8080", "117.254.219.240:8080", "103.49.53.1:83", "103.56.30.128:8080", "27.116.51.21:36033", "45.112.57.230:61222", "103.240.161.59:48809", "43.240.5.225:31777", "103.14.235.26:8080", "103.103.52.53:49650", "103.92.117.129:33891", "1.186.151.206:36253", "103.56.30.128:8080", "103.49.53.1:83", "103.236.114.38:49638", "103.22.173.230:8080", "45.127.121.194:53281", "103.14.235.26:8080", "103.100.168.1:8080", "103.42.161.118:8080", "103.92.117.129:33891", "43.240.5.225:31777", "103.103.52.53:49650", "103.115.180.47:46791", "103.216.172.1:50031", "103.42.161.118:8080", "103.87.25.30:32609", "103.236.114.38:49638", "103.249.180.167:8080", "45.127.121.194:53281", "103.110.20.10:8080", "117.254.218.162:8080", "103.250.156.22:30093", "103.115.180.47:46791", "103.245.188.86:54385", "119.42.152.181:23500", "103.212.128.82:8080", "45.248.65.34:8080", "117.254.218.162:8080", "103.245.188.86:54385", "103.249.180.167:8080", "103.216.172.1:50031", "117.211.166.214:3128", "59.91.127.29:53844", "103.70.205.249:44424", "45.248.65.34:8080", "103.69.220.11:3128", "59.91.127.29:53844", "103.228.76.46:58703", "103.228.76.46:58703", "27.116.51.115:8080", "103.87.25.30:32609", "27.116.51.115:8080", "45.121.29.254:54858", "43.225.23.26:8080", "103.110.20.10:8080", "43.225.23.26:8080", "122.252.235.122:8080", "103.216.175.4:50031", "45.121.29.254:54858", "103.199.157.130:40052", "103.47.218.77:46297", "106.0.37.10:8080", "183.82.32.56:49551", "103.70.205.249:44424", "183.82.32.56:49551", "45.125.61.193:32804", "117.192.8.154:59259", "117.239.240.202:53281", "202.138.127.66:80", "103.239.87.38:34851", "117.192.8.154:59259", "45.125.61.193:32804", "202.138.127.66:80", "103.76.190.193:49939", "103.49.54.1:83", "117.239.240.202:53281", "175.100.185.151:53281", "103.47.218.77:46297", "103.239.87.38:34851", "117.240.59.115:36127", "103.194.248.166:44229", "103.76.190.193:49939", "117.242.154.73:33889", "103.14.235.109:8080", "103.46.233.15:83", "103.14.235.109:8080", "103.220.28.180:45292", "45.115.174.239:8080", "183.87.153.98:49602", "103.211.76.5:8080", "103.49.54.1:83", "202.62.84.210:53281", "103.224.5.13:50133", "183.87.153.98:49602", "43.249.226.225:53281", "175.100.185.151:53281", "103.220.28.180:45292", "202.62.84.210:53281", "43.249.226.225:53281", "202.134.180.50:8080", "45.117.74.174:8080", "45.119.90.47:61572", "103.240.168.130:59496", "202.134.180.50:8080", "103.240.168.130:59496", "49.207.7.131:3128", "14.143.30.202:23500", "45.123.26.146:53281", "103.216.82.46:6666", "103.74.244.126:8080", "43.248.73.86:53281", "183.87.14.250:44915", "103.224.5.5:54143", "103.249.180.134:8080", "45.123.26.146:53281", "103.26.54.94:8080", "14.143.30.202:23500", "45.115.175.143:8080", "103.224.5.5:54143", "43.248.73.86:53281", "183.87.14.250:44915", "49.207.7.131:3128", "103.240.160.21:6666", "103.249.180.134:8080", "103.216.82.46:6666", "103.43.42.85:30477", "14.102.67.101:30337", "114.69.229.161:8080", "103.41.96.46:53281", "103.240.160.21:6666", "103.216.82.50:53281", "103.206.112.49:8080", "103.129.194.1:33691", "103.87.48.20:8080", "14.102.67.101:30337", "103.216.82.50:53281", "103.51.26.233:30867", "103.206.112.49:8080", "103.209.89.67:8080", "103.69.220.14:3128", "119.161.99.25:83", "106.0.37.10:80", "103.109.78.193:53351", "103.87.48.20:8080", "103.72.217.173:48766", "103.69.220.14:3128", "116.197.152.198:61568", "116.197.152.65:61568", "139.5.26.27:53281", "116.197.152.198:61568", "123.108.200.34:83", "103.88.127.246:34927", "103.109.78.193:53351", "116.197.152.65:61568", "103.48.70.193:8080", "103.72.217.173:48766", "103.42.195.70:53281", "139.5.26.27:53281", "119.161.99.25:83", "103.42.195.70:53281", "103.212.129.65:52390", "27.116.20.169:36630", "117.240.151.237:39376", "182.75.110.122:58290", "123.108.200.34:83", "27.116.20.169:36630", "163.53.87.22:8080", "43.225.23.49:8080", "103.199.157.209:40052", "103.199.157.209:40052", "103.225.30.1:53281", "103.216.82.190:6666", "103.36.124.121:53606", "103.226.1.101:8080", "103.102.73.74:46878", "103.52.220.5:49068", "103.69.220.13:8080", "103.226.1.101:8080", "103.102.73.74:46878", "103.109.78.6:53351", "103.69.220.13:8080", "103.36.124.121:53606", "103.52.220.5:49068", "103.253.211.182:80", "103.75.161.38:21776", "103.194.240.54:48989", "103.109.78.6:53351", "103.225.30.1:53281", "103.65.193.249:55417", "103.194.240.54:48989", "103.75.161.38:21776", "103.42.162.58:8080", "103.253.211.182:80", "103.76.188.133:46671", "103.42.162.58:8080", "103.65.193.249:55417", "103.216.82.29:6666", "139.5.26.28:8080", "114.69.235.105:8080", "117.196.231.201:37769", "114.69.235.105:8080", "117.196.231.201:37769", "103.26.55.218:8080", "103.85.92.221:8080", "103.205.112.1:23500", "103.253.169.115:32731", "103.88.221.114:31205", "103.255.234.81:39847", "103.85.92.221:8080", "103.88.221.114:31205", "103.226.202.1:8080", "103.255.234.81:39847", "103.253.169.115:32731", "103.250.153.198:59451", "1.186.63.130:39142", "103.21.161.105:6666", "103.226.202.1:8080", "103.82.99.161:59376", "103.205.112.129:23500", "125.62.193.21:83", "103.250.166.17:6666", "103.250.153.198:59451", "103.21.161.105:6666", "103.226.3.233:8080", "111.125.194.156:53281", "103.205.112.129:23500", "125.62.193.21:83", "103.226.3.233:8080", "183.82.116.56:8080", "103.250.166.17:6666", "14.102.44.136:60175", "183.82.116.56:8080", "14.102.44.136:60175", "45.122.46.36:60416", "45.125.61.209:32804", "45.122.46.36:60416", "43.224.182.140:40779", "45.125.61.209:32804"]
    for p in proxy:
        url = 'http://pubproxy.com/api/proxy?country=IN&limit=20&https=True&user_agent=true'
        while(len(proxies)<5000):
            try:
                j=0
                resp = requests.get(url=url,headers=user_agent,proxies={"http": p, "https": p})
                data = resp.json()
                time.sleep(2.1)
                for proxy in data['data']:
                    proxies.append(proxy['ipPort'])
                print('Length of Proxy till '+str(i)+'th attempt is ',len(proxies))
            except Exception as e:
                #print_exc()
                print('Skipped proxy '+str(p)+" "+str(i)+' time')
                break
            finally:
                i=i+1

    try:
        print("Entered Spy proxy")
        proxies=proxies+spy_proxy()
    except Exception :
        pass
    try:
        proxies=proxies+fate_proxy()
    except Exception:
        pass
    return proxies

def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    #print(len(np_list))
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    return(proxy)

def spy_proxy():
    resp=requests.get('http://spys.me/proxy.txt')
    data=((resp.text).split("Google_passed(+)")[1]).split('\r')[0]
    data=data.split('\n')
    l=[]
    for i in data:
        if 'IN' in i:
            i=i.split(' IN')[0]
            l.append(i)
    return l


proxy_json={'data':get_proxy()}
import json
with open('proxy.json', 'w') as outfile:
    json.dump(proxy_json, outfile)
push_to_git()
