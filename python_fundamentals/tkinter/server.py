import socket
import sys

from tkinter_gui import gui

import threading

RECV_SIZE = 1024

class server:
    def __init__(self):
        #Socket attributes:
        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.addr = None
        self.host = ''
        self.port = 0

        #Link to GUI:
        self.gui_link = None

        #Model State:
        self.is_connected = False
        self.waiting_for_socket_input = False
        self.waiting_for_socket_output = False
        self.socket_input = ''
        self.socket_output = ''

        #Bookeeping attributes:
        self.is_server = True

    def run_gui(self):
        '''gui: creates links between gui and server, and setups server endpoint of socket'''
        self.gui_link = gui("server")
        self.gui_link.link_to_client_server = self

        self.gui_link.root.mainloop()

    def setup_socket_connection(self):
        '''socket: sets up server socket endpoint, and upon connection waits to recv first input from server'''
        self.socket.bind((self.host, self.port))
        self.socket.listen(0)
        self.conn, self.addr = self.socket.accept()
        self.gui_link.update_button_text("calculate y^x")
        self.recvive() #needs to wait for server to recieve socket_input
        self.is_connected = True

    def recvive(self):
        '''socket: recv socket input (i.e. input for the server sent via the socket from the client)'''
        self.gui_link.update_label("Waiting for client to specify y")

        self.socket_input = self.conn.recv(RECV_SIZE).decode()

        if self.socket_input.strip().lower() != "done":
            self.gui_link.update_label("y={}, enter x:".format(self.socket_input))
            self.waiting_for_socket_input = False
            self.waiting_for_socket_output = True
        else:
            self.gui_link.close(False)

    def send(self):
        '''socket: send socket output (i.e. output from the server that will be sent via socket to the client)'''
        self.conn.sendall(self.socket_output.encode())
        
        self.waiting_for_socket_output = False
        self.waiting_for_socket_input = True

    def close(self,close_other_endpoint=True):
        '''socket: close socket endpoint'''
        if self.is_connected:
            if close_other_endpoint:
                self.conn.sendall("done".encode())
            self.conn.close()



if __name__ == '__main__':
    the_server = server()

    the_server.host = 'localhost'
    the_server.port = 50115

    the_server.run_gui()
    
