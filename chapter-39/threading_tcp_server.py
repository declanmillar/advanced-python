import socket
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for the server.
    """

    def __init__(self, request, client_address, server):
        print("Setup names and offices")
        self.addresses = {"JOHN": "C45", "DENISE": "C44", "PHOEBE": "D52", "ADAM": "B23"}
        super().__init__(request, client_address, server)

    def handle(self):
        print("In Handle")
        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).decode()
        print("datareceived:", data)
        key = str(data).upper()
        response = self.addresses[key]
        print("response:", response)
        # Send the result back to the client
        self.request.sendall(response.encode())


def main():
    print("Starting")
    address = (socket.gethostname(), 8084)
    server = socketserver.ThreadingTCPServer(address, MyTCPHandler)
    print("Activating server")
    server.serve_forever()


if __name__ == "__main__":
    main()
