from selenium import  webdriver
import  requests
from lxml import html
#导入一个浏览器对象（传入浏览器的驱动程序）  大写的C
bro = webdriver.Chrome(executable_path='D:\Google\Chrome\Application\chromedriver.exe')
#让浏览器发起一个指定的URL对象请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#page_source获取浏览器当前页面的页面源码数据
page_text= bro.page_source
#解析企业的名称
tree=html.etree.HTML(page_text)
#拿到所有包含标题的Li标签
li_list=tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)