from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://www.dxsbb.com/news/7566.html')
print(r.html.html)