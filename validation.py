import random
import requests
def validate():
	print("Authentication Required!\n")
	number = input("Enter your mobile number: ")
	OTP = random.randint(1000, 9999)
	print('"OTP sent to', number, "is" , OTP, '"')
	message = str(OTP)
	url = "https://www.fast2sms.com/dev/bulkV2?authorization='key'&language=english&route=q&numbers=" + number + "&message=" + message;
	response = requests.get(url)
	recived_OTP = int(input("Enter OTP: "))
	if(OTP == recived_OTP):
		print("Welcome")
	else:
		print("Authentication failed!")
		exit()
if __name__ == "__main__" :
	validate()