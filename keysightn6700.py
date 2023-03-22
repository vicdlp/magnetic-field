# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:04:42 2022

@author: adm.quantumlab
"""

import socket
import sys

def openSocket(IPaddr, port): # Create a connection via sockets
    global skt
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.settimeout(8) # 8 second timeout
    except socket.error as e:
        print('Error creating socket: %s' % e)
        sys.exit(1)
    try:
        skt.connect((IPaddr, port))
    except socket.gaierror as e:
        print('Address-related error connecting to instrument: %s' % e)
        sys.exit(1)
    except socket.error as e:
         print('Error connecting to socket on instrument: %s' % e)
         sys.exit(1) 
         
def outPut(cmd1): # Send SCPI command via sockets
    cmd1 = cmd1 + '\n'
    skt.send(cmd1.encode('ASCII'))
    
def enTer(): # Receive instrument data via sockets
    dataStr=skt.recv(1024).decode('ASCII')
    return dataStr.strip()

def errStr(): # Check for instrument errors
    num=1
    while int(num) != int(0):
        outPut('SYST:ERR?')
        respnse = enTer() # errors include a number and a string
        num, str_resp = respnse.split(',')
        print(num,str_resp)

def closeSockets(): # Close socket connection
    skt.close()
    

    
