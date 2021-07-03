import requests

class HttpRequests:
    def http_requests(self,method,url,data,cookies = None):
        if method.lower() == 'get':
            requests.get(url,params=data,cookies =cookies)
        else:
            res = requests.post(url, json=data, cookies=cookies)
            print(res.json())
            return res

if __name__ == '__main__':
    url = 'https://openapiv5.ketangpai.com/UserApi/loginByMobile'
    data = {
        "code": "179035",
        "email": "",
        "mobile": "18349246200",
        "password": "",
        "remember": "0",
        "reqtimestamp": 1624106623078,
        "type": "login"
    }
    res= HttpRequests().http_requests('post',url,data)

