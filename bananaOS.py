import time
import os
import sys
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# System State
state = {
    'Hours': '503',
    'storeusd': '1GB',
    'bsec': '2',
    'man': 'WD',
    'inter': 'IDE'
}

dirtop = "  Dir       File      Dir      BootFile"
dirbot = "Banana     Readme     sys      boot.sys"

def interfaceconfig():
    print("Detecting Storage Interface Type")
    time.sleep(5)
    print("Unable to Detect")
    time.sleep(0.5)
    print("Please Select From A List:")
    time.sleep(3)
    print("1.NVME")
    time.sleep(0.5)
    print("2.SATA")
    time.sleep(0.5)
    print("3.IDE")
    time.sleep(0.5)
    print("4.30 Pin SCA")
    time.sleep(0.5)
    print("5.20 Pin SCA")
    stor = input("?:").strip()

    if stor == '1':
        state['inter'] = 'NVME'
    elif stor == '2':
        state['inter'] = 'SATA'
    elif stor == '3':
        state['inter'] = 'IDE'
    elif stor == '4':
        state['inter'] = '30 Pin SCA'
    elif stor == '5':
        state['inter'] = '20 Pin SCA'

    print("Set! Disk Info Updated!")
    menu()

def format_disk():
    print("ALL DATA WILL BE DESTROYED")
    time.sleep(5)
    print("Mounting Disk")
    time.sleep(3.2)
    print("Formatting")
    time.sleep(3)
    print("Formatting.")
    time.sleep(2)
    print("Formatting..")
    time.sleep(0.5)
    print("Formatting...")
    state['storeusd'] = '0.5GB'
    state['bsec'] = '0'
    state['inter'] = 'Requires setup'
    print("Done!... Reinstalling Banana OS From Cache")
    time.sleep(10)
    print("Done!")
    time.sleep(2)
    clear_screen()
    menu()

def netconfig():
    print("Is the network card installed?")
    e = input("Y/N:").strip().lower()
    print("Testing Connection To DHCP and DNS")
    time.sleep(2)
    print("Pinging 192.168.1.1")
    time.sleep(2)
    print("Pinging 192.168.1.1.")
    time.sleep(2)
    print("Pinging 192.168.1.1..")
    time.sleep(2)
    print("Pinging 192.168.1.1...")
    time.sleep(4)
    print("Collecting Info...")
    time.sleep(5)
    print("Connection to DHCP Succeeded!")
    time.sleep(8)
    clear_screen()
    print("Testing DNS")
    time.sleep(3)
    print("Pinging 8.8.8.8")
    time.sleep(1)
    print("Reply From 8.8.8.8 With 32 Packet Bits")
    time.sleep(3)
    print("Collecting Info...")
    time.sleep(5)
    clear_screen()
    print("Network Connected! DNS and DHCP are working!")
    time.sleep(5)
    menu()

def menu():
    cmd = input("sky@localdisk $").strip().lower()

    if cmd == 'shutdown':
        sys.exit()
    elif cmd == 'ls':
        print(dirtop)
        print(dirbot)
        time.sleep(1)
        print("Done!")
        menu()
    elif cmd == 'clear':
        clear_screen()
        menu()
    elif cmd == 'disk':
        print("Finding Disk Info")
        time.sleep(3)
        print("Disk Info:")
        time.sleep(0.5)
        print("Storage Used:", state['storeusd'])
        time.sleep(0.5)
        print("Run Hours:", state['Hours'])
        time.sleep(0.5)
        print("Bad Sectors:", state['bsec'])
        time.sleep(0.7)
        print("Manufacturer:", state['man'])
        time.sleep(2)
        print("Interface:", state['inter'])
        time.sleep(3)
        print("Done!")
        time.sleep(2)
        menu()
    elif cmd == 'format':
        print("Proceed With Format?")
        dec = input("Y/N:").strip().lower()
        if dec == 'y':
            format_disk()
        else:
            menu()
    elif cmd == 'netconfig':
        netconfig()
    elif cmd == 'storeconfig':
        interfaceconfig()
    else:
        print("Invalid Syntax Check CMD")
        menu()

# Boot Sequence
clear_screen()
print("Banana BIOS")
time.sleep(0.5)
print("Checking ROM")
time.sleep(1)
print("Checking ROM.")
time.sleep(1)
print("Checking ROM..")
time.sleep(1)
print("Checking ROM...")
time.sleep(0.5)
print("ROM Check Done!")
time.sleep(5)
clear_screen()
print("Checking RAM")
time.sleep(3)
print("256MB Of RAM Detected!")
time.sleep(0.5)
print("You May Have More Than 256MB But Thats The Max We Support")
time.sleep(3)
clear_screen()

number = random.randint(0, 50)
print("Checking RAM")
time.sleep(0.5)
print("Using Pattern 0x1")
time.sleep(0.5)
print("Running...")
time.sleep(10)
print(f"{number} Bad Sectors Detected!")
time.sleep(4)
print("Repairing")
time.sleep(9)
clear_screen()
print("Looking For OS Image On Disk")
time.sleep(2)
print("Looking For OS Image On Disk.")
time.sleep(1)
print("Looking For OS Image On Disk..")
time.sleep(4)
print("Looking For OS Image On Disk...")
time.sleep(0.5)
clear_screen()
print("Found!... Booting!")
time.sleep(3)
clear_screen()

print("Banana OS")
print("System Specs:")
print("256MB Of RAM")
print("Banan i5 1900KS")
time.sleep(3)
clear_screen()

user = input("Login:").strip()
if user == 'sky':
    pas = input("Pass:").strip()
    if pas == 'kalli':
        clear_screen()
        menu()
