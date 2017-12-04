#AUTHOR:ru2600
#PROGRAM:httpybanner.py
#DESCRIPTION:Banner grabber for python, grabs banners and tells possible server used plus send malformed requests

import requests     #Used to create connection with server
import errno        #Get errors
import os           #This is so netcat can be used to send malformed data

def start():
    print
    print "Choose your scan below: "
    choose = input("1: fingerprint, 2: server scan, 3: malformed request, or type 0 to quit: ")
    if choose == 1:
        fingerprint()
    if choose == 2:
        serverScan()
    if choose == 3:
        malformedRequest()
    if choose == 0:
        quit()
    else:
        print "Invalid request!"

def fingerprint():
    server = raw_input("Enter the server you wish to scan: ")
    r = requests.get("http://" + server)
    print (r.headers)
    return start()

def serverScan():
    server = raw_input("Enter the server you wish to scan: ")
    r = requests.get("http://" + server)
    print (r.headers['Server'])
    return start()

def malformedRequest():
    print "NOTE: For malformed request, put your own data in after you put in the server address"
    server = raw_input("Enter ther server you wish to scan: ")
    os.system("nc " + server + " 80")
    return start()

print "Welcome to httpybanner!"
start()
