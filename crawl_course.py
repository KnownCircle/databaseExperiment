from time import sleep
import requests
from urllib.parse import unquote

url = "https://ehall.xjtu.edu.cn/jwapp/sys/kcbcx/modules/qxkcb/qxfbkccx.do"

# 每次访问浏览器获取的Cookie有时效性，大概半个小时会失效，需要重新获取。每次只需要更新Cookies，其他选项不需要变
headers = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: EMAP_LANG=zh; THEME=teal; _WEU=didhvF7R3Dzk8iJL3FarAQd68fGVz6Ktw1H1YbA_ZiIcBpKXWyWLATb4h07QYNdyRwMHb5n13bW1D9vBghDaFTpXI5pI_MIdbkNShNs5k*ybsolrp3VilQZd5FVR1JZMqme9fHd0kLTfhF5sNaD6igpE0T2q2bi9Fsqf7mMKrh8.; route=ab22dc972e174017d573ee90262bcc96; CASTGC=Dsm979dmlzBrGKRzQX0ZAlMdhruWul7nV79xmHB4radbmrpjdq5Ysg==; MOD_AMP_AUTH=MOD_AMP_ca64863e-e72d-41b7-bc7c-5273a362b9d7; asessionid=4eb595a4-7a96-4307-b723-2b6bda602957; amp.locale=undefined; JSESSIONID=Jjgmnu78_2NgQ663YP2g1Fy8iLJKfyKZM-0XTnbzV0_i2GEDPkqJ!-1207711698Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
"""
# 将字符串类型转化为字典类型
header={} 
for item in headers.split('\n'):
    if not item:
        break
    line=item.split(': ')
    header[line[0]]=line[1]

# http报文内容
def get_params(num):
    # num就是页数。每一页有10条信息，共有4364条，所以num范围是1-437
    encoded_query=f"querySetting=%5B%7B%22name%22%3A%22XNXQDM%22%2C%22value%22%3A%222023-2024-2%22%2C%22linkOpt%22%3A%22and%22%2C%22builder%22%3A%22equal%22%7D%2C%5B%7B%22name%22%3A%22RWZTDM%22%2C%22value%22%3A%221%22%2C%22linkOpt%22%3A%22and%22%2C%22builder%22%3A%22equal%22%7D%2C%7B%22name%22%3A%22RWZTDM%22%2C%22linkOpt%22%3A%22or%22%2C%22builder%22%3A%22isNull%22%7D%5D%5D&*order=%2BKKDWDM%2C%2BKCH%2C%2BKXH&pageSize=10&pageNumber={num}"
    decoded_query = unquote(encoded_query) # 将%5B等转化为utf8类型的字符
    query_params = dict(item.split('=') for item in decoded_query.split('&'))
    return query_params

# 发送POST请求
def post_request():
    with open('course.txt', 'w',newline='') as f:
            # sleep(2.5)
            response = requests.get(url, headers=header, params=get_params(0))  # 请求第0页的数据 
            # ！！！请求第0页会一次性返回所有数据 否则需要自己手动一页一页爬
            # 离了个大谱
            # 一页一页爬需要get_params()函数每次传入正整数遍历437页
            print(f"响应状态码：{response.status_code}")
            # 解析JSON响应
            if response.status_code == 200:
                try:
                    data = response.json()
                    rows=data["datas"]["qxfbkccx"]["rows"]
                    for item in rows:
                        cno=item['KCH']
                        cname=item['KCM']
                        period=int(item['XS'])
                        credit=int(item['XF'])
                        teacher=item['SKJS']
                        str=f"{cno}${cname}${period}${credit}${teacher}" # 课程名中有空格，所以使用$作为分隔符
                        f.write(str+'\n')
                        # print(str)
                except requests.exceptions.JSONDecodeError as e:
                    print("JSON解码错误:", e)

if __name__ == '__main__':
    post_request()