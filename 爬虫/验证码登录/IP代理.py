import requests
url='https://www.baidu.com/s?ie=UTF-8&wd=ip&tn=62095104_35_oem_d'
header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
#这个proxies就是放代理IP的  需要传一个字典，键要放是http,或者https
page_text =requests.get(url=url, headers=header,proxies={'http':'117.27.113.33'}).text
with open('./ip.html', 'w',encoding='utf-8') as fp:
    fp.write(page_text)
