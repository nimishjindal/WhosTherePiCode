from GetStaticUrl import GetStaticUrl
import time

gsu = GetStaticUrl("127.0.0.1",4040)

try:
	maxTry = 5
	while not gsu.check_running() and maxTry>0: 
		print("not up yet")
		maxTry -= 1
		time.sleep(2)
	
	if maxTry<=0:
		print("time out")
		
	else:		
		ur = gsu.Static_url()
		print(ur)
	
except Exception as e:
	print(e)