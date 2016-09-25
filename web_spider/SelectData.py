__author__ = 'Goomy'
# coding:utf-8
from bs4 import BeautifulSoup
import re

class SelectData(object):


    def __init__(self,html=''):
        self.__html = html


    def select_content(self):
        bs = BeautifulSoup(self.__html)
        book_bs = bs.find('div',{'id':"content"})
        book_article  = book_bs.find('div',{'class':'article'})
        article_lis = book_article.find_all('li')
        book_list = []
        for li in article_lis:
            if li.get_text()=='':
                continue
            # print(li)
            book_info = []
            # 书名
            book_name = li.find('h2').get_text()
            p=re.compile('\s+')
            book_name=re.sub(p,'',book_name)
            # 简介
            simple_intro_bs = li.find('p')
            simple_intro = simple_intro_bs.get_text()
            p=re.compile('\s+')
            simple_intro=re.sub(p,'',simple_intro)
            # 内容简介
            content_intro = simple_intro_bs.find_next('p').get_text()
            p=re.compile('\s+')
            content_intro=re.sub(p,'',content_intro)
            # id
            book_url = li.find('a')['href']
            # print(book_url)
            p = re.compile('\d+')
            book_id = p.search(book_url).group()

            # 图片url
            pic_url = li.find('img')['src']

            book_info.extend((book_id,book_name,simple_intro,content_intro,pic_url))
            # print(book_info)
            book_list.append(book_info)
        # book_aside = book_bs.find('div',{'class':'aside'})

        return book_list




