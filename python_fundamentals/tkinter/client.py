import socket
import sys

from tkinter_gui import gui

import threading

RECV_SIZE = 1024

class client:
    def __init__(self):
        #Socket attributes:
        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        self.is_server = False

    def run_gui(self):
        '''gui: creates links between gui and client, and setups client endpoint of socket'''
        self.gui_link = gui("client")
        self.gui_link.link_to_client_server = self

        self.gui_link.root.mainloop()

    def setup_socket_connection(self):
        '''socket: sets up client socket endpoint'''
        self.socket.connect((self.host, self.port))
        self.gui_link.update_button_text("send")
        self.gui_link.update_label("Enter y:")
        self.waiting_for_socket_output = True
        self.is_connected = True

    def recvive(self):
        '''socket: recv socket input (i.e. input for the client sent via the socket from the server)'''
        self.gui_link.update_label("Waiting for server to calculate {}^x".format(self.socket_output))
        
        self.socket_input = self.socket.recv(RECV_SIZE).decode()

        if self.socket_input.strip().lower() != "done":
            self.gui_link.update_label("{}^x={}".format(self.socket_output,self.socket_input))
            self.waiting_for_socket_input = False
            self.waiting_for_socket_output = True
        else:
            self.gui_link.close(False)

    def send(self):
        '''socket: send socket output (i.e. output from the client that will be sent via socket to the server)'''
        self.socket.sendall(self.socket_output.encode())
        self.waiting_for_socket_input = True
        self.waiting_for_socket_output = False

    def close(self,close_other_endpoint=True):
        '''socket: close socket endpoint'''
        if self.is_connected:
            if close_other_endpoint:
                self.socket.sendall("done".encode())
            self.socket.close()


        


if __name__ == '__main__':
    the_client = client()

    the_client.host = 'localhost'
    the_client.port = 50115

    the_client.run_gui()

