import json

filename = 'username.json'

try:
    with open(filename) as f :
        username =  json.load(f)
except:
    username = input("请输入你的名字")
    with open(filename,'w') as f :
        json.dump(username,f)
        print(f"欢迎你回来{username}")
else: print(f"来了{username}")