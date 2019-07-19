# -*- coding: utf-8 -*-
import socketserver

"""
-------------------------------------------------
   File Name：     ThreadingTcpServer
   Description :
   Author :       Administrator
   date：          2019/7/19 0019
-------------------------------------------------
   Change Activity:
                   2019/7/19 0019:
-------------------------------------------------
"""


class MyThreadingTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()

                print("{} wrote: {}".format(self.client_address[0], self.data))

                # just send back the same data, but upper-cased

                msg = '{2_0=02345;01523;04321}'  # now on off
                self.request.sendall(msg.encode('utf-8'))
            except ConnectionAbortedError:
                print("ConnectionAbortedError")
                break


if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 8888

    # 使用多线程，可以同时处理多个tcp连接
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyThreadingTcpHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
