from tkinter import *
# from tkinter import ttk
import tkinter as tk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1920x1080")
        self.main_menu()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)     
        self.frame1.pack()
        self.reg_txt = tk.Label(self.frame1, text='login', bg="blue", width="300", height="2")
        self.reg_txt.pack()
        
        # this will create a label widget
        self.l1 = tk.Label(self.frame1, text = "First:")
        self.l2 = tk.Label(self.frame1, text = "Second:")

        self.l1.pack()
        self.l1_label = Entry(self.frame1, bd=5)
        self.l1_label.pack()

        self.l2.pack()
        self.l2_label = Entry(self.frame1, bd=5, show='*')
        self.l2_label.pack()

        tk.Label(self.frame1, text="").pack()
        self.register_btn = tk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()

    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='register')
        self.reg_txt2.pack()

        tk.Label(self.frame2, text="").pack()
        self.login_btn = tk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

        tk.Label(self.frame2, text="").pack()
        self.quit_txt = tk.Button(self.frame2, text='press to quit program', command=root.destroy)
        self.quit_txt.pack(pady=10)

        # tk.Label(text=root.winfo_screenwidth()).pack()
        # tk.Label(text=root.winfo_screenheight()).pack()


    def main_menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.menu = Frame(self.master, width=600, height=600)
        # self.menu.title("Account login")
        
        tk.Label(text="Select Your Choice", bg="blue", width="400", height="2", font=("Calibri", 24)).pack()
        tk.Label(text="\n").pack()
        tk.Button(text="Login", height="5", width="40", command = self.login).pack()
        tk.Label(text="\n\n").pack()
        tk.Button(text="Register", height="5", width="40", command= self.register).pack()

if __name__ == '__main__':
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root = Tk()
        root.attributes('-fullscreen', True)
        app(root)
        root.mainloop()