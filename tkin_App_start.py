import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import subprocess
import os

#сделать еще один файл для окна задания пароля

class AppStart(tk.Tk):
    def __init__(self):
        super().__init__()



    def start_win(self):
        self.title('Создание пароля')
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        lablPass = tk.Label(self, text="Пароль: ")
        lablPass.place(x=50, y=100)

        self.entry_pass = ttk.Entry(self, show="*")
        self.entry_pass.place(x=100, y=100)

        self.btnOk = ttk.Button(self, text="Ok", command=self.click_btn_start)
        self.btnOk.place(x=150, y=160)


    def check_file(self):
        if(not os.path.exists("key_file.txt")):
                #self.start_win()
                return True
        else:
            return False

    def get_key_file(self):
        file = open("key_file.txt", 'r')
        self.password = file.read()
        #print('pass: ', self.password)
        file.close()


    def set_pass(self):
        self.key_file = open("key_file.txt", 'w+')
        self.password = self.entry_pass.get()
        self.key_file.write(self.password)
        self.key_file.close()
        self.entry_pass.delete(0, tk.END)
        self.destroy()




    def click_btn_start(self):
        self.set_pass()




