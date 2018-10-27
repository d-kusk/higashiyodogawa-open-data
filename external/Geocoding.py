from time import sleep
import requests
import sys
import os
from utility.XMLConverter import XMLConverter
sys.path.append(os.pardir)


class Geocoding():
    def __init__(self):
        self.__url = 'http://www.geocoding.jp/api/'

    def location(self, address):
        querys = {'q': address, 'v': '1.1'}
        sleep(5.5)  # APIの制限で5秒以上置いてリクエストする必要がある
        response = requests.get(self.__url, params=querys)
        response_dict = XMLConverter().convertToDict(response.text)

        location = {}
        location["latitude"] = response_dict["result"]["coordinate"]["lat"]
        location["longitude"] = response_dict["result"]["coordinate"]["lng"]
        return location
