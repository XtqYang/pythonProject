#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
# 取消证书校验
import warnings

warnings.filterwarnings("ignore")
url = 'https://api.cn2030.com//sc/api/User/OrderPost'
headers = {
    'Host': 'api.cn2030.com',
    'Connection': 'keep-alive',
    'Content-Length': '418',
    'referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/97/page-frame.html',
    'xweb_xhr': '1'}
cookies = {
    'ASP.NET_SessionId': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Nzg1MjI4MDUuMTI4NDY0OSwiZXhwIjoxNjc4NTI2NDA1LjEyODQ2NDksInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIzMDMxMTE2MjAwNCIsInZhbCI6Ii84aFJBUUlBQUFBRWJtOXVaUnh2Y1hJMWJ6VlFXbkUzZVZRMVlUVjJiVlZ3Tm10eU0wTTRVSHBOQVJ4dlZUSTJXSFExVG0xR01HMTJcclxuU1ZkQ2RtWkRUVnB1TkVjMFp6UlJEVEV4Tnk0eE16WXVOalF1T1RJQUVGODRhRkpCWkRSQlFWRkRObk5FVVVJQkFBQUFBQT09In0.RYDOfvNsuBeJbPPcOZ7nH7PTPEe08qxwF8csE6T-lF8',
    'path': '/'
}
data = "73e73affd092526a56273ceb14a5521b075658baee243fe70bcb71014dd347743dc1346766247191920e0c27ecf1d612d3537785009f4ab4d982be02eaa5e88b7deb2dba6b812a321188550ed6c60191a80415510a665f6f7f8dc808baac9dccf63933ae4679a9fdcf58970f5dec6847f0957e9c9160754d629bce618e178c5cfcf573a58bae4eabd57179b9ac38b873b3e128453937e714006c93fb2ef7c1e5ebd3c19472a8fb6c4f797c2ae913afc3413d31f9ee2368f881c59d9d9d3ce22e8665283dff532d2894108f37daacb6a3"

html = requests.post(url, headers=headers, verify=False, cookies=cookies, data=data)
print(html.text)
