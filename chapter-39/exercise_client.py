import socket


def main():
    print("Starting Client")
    server_address = (socket.gethostname(), 8084)

    while True:
        print("Please provide an input (Date, Time, DataAndTime or -1 to exit):")
        message = input()

        if message == "-1":
            break
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(server_address)
            print("Connected to server")
            print("Sending data")
            sock.send(message.encode())
            data = sock.recv(1024).decode()
            print("Received from server: ", data)
            print("Closing socket")
            sock.close()

if __name__ == "__main__":
    main()
