from doubaninfo.douban_book import *
from doubaninfo.douban_movie import *
import argparse
import os
import pyperclip

def readargs():
    parser = argparse.ArgumentParser(description='Weclome DoubanInfo')
    parser.add_argument('-u','--url', type=str, help='Input your douban-url',required=True,default='')
    parser.add_argument('-c','--cookie', type=str, help='Input your douban-cookie',required=False,default='')
    parser.add_argument('-j','--json', action='store_true', default=False,  help='Output as json format',required=False)
    parser.add_argument('-cp','--copy', action='store_true', default=False,  help='Copy the output to the clipboard',required=False)

    args = parser.parse_args()
    return args


def getdoubaninfo(url:str='',cookie:str='',cp:bool=False):
    if 'movie.douban.com' in url:
        if cookie.strip()=='':
            page_parse=MoviePageParse(movie_url=url)
        else:
            page_parse=MoviePageParse(movie_url=url,cookie=cookie)
    elif 'book.douban.com' in url:
        if cookie.strip()=='':
            page_parse=BookPageParse(book_url=url)
        else:
            page_parse=BookPageParse(book_url=url,cookie=cookie)
    else:
        raise Exception('豆瓣链接填写错误')
    res=page_parse.info()
    print('\n'+res)
    if cp:
        pyperclip.copy(res)


def getdoubaninfo_json(url:str='',cookie:str=''):
    if 'movie.douban.com' in url:
        if cookie.strip()=='':
            page_parse=MoviePageParse(movie_url=url)
        else:
            page_parse=MoviePageParse(movie_url=url,cookie=cookie)
    elif 'book.douban.com' in url:
        if cookie.strip()=='':
            page_parse=BookPageParse(book_url=url)
        else:
            page_parse=BookPageParse(book_url=url,cookie=cookie)
    else:
        raise Exception('豆瓣链接填写错误')
    print( page_parse.parse())
