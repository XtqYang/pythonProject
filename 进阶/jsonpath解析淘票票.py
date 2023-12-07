import jsonpath
import json
import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1667572503517_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    # 带冒号的请求头一般情况下不好使
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br'#默认请求头支持gzip...需要注释掉
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 't=200e3007722d7ef3d3410a5d08d30d99; cookie2=125d94163993147b99d7ae1f61939911; v=0; _tb_token_=357835e763eb; cna=IBDsG0Ww800CAd9o1qFkbc4u; xlly_s=1; _m_h5_tk=7061f8c47f3e690e915b738089686a8e_1667582411558; _m_h5_tk_enc=c0a2e78ebcaebc516d070fc7de92e912; thw=cn; l=eBLcG58RTJFW46GhBOfZlurza77OJIRYIuPzaNbMiOCPOgfH5hfAW6r7aO8MCnGVhs1eR3rp2umHBeYBqC2sjqj2nAHOr_Dmn; tfstk=clwPByqPjTBrn_qdWxDUQ8hzYOcRZ80n5KoZZwm-mKZ9yDhliX8KmN7I0D-2-bf..; isg=BIqKYiwC3aATeFEMZsoRO_zZ23Asew7VEXfWdRTDBl1oxyqB_Avg5YQ51zMbDoZt',
    'Host': 'dianying.taobao.com',
    'Referer': 'https://dianying.taobao.com/index.htm?spm=a1z21.3046609.header.3.32c0112at9cXGf&n_s=new',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 获得的json数据头部jsonp109(和尾部);需要去掉
# split切割
content = content.split('(')[1].split(')')[0]
with open('D:\code\pythonProject\wj\json\jsonpath.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
# 不能读字符串只能读文件加上open  ‘r’ en...
obj = json.load(open('D:\code\pythonProject\wj\json\jsonpath.json', 'r', encoding='utf-8'))
st = jsonpath.jsonpath(obj, '$..regionName')
print(st)
