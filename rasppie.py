import requests
import json
import pprint
import subprocess


# r = requests.get('http://localhost:8000/adverts/list',)
r = requests.post('http://localhost:8000/rest_auth/login/',data={'username':'kirega','password':'mtotomdogo'})

r = r.content.decode('utf-8')
r = json.loads(r)
print(r['key'])

q = requests.get('http://localhost:8000/adverts/list', headers={'Authorization':'Token ' + r['key']})
q = q.content.decode('utf-8')
q = json.loads(q)

l=[]
m = [23,20]
m= ','.join(map(str,m))
print("message" + m)
q = requests.get('http://localhost:8000/adverts/list?id__in= '+ m, headers={'Authorization':'Token ' + r['key']})
q = q.content.decode('utf-8')
q = json.loads(q)
print(q)
# for each in q :
#     # print(each['upload'])
#     l.append(each['upload'])
#     m = each['upload']

# for i in l[:1]:
    # subprocess.Popen(['wget','-r',i])
    
# subprocess.Popen(['vlc','--loop','-f', i ])

# subprocess.Popen(['./localhost:8000/media/ad/loop-several.sh'])
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
print(get_sec(q[0]['duration']))