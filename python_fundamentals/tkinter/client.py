import os
import socket
import threading

from gui import gui

HOST = 'localhost'
PORT = 50115
RECV_SIZE = 1024

class client_socket:
    def __init__(self,host,port):
        #Link to Client:
        self.link_to_client = None

        #Socket Attributes:
        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

        #Book keeping Attributes:
        self.is_connected = False
        self.did_close = False
        self.socket_input = ''
        self.socket_output = ''

    def run(self):
        '''run socket thread'''
        self.setup()
        self.recieve_loop()

    def setup(self):
        '''setups up connection (via connect)'''
        self.socket.connect((self.host, self.port))
        
        self.is_connected = True
        self.link_to_client.handle_connected()

    def recieve_loop(self):
        '''primary socket thread loop'''
        while self.is_connected:
            if self.did_close:
                break
            elif self.socket_input.strip().lower() == "done":
                break
            else:
                try:
                    self.socket_input = self.socket.recv(RECV_SIZE).decode()
                    self.link_to_client.handle_recv_data()
                except:
                    self.link_to_client.close()

    def send(self):
        '''send via socket'''
        self.socket.sendall(self.socket_output.encode())

    def close(self,close_other_endpoint=True):
        '''socket: close socket endpoint'''
        if self.is_connected:
            self.did_close = True
            if close_other_endpoint:
                self.socket.sendall("done".encode())
            self.socket.close()
            self.is_connected = False

class client:
    def __init__(self):
        #The created socket thread:
        self.socket_thread = None

        #Links to socket and gui code
        self.socket_link = None
        self.gui_link = None

        #Book keeping attributes:
        self.waiting_for_server = False

        #Start by Running the GUI:
        self.run_gui()

    def run_gui(self):
        '''run gui (on main thread)'''
        self.gui_link  = gui("client")
        self.gui_link.link_to_client_server = self
        self.gui_link.running = True
        self.gui_link.root.mainloop()
        
    def run_socket(self):
        '''run socket thread'''
        self.socket_link = client_socket(HOST,PORT)
        self.socket_link.link_to_client = self
        self.socket_thread = threading.Thread(target=self.socket_link.run)
        #self.socket_thread.setDaemon(True)
        self.socket_thread.daemon = True
        self.socket_thread.start()

    def handle_connected(self):
        '''after connection is made, update gui label and button'''
        self.gui_link.label_string = "enter y:"
        self.gui_link.button_string = "send"
        self.gui_link.update()

    def handle_click(self):
        '''handles click of gui button'''
        if self.socket_link == None:
            self.run_socket()
        elif self.waiting_for_server:
            self.gui_link.label_string = 'Waiting for Server'
            self.gui_link.update()
        else:
            user_input = self.gui_link.user_input.get().strip()
            if not user_input.isnumeric():
                self.gui_link.label_string = 'Error: Input a Valid Number'
            else:
                self.waiting_for_server = True
                self.socket_link.socket_output = user_input
                self.socket_link.send()
                self.gui_link.label_string = 'Waiting for Server'
            self.gui_link.update()
        return True

    def handle_recv_data(self):
        '''takes recv'd data and updates gui window'''
        if self.socket_link.socket_input.strip().lower() == "done":
            self.close(close_socket=False)
        else:
            self.waiting_for_server = False
            self.gui_link.label_string = "y^x={}".format(self.socket_link.socket_input)
            self.gui_link.update()

    def close(self,close_socket=True):
        '''clean up everything to close shop'''
        if close_socket and self.socket_link != None and self.socket_link.is_connected:
            self.socket_link.close(False)
        self.gui_link.close()
        os._exit(1)
        
            

if __name__ == '__main__':
    the_client = client()

    
