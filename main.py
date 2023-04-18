import sys
from minimal_subnet import MinimalSubnet

def main(fileName):
    obj = MinimalSubnet(fileName)
    obj.findMinimalSpanningSubnet()
    obj.printPrefixLength()
    # print(obj.maxPrefixLength)

if __name__ == "__main__":
    fileName = 'test.txt'
    if len(sys.argv)>1:
        fileName= sys.argv[1]
    main(fileName)

