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
			resp = requests.get(url=self.url).json()
			statUrl = resp["tunnels"][0]["public_url"]
			print(statUrl)
			return str(statUrl)
		except Exception as e:
			print(e)
			return str("could not connect to the server")
			
if __name__ == '__main__':
	try:
		gsu = GetStaticUrl("127.0.0.1",4040)
		url = gsu.Static_url()
		print(url)
	except Exception as e:
		print(e)