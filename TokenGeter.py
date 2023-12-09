import requests

if __name__ == '__main__':
        headers = {
            'Host': 'nls-meta.cn-shanghai.aliyuncs.com'
        }
        url = 'https://www.baidu.com/s'
        content = input('请输入您想查询的词：')
        param = {
            'wd': content,
            'pn': 0
        }
        response = requests.get(url=url, params=param, headers=headers)  # 三个参数
        ctx = response.text
        print("获取Token:" + ctx)
