#爬取三国演义具体章节名称以及章节内容

from bs4 import BeautifulSoup
import lxml
import  requests

#获取页面章节信息
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page_text = requests.get(url=url, headers=header).text.encode('ISO-8859-1')#加上后缀 .encode 可以解决乱码
#获取具体的章节详情网址的进入网址 是需要利用beautifulsoup
#创建BeautifulSoup对象
soup = BeautifulSoup(page_text, 'lxml')
#解析章节标题和信息的具体页面的url
li_list =soup.select('.book-mulu>ul>li')   #  .表示class class=book-mulu  slect 可以拿到所有的Li标签内容 返回一个列表
fp= open('./sanguo.text','w',encoding='utf-8')  #w为了接受 章节标题以及内容的 需要将章节标题和内容做一个拼接
#遍历所有Li标签拿到所有章节细节的网址
for list in li_list:
    title =list.a.string   #拿到标题
    detail_url = 'https://www.shicimingju.com/'+ list.a['href']
    #对详情页发起请求 解析其详细内容
    detail_page_text = requests.get(url=detail_url,headers=header).text.encode('ISO-8859-1')
    #拿到了具体的文本 里面的P标签才是具体内容     +======这个beatifulsouP就是拿标签的吧
    detail_soup =BeautifulSoup(detail_page_text, 'lxml')
    div_tag = detail_soup.find('div', class_='chapter_content')  # class_  表示的属性 一定要加下划线
    content = div_tag.getText()
    fp.write(title+':'+content+'\n')
    print(title+"打印完成")


