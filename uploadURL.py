from GetStaticUrl import GetStaticUrl
import time

gsu = GetStaticUrl("127.0.0.1",4040)

try:
	maxTry = 8
	
	while not gsu.check_running() and maxTry>0: 
		print("not up yet")
		maxTry -= 1
		time.sleep(2)
	
	if maxTry<=0:
		print("time out")
		
	else:
		time.sleep(5)
		url = gsu.Static_url()
		print(url)
		
		with open("/home/pi/Desktop/StaticURL.txt","w") as file:
			file.write(url)
	
except Exception as e:
	print(e)