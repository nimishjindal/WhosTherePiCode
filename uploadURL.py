from GetStaticUrl import GetStaticUrl
import time
import boto3
from config import awsCreds as creds

def uploadurl():

	gsu = GetStaticUrl("127.0.0.1",4040)

	filename = "StaticURL.txt"
	bucket_name = 'alexangrokurl'

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
			
			with open("/home/pi/Desktop/"+filename,"w") as file:
				file.write(url)

			session = boto3.Session(aws_access_key_id = creds["AWS_SERVER_PUBLIC_KEY"], aws_secret_access_key = creds["AWS_SERVER_SECRET_KEY"])
			s3 = session.resource('s3')
		
			s3.meta.client.upload_file("/home/pi/Desktop/"+filename, bucket_name, filename)
			print("done")
			return True
			
	except Exception as e:
		print(e)
		return False