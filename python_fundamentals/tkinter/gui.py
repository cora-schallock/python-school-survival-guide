import tkinter as tk

class gui():
    def __init__(self,title="gui^x"):
        self.link_to_client_server = None
        self.running = False

        self.title = title
        self.label_string = 'Click "Connect" to connect server & client'
        self.button_string = 'Connect'
      
        #Step 1) Create Tkinter label
        self.setup_window(self.title)

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
        self.result.set(self.label_string)
        self.result_label = tk.Label(self.root, textvariable=self.result,width=300)
        self.result_label.pack()
      
    def create_button(self):
        '''create connection/submit/calculate button'''
        self.the_button = tk.Button(self.root,text=self.button_string,command=lambda:self.on_click())
        self.the_button.pack()

    def create_quit_button(self):
        '''create quit button to close everything'''
        self.quitButton = tk.Button(self.root,text="Quit",command=lambda:self.on_quit())
        self.quitButton.pack()

    def on_click(self):
        '''code to run if connect/send button is clicked'''
        self.link_to_client_server.done_handeling_click = False
        self.link_to_client_server.handle_click()

    def on_quit(self):
        '''code to run if quit button is clicked'''
        self.link_to_client_server.close()

    def update(self):
        '''update label and button text'''
        self.result.set(self.label_string)
        self.the_button.configure(text=self.button_string)
        self.root.update()

    def close(self):
        '''close tkinter window'''
        self.root.destroy()

        
    
