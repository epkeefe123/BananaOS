import time
import os
import sys
import random

#Disk Int
Hours = '503'
storeusd = '1GB'
bsec = '2'
man = 'WD'
inter = 'IDE'



#Dir Int
dirtop = "  Dir       File      Dir      BootFile"
dirbot = "Banana     Readme     sys      boot.sys"

#format int
def format():
        print ("ALL DATA WILL BE DESTROYED")
        time.sleep(5)
        print ("Mounting Disk")
        time.sleep(3.2)
        print ("Formatting")
        time.sleep(3)
        print ("Formatting.")
        time.sleep(2)
        print ("Formatting..")
        time.sleep(0.5)
        print ("Formatting...")
        storeusd = '0.5GB'
        bsec = '0'
        inter = 'Requires setup'
        print ("Done!... Reinstalling Banana OS From Cache")
        time.sleep(10)
        print ("Done!")
        time.sleep(2)
        os.system ('clear')
        menu()


#menuint
def menu():
	cmd = input("sky@localdisk $")
	if cmd == 'shutdown':
		sys.exit()
	elif cmd == 'ls':
		print (dirtop)
		print (dirbot)
		menu()
	elif cmd == 'clear':
		os.system ('clear')
		menu()
	elif cmd == 'disk':
		print ("Finding Disk Info")
		time.sleep(3)
		print ("Disk Info:")
		time.sleep(0.5)
		print ("Storage Used:", storeusd)
		time.sleep(0.5)
		print ("Run Hours:", Hours)
		time.sleep(0.5)
		print ("Bad Sectors:", bsec)
		time.sleep(0.7)
		print ("Manufacturer:", man)
		time.sleep(2)
		print ("Interface:", inter)
		menu()
	elif cmd == 'format':
		print ("Proceed With Format?")
		dec = input("Y/N:")
		if dec == 'N':
			menu()
		elif dec == 'n':
			menu()
		elif dec == 'Y':
			format()
		elif dec == 'y':
			format()





#bios
os.system('clear')
print ("Banana BIOS")
time.sleep(0.5)
print ("Checking ROM")
time.sleep(1)
print ("Checking ROM.")
time.sleep(1)
print ("Checking ROM..")
time.sleep(1)
print ("Checking ROM...")
time.sleep(0.5)
print ("ROM Check Done!")
time.sleep(5)
os.system('clear')
print ("Checking RAM")
time.sleep(3)
print ("256MB Of RAM Detected!")
time.sleep(0.5)
print ("You May Have More Than 256MB But Thats The Max We Support")
time.sleep(3)
os.system('clear')
#ram check
number = random.randint(0,50)
print ("Checking RAM")
time.sleep(0.5)
print ("Using Pattern 0x1")
time.sleep(0.5)
print ("Running...")
time.sleep(10)
print (number, "Bad Sectors Detected!")
time.sleep(4)
print ("Repairing")
time.sleep(9)
os.system('clear')
print ("Looking For OS Image On Disk")
time.sleep(2)
print ("Looking For OS Image On Disk.")
time.sleep(1)
print ("Looking For OS Image On Disk..")
time.sleep(4)
print ("Looking For OS Image On Disk...")
time.sleep(0.5)
os.system ('clear')
print ("Found!... Booting!")
time.sleep(3)
#OS
os.system ('clear')
print ("Banana OS")
print ("System Specs:")
print ("256MB Of RAM")
print ("Banan i5 1900KS")
#OS Login
time.sleep(3)
os.system('clear')
user = input("Login:")
if user == 'sky':
	pas = input("Pass:")
if pas == 'kalli':
	#menu
	os.system ('clear')
	menu()
