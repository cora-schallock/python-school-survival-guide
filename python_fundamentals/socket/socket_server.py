import socket

HOST = 'localhost' # Standard loopback interface address (localhost)
PORT = 50000  # Port to listen on (non-privileged ports are > 1023)

RECV_SIZE = 1024 # read at most 1024 bytes

def square_input(user_input):
    return str(float(user_input)*float(user_input))


def run_server():
    print("Setting up server (HOST: {}, Port: {}".format(HOST,PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        
        while True:
            input_from_client = conn.recv(RECV_SIZE).decode() #use .decode() when recieving data
            print("Input: {}".format(input_from_client))
            if not input_from_client:
                break
            else:
                square_of_user_input = square_input(input_from_client)
                print("Answer: {}".format(square_of_user_input))
                conn.sendall(square_of_user_input.encode()) #use .encode() when sending data
        conn.close()
    

if __name__ == "__main__":
    run_server()
