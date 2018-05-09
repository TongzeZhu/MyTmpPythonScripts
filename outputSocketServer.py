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
            self.request.sendall('one night, and no more!'.encode())
            print('no more play')
        else:
            g_peers.append(self.client_address[0])
            global g_datafile
            for line in fileinput.input(g_datafile):
                linelen = len(line)
                if linelen == 0:
                    continue
                data = bytearray(2)
                data[0] = int(linelen / 256)
                data[1] = linelen % 256
                self.request.sendall(data)
                self.request.sendall(line.encode())
            
        

if __name__ == "__main__":
    server = socketserver.TCPServer(("192.168.101.184", 9002), MyTCPHandle)
    server.serve_forever()
