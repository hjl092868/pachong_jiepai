#spider.py
#提取各“分页”的url，并读取url中所有内容

import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json

def get_page_index(offset,keyword):
	data = {
	'offset':offset,
	'format':'json',
	'keyword':keyword,
	'autoload':'true',
	'count':'20',
	'cur_tab':'1'
	}

	url = 'https://www.toutiao.com/search_content/?' + urlencode(data)#from urllib.parse import urlencode
	try:#避免网址输入错误而影响程序中断
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求索引页面出错')
		return None

def parse_page_index(html):
	data = json.loads(html)
	if data and 'data' in data.keys():
		for item in data.get('data'):
			yield item.get('article_url')

def get_page_detail(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		print('请求详情页出错',url)
		return None

def main():
	html = get_page_index(0,'街拍')
	for url in parse_page_index(html):
		print(get_page_detail(url))

if __name__ == '__main__':
	main()