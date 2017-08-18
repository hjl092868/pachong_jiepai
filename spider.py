#spider.py
#提取“主页”的所有信息

import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode

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
	response = requests.get(url)
	try:#避免网址输入错误而影响程序中断
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def main():
	html = get_page_index(0,'街拍')
	print(html)

if __name__ == '__main__':
	main()