from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import customtkinter
import os
from PIL import Image, ImageTk

CURRENT_PATH = os.getcwd()

class app:
    def __init__(self, master):
        self.master = master
        window_width = 1080
        window_height = 1920
        # get the screen dimension
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.master.resizable(0, 0)
        self.master['bg'] = '#B9D6F2'
        self.main_menu()


    def login(self):  
        #   Setting up grid and frame for button widgets/ texts
        #   comment these out for now, as they messed with the alignment of widgets for tkinter
        # Grid.columnconfigure(root, index = 0, weight = 1)
        # Grid.rowconfigure(root, 0, weight = 1)

        for i in self.master.winfo_children():
            i.destroy()
        #   Arrow on top corner left
        self.arrow_logo = customtkinter.CTkImage(Image.open("Frontend\\logostorage\\material-symbols_arrow-back.png"), size=(50, 50))
        arrow_label = customtkinter.CTkButton(self.master, image=self.arrow_logo, text="", fg_color='#D9D9D9', command=self.main_menu)
        arrow_label.grid(row = 0, column = 0, sticky=tk.NW)

        #   Cube logo
        self.imge = customtkinter.CTkImage(Image.open("Frontend\\logostorage\\vaadin_cube.png"), size=(180, 180))
        img_label = customtkinter.CTkLabel(self.master, text="", image=self.imge)
        img_label.grid(column=1, row=0, pady=35)

        tk.Label(self.master, text="Login", font=("Inter", 40), bg='#B9D6F2').grid(column=1, row=1, pady=5, sticky=tk.N)

        #   Insert text widget/ To add in sending data to firebase admin things after actual login attempt
        entry_1 = customtkinter.CTkEntry(self.master, placeholder_text="Username", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        entry_1.grid(column=1, row=2, rowspan=2, sticky=tk.N, pady=25)

        entry_2 = customtkinter.CTkEntry(self.master, placeholder_text="Password", show="*", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        entry_2.grid(column=1, row=2, rowspan=2, pady=30)

        #   Login button
        bottom_ = customtkinter.CTkButton(self.master, text="Login", font=("Inter", 25), corner_radius=20, text_color="#FFFFFF", fg_color='#051739', width=300, height=50, command=root.destroy)
        bottom_.grid(column=1, row=4)


    def register(self):  
        #   Setting up grid and frame for button widgets/ texts
        #   comment these out for now, as they messed with the alignment of widgets for tkinter
        # Grid.columnconfigure(root, index = 0, weight = 1)
        # Grid.rowconfigure(root, 0, weight = 1)

        for i in self.master.winfo_children():
            i.destroy()
        #   Arrow on top corner left
        self.arrow_logo = customtkinter.CTkImage(Image.open("Frontend\\logostorage\\material-symbols_arrow-back.png"), size=(50, 50))
        arrow_label = customtkinter.CTkButton(self.master, image=self.arrow_logo, text="", fg_color='#D9D9D9', command=self.main_menu)
        arrow_label.grid(row = 0, column = 0, sticky=tk.NW)
    
        #   Cube logo
        self.imge = customtkinter.CTkImage(Image.open("Frontend\\logostorage\\vaadin_cube.png"), size=(180, 180))
        img_label = customtkinter.CTkLabel(self.master, text="", image=self.imge)
        img_label.grid(column=1, row=0, pady=35)

        tk.Label(self.master, text="Register", font=("Inter", 40), bg='#B9D6F2').grid(column=1, row=1, pady=5)

        #   Insert text widget/ To add in sending data to firebase admin things after actual login attempt
        entry_1 = customtkinter.CTkEntry(self.master, placeholder_text="Name", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        # entry_1.grid(column=1, row=2, rowspan= 2, sticky=tk.N, pady=25)
        entry_1.grid(column=1, row=2, pady=15)

        entry_2 = customtkinter.CTkEntry(self.master, placeholder_text="Username", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        # entry_2.grid(column=1, row=2, pady=25)
        entry_2.grid(column=1, row=3, pady=15)

        entry_3 = customtkinter.CTkEntry(self.master, placeholder_text="Password", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        # entry_3.grid(column=1, row=3, rowspan= 2, sticky=tk.N, pady=25)
        entry_3.grid(column=1, row=4, pady=15)

        entry_4 = customtkinter.CTkEntry(self.master, placeholder_text="Confirm password", font=("Inter", 20), corner_radius=15, text_color='#989898', fg_color="#FFFFFF", width=300, height=45)
        # entry_4.grid(column=1, row=3, pady=25)
        entry_4.grid(column=1, row=5, pady=15)

        #   Register button
        bottom_ = customtkinter.CTkButton(self.master, text="Register", font=("Inter", 25), corner_radius=20, text_color="#FFFFFF", fg_color='#051739', width=300, height=50, command=root.destroy)
        bottom_.grid(column=1, row=8)


    def main_menu(self):
        #   Setting up grid and frame for button widgets/ texts
        Grid.columnconfigure(root,0,weight=1)
        Grid.columnconfigure(root,1,weight=1)
        Grid.columnconfigure(root,2,weight=1)
        Grid.rowconfigure(root,3,weight=1)
        Grid.rowconfigure(root,4,weight=1)

        for i in self.master.winfo_children():
            i.destroy()
        #   Title 
        tk.Label(self.master, text="Cube", font=("Inter", 64), bg='#B9D6F2').grid(column=1, row=0, sticky=tk.N, padx=1, pady=45)
        
        #   Cube logo
        self.imge = customtkinter.CTkImage(Image.open("Frontend\\logostorage\\vaadin_cube.png"), size=(220, 220))
        img_label = customtkinter.CTkLabel(self.master, text="", image=self.imge)
        img_label.grid(column=1, row=1)

        #   Menu texts/ three buttons: Login, Register, & Quit
        tk.Label(self.master, text="Welcome\nglad to see you!\n\n\n\n", font=("Inter", 25), bg='#B9D6F2').grid(column=1, row=2, padx=1, pady=10, rowspan=2, sticky=tk.N)

        bt1 = customtkinter.CTkButton(self.master, text="Login", font=("Inter", 35), corner_radius=20, text_color="#FFFFFF", fg_color='#051739', width=350, height=75, command=self.login)
        bt1.grid(column=1, row=2, rowspan=2, sticky=tk.S, pady=30)

        bt2 = customtkinter.CTkButton(self.master, text="Register", font=("Inter", 35), corner_radius=20, text_color="#FFFFFF", fg_color='#051739', width=350, height=75, command=self.register)
        bt2.grid(column=1, row=3, pady=100)

        bt3 = customtkinter.CTkButton(self.master, text="Quit", font=("Inter", 35), corner_radius=20, text_color="#000000", fg_color='#FFFFFF', width=250, height=75, command=root.destroy)
        bt3.grid(column=1, row=4)


if __name__ == '__main__':
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root = Tk()
        # root = customtkinter.CTk()                    #   TO DO: may change the app from using Tk to customtkinterCTk as app frame instead
        root.attributes('-fullscreen', True)
        app(root)
        root.mainloop()