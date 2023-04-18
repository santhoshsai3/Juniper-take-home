import unittest
from minimal_subnet import MinimalSubnet

class TestMinimalSubnet(unittest.TestCase):
    
    def test_openFile(self):
        # Test case where file exists
        ms = MinimalSubnet('test1.txt')
        self.assertEqual(ms.ip_addresses, ["172.16.10.1", "172.16.11.2", "172.16.12.3", "172.16.13.4"])

    def test_findMinimalSpanningSubnet(self):

        # Test case to check functionality
        ms = MinimalSubnet('test1.txt')
        ms.findMinimalSpanningSubnet()
        self.assertEqual(ms.maxPrefixLength, 21)

        # Test case where there are multiple IP addresses
        ms = MinimalSubnet('test.txt')
        ms.findMinimalSpanningSubnet()
        self.assertEqual(ms.minSpanSubnet, '192.168.1.0/29')

    def test_edge_case(self):

        # Test case where there is only one IP address
        ms = MinimalSubnet('test3.txt')
        ms.findMinimalSpanningSubnet()
        self.assertEqual(ms.maxPrefixLength, 32)




if __name__ == '__main__':
    unittest.main()
