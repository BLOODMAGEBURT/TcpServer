# -*- coding: utf-8 -*-
import socketserver

"""
-------------------------------------------------
   File Name：     TcpServer
   Description :
   Author :       Administrator
   date：          2019/6/26 0026
-------------------------------------------------
   Change Activity:
                   2019/6/26 0026:
-------------------------------------------------
"""


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()

        print("{} wrote:".format(self.client_address[0]))

        print(self.data)

        # just send back the same data, but upper-cased

        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "192.168.1.81", 9999
    # Create the server, binding to localhost on port 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you

    # interrupt the program with Ctrl-C

    server.serve_forever()