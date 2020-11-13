import hashlib
import os

hashlist = ['','','']
pattern = ''
choice = 0

os.system('more bashban ')


print("\nWelcome to Crypto-Pass, let's create a secure crypto-password for you!!!")
print("1- first choose 3 secure words for your 3 first keys\n2- create symbol pattern(@!@#, 9*&¨1)\n3- choose where you want your pattern")

hashlist[0] = input("\nTell me the first key: ")
hashlist[1] = input("\nTell me the second key: ")
hashlist[2] = input("\nTell me the third key: ")
pattern = input("\nChoose a symbol pattern: ")

sha = ['','','']
sha[0] = hashlib.sha256(str(hashlist[0]).encode("utf-8")).hexdigest() 
sha[1] = hashlib.sha256(str(hashlist[1]).encode("utf-8")).hexdigest() 
sha[2] = hashlib.sha256(str(hashlist[2]).encode("utf-8")).hexdigest() 

mdp = ['','','']

mdp[0] = hashlib.md5(str(sha[0]+sha[1]).encode("utf-8")).hexdigest()
mdp[1] = hashlib.md5(str(sha[1]+sha[2]).encode("utf-8")).hexdigest()
mdp[2] = hashlib.md5(str(mdp[0]+mdp[1]+sha[0]).encode("utf-8")).hexdigest()

while choice == 0:
	choice = int(input("\n1- Beginning\n2- Final \n3 - Both\nWhere you want your pattern: "))
	if choice > 3 or choice < 1:
		choice == 0
	
	elif choice == 1:
		print("\nYour cryptopass: ", pattern+mdp[2])
	elif choice == 2:
		print("\nYour cryptopass: ", mdp[2]+pattern)
	elif choice == 3:
		print("\nYour cryptopass: ", pattern+mdp[2]+pattern)






