from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
import socket


class GetStaticUrl:
	def __init__(self,hostname,port):
		self.hostname = hostname
		self.port = port
		self.url = "http://" +hostname+ ":" +str(port)+"/api/tunnels"
		
	def check_running(self):
		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((self.hostname,self.port))
		print(result)
		if result == 0:
			print ("Port is not open")
			return True
		else:
			print ("Port is open")
			return False

	def Static_url(self):
		try:
			resp = requests.get(url=self.url)
			print(resp.json())
			return str("")
		except Exception as e:
			print(e)
			return str(e)
			
			
	def Static_url_old(self):
		try:
			resp = requests.get(str(self.url))
			http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
			html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
			encoding = html_encoding or http_encoding
			soup = BeautifulSoup(resp.content, "lxml")
			tags = soup.find_all(type="text/javascript")

			print("tags")
			print(tags)
			
			want = tags[5]
							
			urls = re.findall("https://[0-9a-zA-Z]{8}\.ngrok\.io",str(want))

			
			return str(urls[0])
		except Exception as e:
			print(e)
			return str(e)
			
if __name__ == '__main__':
	try:
		gsu = GetStaticUrl("127.0.0.1",4040)
		url = gsu.Static_url()
		print(url)
	except Exception as e:
		print(e)