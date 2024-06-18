import requests
from requests.auth import HTTPBasicAuth

# 目标网页的URL
url2 = 'http://www.cs.xjtu.edu.cn/info/1233/3336.htm'
# 发送GET请求，使用自定义的headers

response = requests.get(url2)

# 检查请求是否成功
if response.status_code == 200:
    # 请求成功，打印网页内容
    with open('out.txt', 'w',encoding='utf-8') as f:
        f.write(response.content.decode())
else:
    # 请求失败，打印状态码和原因
    print('Failed to retrieve content, status code:', response.status_code)