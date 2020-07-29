import wlog
import requests
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

# global var
url = 'https://www.coches.net/'
filepath = 'html/coches.html'
header = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

class Scrapper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url = url
        self.__wlog = wlog

    def retrive_webpage(self):
        try:
            html = urlopen(Request(url,data=None, headers=header))
            #html = urlopen(url)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
        else: 
            self.__data = html.read()
            print(type(self.__data))
            if len(self.__data) > 0:
                print('successfully retrived')

    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
    
    def read_webpage_from_html(self,filepath=filepath):
        try: 
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def change_url(self, url):
        self.__url = url
    
    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, 'html.parser')
    
    def parse_soup_to_simple_html(self):
        car_list = self.__soup.find_all('div', {'class':'sui-CardBasic-description'})
        print(car_list)