#爬取二手房标题信息

import  requests
from lxml import html

url ='http://bj.58.com/ershoufang/'
header={'uesr-agemt':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page_text = requests.get(url=url,headers =header).text
#数据解析
tree=html.etree.HTML(page_text)
li_list=tree.xpath('//section[@class="list"]/div')  #这一步是没有错的   但是拿的是一个空列表我曹！
print(li_list)
for li in li_list:
    title=li.xpath('//div[class@="property-content-detail"]/h3/text()')
    print(title)
