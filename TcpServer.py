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
        while True:  # while True, 一直保持在线
            try:

                self.data = self.request.recv(1024).strip()

                print("{} wrote:".format(self.client_address[0]))

                print(self.data)

                # just send back the same data, but upper-cased

                msg = '{2_0=02345;01523;04321}'  # now on off
                self.request.sendall(msg.encode('utf-8'))
            except ConnectionAbortedError:
                print("ConnectionAbortedError")


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    # Create the server, binding to 0.0.0.0 on port 9999

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 使用多线程，可以同时处理多个tcp连接

    # Activate the server; this will keep running until you

    # interrupt the program with Ctrl-C

    server.serve_forever()
