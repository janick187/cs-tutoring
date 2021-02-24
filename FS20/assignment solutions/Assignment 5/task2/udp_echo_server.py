# -*- coding: utf-8 -*-
"""
task2.udp_echo_server
15-538-085
Janick Spirig
"""

from socket import socket, timeout, AF_INET, SOCK_DGRAM

SERVER_IP = "127.0.0.1" # IP address of the server
SERVER_PORT = 22222     # UDP Port of the server
BUF_SIZE = 1024         # Maximum receiving data buffer size in bytes

class UDPEchoServer:
    """
    An echo sever with UDP transport.
    """

    def __init__(self, ip_address, udp_port):
        """
        :param ip_address: the IP address to listen
        :param udp_port: the port to listen for the udp connection
        """
        
        # assign address and port to UDP server, these values are passed to the consturctor in the main method
        self.ip_address = ip_address
        self.udp_port = udp_port

        # Create a UDP socket at client side
        # AF_INET: IPv4
        # SOCK_DGRAM: UDP
        
        self._sock = socket(family=AF_INET, type=SOCK_DGRAM)

    def start(self):
        """
        Start the UDP Echo Server.

        This class instance method first binds the socket to the IP address and the port.
        Then in an infinite loop:
            1. Receive the data from clients
            2. Decode the received bytes object to a string message
            3. Print the message
            4. Make all the characters in the message to uppercase
            5. Encode the message to a bytes object
            6. Echo back the message to the client
            7. When the message from the client is 'bye', this echo server should exit the loop after sending back the last message (i.e., 'BYE') to the client.
        """
        print("\n --------------- UDP Echo Server ---------------\n")
        ###   Task 2(b)   ###

        # HINT 1: use self._sock.bind() to bind the IP address and the port.
        # Note that the address parameter of bind() is a tuple of an IP address (string) and Port (integer) for AF_INET address family.
        # https://docs.python.org/3/library/socket.html#socket.socket.bind
        #
        # HINT 2: use bytes.decode() to decode the data.
        # https://docs.python.org/3/library/stdtypes.html#bytes.decode
        # Don't forget to encode the data before sending it to the client!
        
        
        # How to program udp sockets -> https://www.binarytides.com/programming-udp-sockets-in-python/
        # How to receive incoming data -> https://pythontic.com/modules/socket/recvfrom
        
        # bind socket to local host and port, the bind method requires a tuple, thats why a tuple first is created (inner brackets)
        # and then passed to the method as parameter
        self._sock.bind((self.ip_address, self.udp_port))
        
        while True:
            '''
            receive message with max BUF_SIZE, method returns a tuple containing the bytes object as as the first element
            and the information of the address from which the message was sent as the second element
            e.g. (message(ip:port, client_id))
            '''
            
            # receive data as bytes
            data = self._sock.recvfrom(BUF_SIZE)
            
            # decode the byte object to a string so that we can actually process the message
            message = data[0].decode()
            
            # save the tuple with sender information in a local variable
            client = data[1]
            
            # print all information
            print("Message received from ({}, {}): {}".format(client[0], str(client[1]), message))
            
            # make whole string upper
            upper_string = message.upper()
            
            # send back upper string
            self._sock.sendto(upper_string.encode(), client)
            
            # exit loop if client sends bye, break; possible as well
            if upper_string == "BYE":
                exit();
                # break;

        ### Task 2(b) END ###
            
        '''
        Frame Length:
            The headers combined of IP and UDP equal always to 32 bytes (for IPv4 in combination with UDP)
            Every character of the payload (text sent to server or received from server) equals to 1 byte (depends on the encoding)
            Hence, the size of the frame transferred always equals to 32 bytes + (number of characters * 1 byte)
        
            See also: https://stackoverflow.com/questions/4850241/how-many-bits-or-bytes-are-there-in-a-character
        '''

if __name__ == '__main__':
    server = UDPEchoServer(SERVER_IP, SERVER_PORT)
    server.start()
