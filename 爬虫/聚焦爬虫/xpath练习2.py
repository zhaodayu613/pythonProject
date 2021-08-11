#爬取网址照片
import  requests
from lxml import  html
import  os

url = 'https://pic.netbian.com/4kmeinv/'
header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page_text = requests.get(url= url, headers= header).text

tree = html.etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
#如果这个文件夹不存在，那么就创建一个
if not os.path.exists('./piclibs'):
    os.mkdir('./piclibs')

for li in li_list:
    #./表示的是li标签
    img_src='https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]   # 因为xpath拿到的是一个列表 但是这个列表目前只有一个元素
    img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
    #下面代码是解决中文乱码的通用
    img_name=img_name.encode('iso-8859-1').decode('gbk')
    print(img_name,img_src)
    #请求图片进行持久化存储
    img_data = requests.get(url= img_src,headers=header).content   #存储二进制的要用conten
    img_path = 'piclibs'+ img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,"下载成功")
