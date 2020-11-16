import tkinter as tk

from tkinter import ttk
from tkinter import messagebox as mb
#import tkinter.messagebox as mb



import subprocess
import os

#сделать еще один файл для окна задания пароля

class AppCheck(tk.Tk):
    def __init__(self):
        super().__init__()


    def init_win(self):
        self.proc = None
        self.flag = None
        self.count_try = 0
        self.get_key_file()
        self.title("Ввод пароля")
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        lablPass = tk.Label(self, text="Пароль: ")
        lablPass.place(x=50, y=100)

        self.entry_pass = ttk.Entry(self, show="*")
        self.entry_pass.place(x=100, y=100)

        self.btnOk = ttk.Button(self, text="Ok", command=self.click_btn)
        self.btnOk.place(x=150, y=160)

    def get_pass(self):
        passw = self.entry_pass.get()
        self.entry_pass.delete(0, tk.END)
        #print(passw)
        #print(self.password)
        if( passw == self.password):
            return  True
        else:
            return False


    def get_key_file(self):
        file = open("key_file.txt", 'r')
        self.password = file.read()
        #print('pass: ', self.password)
        file.close()


    def click_btn(self):
        self.flag = self.get_pass()
        self.count_try += 1
        if(self.flag  and self.count_try < 4):
            self.proc.resume()
            self.destroy()
        elif(self.count_try == 3):
            self.proc.kill()
            self.destroy()
        else:
            if(self.count_try == 2):
                string_exp = 'Вы ввели неверный пароль\n Последняя попытка'
            else:
                string_exp = 'Вы ввели неверный пароль\n Осталоь попыток: ' + str(3 - self.count_try)

            mb.showinfo(title='Предупреждение', message=string_exp)

'''
if __name__ == '__main__':
    app = App()
    app.init_win()
    app.mainloop()
'''
