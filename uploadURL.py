from GetStaticUrl import GetStaticUrl
import time
import boto3

gsu = GetStaticUrl("127.0.0.1",4040)
AWS_SERVER_PUBLIC_KEY = "AKIAIEALTGGGYW5SU33A"
AWS_SERVER_SECRET_KEY = "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"

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
		
		s3_client = boto3.client('s3', 
                      aws_access_key_id = AWS_SERVER_PUBLIC_KEY, 
                      aws_secret_access_key = AWS_SERVER_SECRET_KEY, 
                      )
	
except Exception as e:
	print(e)