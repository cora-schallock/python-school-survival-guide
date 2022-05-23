import os
import sys
import threading

import tkinter as tk

class gui():
    def __init__(self,title="gui^x"):
        self.link_to_client_server = None
        
        #Step 1) Create Tkinter label
        self.setup_window(title)

        #Step 2) Create Tkinter variables
        self.user_input = tk.StringVar()
        self.result = tk.StringVar()

        #Step 3) Create Tkinter objects
        self.create_result_label()
        self.create_entry()
        self.create_button()
        self.create_quit_button()
          
    def setup_window(self,title):
        '''creates tkinter window'''
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry('300x100')
        self.root.configure(background='blue')
        self.root.resizable(1,1)
          
    def create_entry(self):
        '''creates entry'''
        self.text_entry = tk.Entry(self.root, textvariable=self.user_input,width=300)
        self.text_entry.pack()

    def create_result_label(self):
        '''cretaes label'''
        self.result.set('Click "Connect" to connect server & client')
        self.result_label = tk.Label(self.root, textvariable=self.result,width=300)
        self.result_label.pack()
      
    def create_button(self):
        '''create connection/submit/calculate button'''
        self.the_button = tk.Button(self.root,text="Connect",command=self.handle_button_click)
        self.the_button.pack()

    def create_quit_button(self):
        '''create quit button to close everything'''
        self.quitButton = tk.Button(self.root,text="Quit",command=self.close).pack() #self.root.destroy

    def update_label(self,new_label):
        '''update label text'''
        self.result.set(new_label)

    def update_button_text(self,new_button_text):
        '''update button text'''
        self.the_button.configure(text=new_button_text)

    
    def close(self,close_other_endpoint=True):
        '''function to close everything'''
        self.root.after(10, self.root.destroy) #close tkinter window... but wait 10ms first
        self.link_to_client_server.close(close_other_endpoint) #closes socket endpoint
        #sys.exit() #use this instead of sys.exit() to close everything (regardless of threads) #https://stackoverflow.com/a/1489838
        os._exit(1) #exit the program

    def validate_entry(self):
        '''verifies user entry input'''
        try:
            return int(self.user_input.get())
        except:
            return None
            
    def handle_button_click(self):
        '''hanldes button click for connect/ send/ calculate button'''
        if not self.link_to_client_server.is_connected:
            #Creates thread to setup socket connection, and pauses GUI until connection is made:
            start_socket_thread = threading.Thread(target=self.link_to_client_server.setup_socket_connection)
            start_socket_thread.setDaemon(True)
            start_socket_thread.start()

            self.root.wait_variable(self.link_to_client_server.is_connected)
        else:
            #Checks user input:
            user_entry = self.validate_entry()
            if user_entry == None:
                self.update_label("Error: Please enter a valid integer")
                return

        if self.link_to_client_server.waiting_for_socket_input:
            #Creates thread to recv data, and pauses GUI until recv'd data (socket input)
            recv_thread = threading.Thread(target=self.link_to_client_server.recvive)
            recv_thread.setDaemon(True)
            recv_thread.start()
            
            self.root.wait_variable(self.link_to_client_server.waiting_for_socket_output)
        elif self.link_to_client_server.waiting_for_socket_output:
            #Figures out what the socket ouput should be:
            if self.link_to_client_server.is_server:
                y = int(self.link_to_client_server.socket_input)
                x = int(self.user_input.get())
                the_ouput = y**x
            else:
                the_ouput = self.user_input.get()
            self.link_to_client_server.socket_output = str(the_ouput)

            #Send socket output:
            self.link_to_client_server.send()

            #Creates thread to recv data, and pauses GUI until recv'd data (socket input)
            recv_thread = threading.Thread(target=self.link_to_client_server.recvive)
            recv_thread.setDaemon(True)
            recv_thread.start()
            
            self.root.wait_variable(self.link_to_client_server.waiting_for_socket_output)

    
if __name__ == '__main__':
       test_gui = gui()
