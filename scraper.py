import urllib.request
import urllib.parse
import re
import os

# extract all sources from given tag and save to file
def get_src(url, tag):
	data = _get_data(url)
	images = re.findall(r'<'+tag+' src="(.*?)"', str(data))
	_save_to_file(images)
	return images

# get contents of given tag
def get_tag_content(url, tag):
	data = _get_data(url)
	titles = re.findall(r'<'+tag+'>(.*?)</'+tag+'>', str(data))
	_save_to_file(titles)
	return titles

# get basic request and fetch data
def _get_data(url):
	req = urllib.request.Request(url)
	rsp = urllib.request.urlopen(req)
	rspData = rsp.read()
	return rspData

# save results to file, every entry on new line
def _save_to_file(res):
	try:
		os.remove('results.txt')
	except Exception as e:
		print(e)

	with open('results.txt', 'a') as file:
		for line in res:
			file.write(line + '\n')
		file.close()
