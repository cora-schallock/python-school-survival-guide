import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 50000  # Port to listen on (non-privileged ports are > 1023)

RECV_SIZE = 1024 # read at most 1024 bytes

def get_user_input():
    user_input = input("Please enter a integer to square (or type 'DONE' to exit):")

    if user_input.isnumeric() or user_input == "DONE":
        return user_input
    else:
        raise ValueError
        

def run_client():
    print("Establishing Connection to server (HOST: {}, Port: {}".format(HOST,PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        try:
            user_input = get_user_input()
            if user_input == "DONE":
                break
        except:
            print("Error: Please enter a valid integer (or type 'DONE' to exit)")
            continue

        s.sendall(user_input.encode()) #use .encode() when sending data
        result_from_server = s.recv(RECV_SIZE).decode() #use .decode() when recieving data
        print("{}^2={}".format(user_input,result_from_server))
    s.close()

if __name__ == "__main__":
    run_client()
