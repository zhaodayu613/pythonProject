#图片网址背后是二进制数据 用content接收
import requests

url = 'https://img.yalayi.net/d/file/2020/06/22/bed0c8033d95948ba6ee6774d1eeb980.jpg'
data= requests.get(url=url).content
with open('./pic.jpg', 'wb') as  fp:
    fp.write(data)
