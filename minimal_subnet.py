import ipaddress
import os
import sys

class MinimalSubnet:

    def __init__(self, fileName):
        self.fileName = fileName
        self.ip_addresses = []
        self.minSpanSubnet = ''
        self.max_ip = ipaddress.IPv4Address('0.0.0.0')
        self.min_ip = ipaddress.IPv4Address('255.255.255.255')
        self.maxPrefixLength = 0
        self.openFile()
        
    # Opens the file and reads the contents of the file
    def openFile(self):
        if not os.path.exists(self.fileName):
            print("file not exits")
            sys.exit()
        # Assuming all the ips are present in the first line of the text file
        with open(self.fileName, 'r') as f:
            first_line = f.readline()
        if first_line:
             self.ip_addresses = first_line.split(',')

    def printPrefixLength(self):
        print(self.maxPrefixLength)
    
    def findMinimalSpanningSubnet(self):
        #If length of array is 0, return null
        if len(self.ip_addresses)==0:
            print("please check the input")
            exit(0)     

        #Finding the max and min ip address, so that max prefix can be found using them.       
        for ip in self.ip_addresses:
            ip_bin = ipaddress.IPv4Address(ip.strip())
            self.max_ip = max(self.max_ip,ip_bin)
            self.min_ip = min(self.min_ip,ip_bin)
        if self.max_ip == self.min_ip:
            #this condition is true when there is only one ip address, so maxprefix len is 32
            self.maxPrefixLength = 32
            self.minSpanSubnet = (str(self.max_ip)+'/'+"32")
        else:
            #if there are 2 or more subnets
            #Converting the ip addresses to binary to find the common prefix
            max_ip_binary = bin(int(self.max_ip))[2:].zfill(32)
            min_ip_bin = bin(int(self.min_ip))[2:].zfill(32)
            l = []
            for i in range(32):
                if max_ip_binary[i]!=min_ip_bin[i]:
                    self.maxPrefixLength = i
                    break
            for i in range(self.maxPrefixLength):
                l.append(min_ip_bin[i])

            for i in range(self.maxPrefixLength,32):
                l.append('0')
            res = ''.join(l)
            decimal_address = int(res, 2)  # Convert binary to decimal
            ip_address = ipaddress.IPv4Address(decimal_address)  # Convert decimal to IP address
            self.minSpanSubnet = str(ip_address)+"/"+str(self.maxPrefixLength)

