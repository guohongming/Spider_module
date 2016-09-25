__author__ = 'Goomy'
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time


class Spider(object):

    def __init__(self):

        self.__session = requests.Session()
        self.__header = {
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':"gzip, deflate, sdch",
            'Accept-Language':"zh-CN,zh;q=0.8",
            'Connection':'keep-alive',
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"
        }


    def login(self):


        return


    def get_html_from(self,the_url):
        while 1:
            try:
                response = self.__session.get(url=the_url, headers=self.__header)
                the_html = response.text
                return the_html
            except Exception as e:
                print('there is a error:',e)


    def post_frame_to(self,the_frame,the_url):

        response = self.__session.post(url=the_url,data = the_frame,headers = self.__header)

        return  response


