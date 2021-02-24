# -*- coding: utf-8 -*-
"""
task3.simple_web_browser
15-538-085
Janick Spirig
"""


from socket import gethostbyname, socket, timeout, AF_INET, SOCK_STREAM
from sys import argv

HTTP_HEADER_DELIMITER = b'\r\n\r\n'
CONTENT_LENGTH_FIELD = b'Content-Length:'
HTTP_PORT = 80
ONE_BYTE_LENGTH = 1

def create_http_request(host, path, method='GET'):
    '''
    Create a sequence of bytes representing an HTTP/1.1 request of the given method.

    :param host: the string contains the hostname of the remote server
    :param path: the string contains the path to the document to retrieve
    :return: a bytes object contains the HTTP request to send to the remote server

    e.g.,) An HTTP Get request to http://compass.unisg.ch/
    host: compass.unisg.ch
    path: /
    return: b'GET compass.unisg.ch HTTP/1.1\nhost: compass.unisg.ch\r\n\r\n'
    '''
    ###   Task 3(a)   ###

    # Hint: use str.encode() to create an encoded version of the string as a bytes object
    # https://docs.python.org/3/library/stdtypes.html#str.encode
    # ADD YOUR CODE HERE
    
    # decode header delimiter as it is bytes (b')
    header_delimiter = HTTP_HEADER_DELIMITER.decode()
    
    # create request string for http get request
    request_string = "{} {} HTTP/1.1\nHost: {}{}".format(method, path, host, header_delimiter)
    
    # return request string as bytes
    return request_string.encode()

    ### Task 3(a) END ###
    
def receive_http_response_header(sock):
    '''
    Receive the HTTP response header from the TCP socket.

    :param sock: the TCP socket connected to the remote server
    :return: a bytes object that is the HTTP response header received
    '''
    ###   Task 3(b)   ###

    # Hint 1: use HTTP_HEADER_DELIMITER to determine the end of the HTTP header
    # Hint 2: use sock.recv(ONE_BYTE_LENGTH) to receive the chunk byte-by-byte
    # ADD YOUR CODE HERE
    
    # create empty header variable
    header_bytes = bytes()
    
    # loop through each character of header
    # we start at byte character one and add every character to the header_bytes variable until we included all characters of the header delimiter
    while True:
        # add byte character to the header
        header_bytes += sock.recv(ONE_BYTE_LENGTH)
        
        # check if already arrived at the end of the header
        if header_bytes[-4:] == HTTP_HEADER_DELIMITER:
            break;
    
    # return header
    return header_bytes

    ### Task 3(b) END ###


def get_content_length(header):
    '''
    Get the integer value from the Content-Length HTTP header field if it
    is found in the given sequence of bytes. Otherwise returns 0.

    :param header: the bytes object contains the HTTP header
    :return: an integer value of the Content-Length, 0 if not found
    '''
    ###   Task 3(c)   ###

    # Hint: use CONTENT_LENGTH_FIELD to find the value
    # ADD YOUR CODE HERE
    
    # check if header contains Content-Length field
    if CONTENT_LENGTH_FIELD in header:
        
        '''
        Example Response-Header:
        b'HTTP/1.1 200 OK\r\nAccept-Ranges: bytes\r\nAge: 71015\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\n
        Date: Fri, 27 Mar 2020 07:48:25 GMT\r\nEtag: "3147526947"\r\nExpires: Fri, 03 Apr 2020 07:48:25 GMT\r\n
        Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT\r\nServer: ECS (bsa/EB1E)\r\nVary: Accept-Encoding\r\nX-Cache: HIT\r\nContent-Length: 1256\r\n\r\n'
        '''
        
        # decode the header from bytes to string
        header_string = header.decode()
        
        # get all the values after the text "Content-Length: "
        from_contentlength = header_string.split(CONTENT_LENGTH_FIELD.decode() + " ")[1]
        
        # cut out the field end "\r\n" and get the number before the field end
        # as we do not want to depend on Conten-Length field is always at the end of the header we do not split at "\r\n\r\n", but at "\r\n"
        # after the split get the first element in the list which is the content-length value as string
        without_end = from_contentlength.split(HTTP_HEADER_DELIMITER.decode()[:2])[0]
        
        # transform conent-length value to integer
        content_length = int(without_end)
        
        # return value
        return content_length
    
    # no content-length field present in header
    else:
        return 0

    ### Task 3(c) END ###


def receive_body(sock, content_length):
    '''
    Receive the body content in the HTTP response

    :param sock: the TCP socket connected to the remote server
    :param content_length: the size of the content to recieve
    :return: a bytes object contains the remaining content (body) in the HTTP response
    '''
    ###   Task 3(d)   ###

    # ADD YOUR CODE HERE
    
    # receive body of content_length and return it
    # https://docs.python.org/2/library/socket.html#socket.socket.recv
    return sock.recv(content_length)

    ### Task 3(d) END ###


def main():
    # Change the host and path below to test other web sites!
    host = 'example.com'
    path = '/index.html'
    print('# Retrieve data from http://{}'.format(host+path))

    # Get the IP address of the host
    ip_address = gethostbyname(host)
    print('> Remote server {} resolved as {}'.format(host, ip_address))

    # Establish the TCP connection to the host
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip_address, HTTP_PORT))
    print('> TCP Connection to {}:{} established'.format(ip_address, HTTP_PORT))

    # Uncomment this comment block after Task 3(a)
    # Send an HTTP GET request
    http_get_request = create_http_request(host, path)
    print('\n# HTTP GET request ({} bytes)'.format(len(http_get_request)))
    print(http_get_request)
    sock.sendall(http_get_request)
    # Comment block for Task 3(a) END

    # Uncomment this comment block after Task 3(b)
    # Receive the HTTP response header
    header = receive_http_response_header(sock)
    print(type(header))
    print('\n# HTTP Response Header ({} bytes)'.format(len(header)))
    print(header)
    # Comment block for Task 3(b) END

    #Uncomment this comment block after Task 3(c)
    content_length = get_content_length(header)
    print('\n# Content-Length')
    print('{} bytes'.format(content_length))
    # Comment block for Task 3(c) END

    # Uncomment this comment block after Task 3(d)
    body = receive_body(sock, content_length)
    print('\n# Body ({} bytes)'.format(len(body)))
    print(body)
    # Comment block for Task 3(d) END

if __name__ == '__main__':
    main()
