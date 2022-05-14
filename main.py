import socket
import sys
import os



def get_banner(ip,port):
    try:
        socket.setdefaulttimeout(5)
        s= socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024).decode()
        return banner
    except:
        return
def checkvul(banner1, filename1):
    f=open(filename1,"r")
    for line in f.readline():
        if line in banner1:
            print("server is vulnerable ",banner1)


def main():
    if len(sys.argv)==2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("File not found")
            exit(0)
        elif not os.access(filename,os.R_OK):
            print("Access denied")
            exit(0)
    else:
        print("usage "+sys.argv[0]+" <valnerability filename>")
        exit(0)
    ip = input("Enter the ip to scan= ")
    ports=[22]
    for p in ports:
        banner = get_banner(ip,p)
        if banner:
            checkvul(banner, filename)



main()
