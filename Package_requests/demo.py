import json

import requests


class TestAddress:
    def setup(self):
        # 每个函数都要用到token信息，提取到setup函数
        self.token = self.get_token()

    # 用get请求，拿到token
    def get_token(self):
        proxies = {'https': 'http://127.0.0.1:8080'}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwbcb5a10dc1f2c784&corpsecret=AKLMPeMVpulW6_aQYw3KfRk3k-9TsesvVN7Q5EQItoQ'
        r = requests.get(url, proxies=proxies, verify=False)
        return r.json()['access_token']

    def test_get_information(self):
        proxies = {'https': 'http://127.0.0.1:8080'}
        user_id = 'WangWei'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}'
        r = requests.get(url=url, proxies=proxies, verify=False)
        print(r.text)

    def test_add_member(self):
        proxies = {'https': 'http://127.0.0.1:8080'}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "wangwei002",
            "name": "wangwei002",
            "mobile": "+86 13611240702",
            "department": [3],
        }
        r = requests.post(url=url, data=json.dumps(data), proxies=proxies, verify=False)
        print(r.text)

    def test_update_member(self):
        proxies = {'https': 'http://127.0.0.1:8080'}
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "wangwei002",
            "name": "王为002-2",
            "mobile": "+86 13611240703",
            "department": [2, 4],
        }
        r = requests.post(url, json=data, proxies=proxies, verify=False)
        print(r.text)

    def test_delete_member(self):
        user_id = 'wangwei002'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}'
        r = requests.get(url)
        print(r.text)
