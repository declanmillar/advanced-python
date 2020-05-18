import socket
import socketserver

import datetime


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for the server.
    """

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).decode()

        # print("datareceived:", data)
        if data == "Date":
            response = datetime.datetime.now().strftime("%d/%m/%Y")
        elif data == "Time":
            response = datetime.datetime.now().strftime("%H:%M:%S")
        elif data == "DateAndTime":
            response = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
        else:
            response = f"UNKNOWN RESPONSE {data}"

        # print("response:", response)
        # Send the result back to the client
        self.request.sendall(response.encode())


def main():
    print("Starting")
    address = (socket.gethostname(), 8084)
    server = socketserver.ThreadingTCPServer(address, MyTCPHandler)
    print("Activating server")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.shutdown()
    server.server_close()


if __name__ == "__main__":
    main()