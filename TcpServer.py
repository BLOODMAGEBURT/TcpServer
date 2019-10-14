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
        val = 12345
        while True:  # while True, 一直保持在线
            try:

                self.data = self.request.recv(1024).strip()

                print("{} wrote:".format(self.client_address[0]))

                print(self.data)

                # just send back the same data, but upper-cased

                val -= 20
                msg = '{2_0= %d;11521;14322}' % val  # now on off
                # msg = '{ok}'  # now on off
                self.request.sendall(msg.encode('utf-8'))
            except ConnectionAbortedError:
                print("ConnectionAbortedError")
                break


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888
    # Create the server, binding to 0.0.0.0 on port 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you

    # interrupt the program with Ctrl-C

    server.serve_forever()
