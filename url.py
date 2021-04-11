import requests
import json

class lunar():
    def __init__(self, date):
        self.date = date
    def GetDataFromAPI(self):
        url = "http://api.tianapi.com/txapi/lunar/index?key=5510bf676ff04202ebba97000b753784&date="+self.date
        r = requests.get(url)
        data_str =  r.content.decode("utf-8")
        data_dict = json.loads(data_str)
        if data_dict["code"] != 200:
            return {}
        else:
            return data_dict
