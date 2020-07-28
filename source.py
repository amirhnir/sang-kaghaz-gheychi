# programmer : AmirHossein Naei
# website : amirhn.ir

import random
emtiyaz = 0
while(1):
	print("emtiyaz : " +str(emtiyaz))
	entekhab = input("1- sang \n2- kaghaz \n3- gheychi \n")
	entekhab = int(entekhab)
	if entekhab == 0 : 
		break
	if (entekhab != 1) and (entekhab != 2) and (entekhab != 3):
		print("voroodi na motabar ast")
		break
	entekhabesystem = random.randint(1,3)
	entekhabesystemstring = ""
	if entekhabesystem == 1 : entekhabesystemstring = "sang"
	elif entekhabesystem == 2 : entekhabesystemstring = "kaghaz"
	elif entekhabesystem == 3 : entekhabesystemstring = "gheychi"
	print("entekhabe system : "+entekhabesystemstring)
	if(entekhabesystem == 1 and entekhab == 2) or (entekhabesystem == 2 and entekhab == 3) or (entekhabesystem == 3 and entekhab == 1):
		print("shoma barande shodid !!!")
		emtiyaz+=1
	elif entekhabesystem == entekhab :
		print("mosavi shodid !!")
	else :
		print("shoma bakhtid !!!")
		emtiyaz-=1
	print("\n\n")
