#!/usr/bin/env python3
# -*- encoding utf8 -*-

import socketserver
import fileinput

g_peers = []
g_datafile = '/home/tongze/testspace/plcdata.txt'

class MyTCPHandle(socketserver.BaseRequestHandler):
    def handle(self):
        global g_peers
        if self.client_address[0] in g_peers:
            data = self.request.recv(4096).strip()
            print(data.decode())
        else:
            g_peers.append(self.client_address[0])
            data = self.request.recv(4096).strip()
            print(data.decode())
        

if __name__ == "__main__":
    server = socketserver.TCPServer(("192.168.101.184", 9000), MyTCPHandle)
    server.serve_forever()
