#!/usr/bin/python

import SocketServer

class MyTCPHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(4096).strip()
        print "get one"
        print self.data

if __name__ == "__main__":
    server = SocketServer.TCPServer(("127.0.0.1", 9000), MyTCPHandle)
    server.serve_forever()
