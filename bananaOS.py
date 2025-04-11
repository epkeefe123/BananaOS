import time
import os
import sys
import random
import socket

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

def dialup():
    print("Connecting to dialup server...")
    time.sleep(2)
    
    try:
        server_ip = input("Enter server IP (e.g., 127.0.0.1): ").strip()
        port = 2525
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)
            s.connect((server_ip, port))
            print("Connection established!")
            time.sleep(1)

            print("Handshaking...")
            time.sleep(10)
            s.sendall(b"HELLO FROM BANANA OS\r\n")
            recv = s.recv(1024).decode(errors='ignore')
            print("Server:", recv.strip())

            print("\nWelcome to BananaBBS!")
            print("=======================")
            print("1. Read Messages")
            print("2. Post Message")
            print("3. Disconnect")

            while True:
                choice = input("Select an option (1-3): ").strip()
                if choice == '1':
                    s.sendall(b"READ\r\n")
                    response = s.recv(2048).decode(errors='ignore')
                    print("\n--- Messages ---")
                    print(response.strip())
                    print("----------------")
                elif choice == '2':
                    msg = input("Enter your message: ").strip()
                    s.sendall(f"POST {msg}\r\n".encode())
                    ack = s.recv(1024).decode(errors='ignore')
                    print("Server:", ack.strip())
                elif choice == '3':
                    s.sendall(b"BYE\r\n")
                    print("Disconnected from server.")
                    break
                else:
                    print("Invalid option.")

    except Exception as e:
        print(f"Connection failed: {e}")

def diskpart():
    print("Linux DiskPart")
    time.sleep(0.5)
    print("Disk Info")
    time.sleep(1)
    print("Run Hours:", state['Hours'])
    time.sleep(0.5)
    print("Storage Used:", state['storeusd'])
    time.sleep(0.5)
    print("Bad Sectors:", state['bsec'])
    time.sleep(0.5)
    print("Manufacturer:", state['man'])
    time.sleep(0.5)
    print("Interface:", state['inter'])
    time.sleep(2)
    print("Disk info fetched!")
    print("Select info to edit:")
    time.sleep(2)
    print("1. Reset disk hours")
    time.sleep(0.5)
    print("2. Change manufacturer")
    time.sleep(0.5)
    print("3. Change interface")
    time.sleep(0.5)
    manchoice = input("?: ").strip()

    if manchoice == '1':
        state['Hours'] = '0'
        print("Disk hours reset to 0.")
    elif manchoice == '2':
        print("Options:")
        time.sleep(1)
        print("1. WD")
        time.sleep(0.5)
        print("2. WD Green")
        time.sleep(0.5)
        print("3. Barracuda")
        time.sleep(0.5)
        print("4. IBM")
        time.sleep(2)
        man = input("Select manufacturer: ").strip()
        brands = {'1': 'WD', '2': 'WD Green', '3': 'Barracuda', '4': 'IBM'}
        if man in brands:
            state['man'] = brands[man]
            time.sleep(0.5)
            print("Manufacturer updated.")
        else:
            print("Invalid selection.")
    elif manchoice == '3':
        interfaceconfig()
    else:
        print("Invalid selection.")

def interfaceconfig():
    print("Detecting Storage Interface Type")
    time.sleep(2)
    print("Unable to Detect")
    time.sleep(0.5)
    print("Please Select From A List:")
    time.sleep(1)
    print("1.NVME")
    time.sleep(0.5)
    print("2.SATA")
    time.sleep(0.5)
    print("3.IDE")
    time.sleep(0.5)
    print("4.30 Pin SCA")
    time.sleep(0.5)
    print("5.20 Pin SCA")
    time.sleep(3)
    stor = input("?:").strip()

    interfaces = {
        '1': 'NVME',
        '2': 'SATA',
        '3': 'IDE',
        '4': '30 Pin SCA',
        '5': '20 Pin SCA'
    }

    if stor in interfaces:
        state['inter'] = interfaces[stor]
        print("Set! Disk Info Updated!")
    else:
        print("Invalid selection.")

def format_disk():
    print("ALL DATA WILL BE DESTROYED")
    time.sleep(2)
    print("Mounting Disk")
    time.sleep(2)
    print("Formatting")
    for _ in range(3):
        print("Formatting" + "." * (_ + 1))
        time.sleep(5)
    state['storeusd'] = '0.5GB'
    state['bsec'] = '0'
    state['inter'] = 'Requires setup'
    print("Done!... Reinstalling Banana OS From Cache")
    time.sleep(32)
    print("Done!")
    time.sleep(21)
    print("Please Run storeconfig to setup the storage interface!")

def netconfig():
    e = input("Is the network card installed? (Y/N):").strip().lower()
    if e != 'y':
        print("No network card detected. Exiting netconfig.")
        return

    print("Testing Connection To DHCP and DNS")
    for dots in range(4):
        print("Pinging 192.168.1.1" + "." * dots)
        time.sleep(2)
    print("Collecting Info...")
    time.sleep(3)
    print("Connection to DHCP Succeeded!")
    time.sleep(3)
    clear_screen()
    print("Testing DNS")
    time.sleep(3)
    print("Pinging 8.8.8.8")
    time.sleep(2)
    print("Reply From 8.8.8.8 With 32 Packet Bits")
    time.sleep(4)
    print("Collecting Info...")
    time.sleep(5)
    clear_screen()
    print("Network Connected! DNS and DHCP are working!")

def boot_sequence():
    clear_screen()
    print("Banana BIOS")
    for dots in range(4):
        print("Checking ROM" + "." * dots)
        time.sleep(2)
    print("ROM Check Done!")
    time.sleep(2)
    clear_screen()
    print("Checking RAM")
    time.sleep(2)
    print("256MB Of RAM Detected!")
    time.sleep(1)
    print("You May Have More Than 256MB But Thats The Max We Support")
    time.sleep(5)
    clear_screen()

    print("Checking RAM")
    print("Using Pattern 0x1")
    time.sleep(4)
    print("Running...")
    time.sleep(3)
    number = random.randint(0, 50)
    print(f"{number} Bad Sectors Detected!")
    time.sleep(2)
    print("Repairing")
    time.sleep(5)
    clear_screen()

    print("Looking For OS Image On Disk")
    for dots in range(4):
        print("Looking For OS Image On Disk" + "." * dots)
        time.sleep(2)
    clear_screen()
    print("Found!... Booting!")
    time.sleep(5)
    clear_screen()

    print("Banana OS")
    print("System Specs:")
    print("256MB Of RAM")
    print("Banan i5 1900KS")
    time.sleep(2)
    clear_screen()

def login():
    while True:
        user = input("Login:").strip()
        if user == 'sky':
            pas = input("Pass:").strip()
            if pas == 'kalli':
                clear_screen()
                return True
            else:
                print("Wrong password.")
        else:
            print("Unknown user.")

def menu():
    while True:
        cmd = input("sky@localdisk $").strip().lower()

        if cmd == 'shutdown':
            sys.exit()
        elif cmd == 'ls':
            print(dirtop)
            print(dirbot)
            time.sleep(1)
            print("Done!")
        elif cmd == 'clear':
            clear_screen()
        elif cmd == 'disk':
            print("Finding Disk Info")
            time.sleep(1)
            print("Disk Info:")
            time.sleep(0.5)
            if state['inter'] == 'Requires setup':
                print("Unable to read disk")
                print("If you just formatted, run storeconfig to setup the storage interface")
            else:
                print("Storage Used:", state['storeusd'])
                time.sleep(0.5)
                print("Run Hours:", state['Hours'])
                time.sleep(0.5)
                print("Bad Sectors:", state['bsec'])
                time.sleep(0.5)
                print("Manufacturer:", state['man'])
                time.sleep(4)
                print("Interface:", state['inter'])
                time.sleep(2)
                print("Done!")
        elif cmd == 'format':
            dec = input("Proceed With Format? (Y/N):").strip().lower()
            if dec == 'y':
                format_disk()
        elif cmd == 'netconfig':
            netconfig()
        elif cmd == 'storeconfig':
            interfaceconfig()
        elif cmd == 'diskpart':
            diskpart()
        elif cmd == 'dialup':
            dialup()
        else:
            print("Invalid Syntax. Check CMD.")

# Boot and Run
boot_sequence()
if login():
    menu()
