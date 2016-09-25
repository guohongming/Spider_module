__author__ = 'Goomy'

from Spider import Spider
from SelectData import SelectData
import csv

def write_file(filename,data):
    with open(filename, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)
    pass

if __name__ =='__main__':

    the_spider = Spider()
    html_new_all = the_spider.get_html_from('https://book.douban.com/latest?icn=index-latestbook-all')
    # print(html_new_all)
    se_html = SelectData(html_new_all)
    data = se_html.select_content()
    write_file('新书.csv',data)