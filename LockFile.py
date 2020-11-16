import time
import subprocess
import tkin
import tkin_App_start
import NotepadFile as nf
import WordFile as wf

from time import sleep
sleep()

class LockApp():
    def __init__(self):
        #self.init_clik()
        self.cont = 0
        self.dict_compare = {
            'notepad.exe': 0,
            'WINWORD.EXE': 0,
            #'WmiPrvSE.exe': 0,
            #'explorer.exe': 0,
        }
        self.dict_classes = {
            'notepad.exe': nf.OpenNotePadFile,
            'WINWORD.EXE': wf.OpenWordFile,
            #'WmiPrvSE.exe': 0,
            #'explorer.exe': fol.OpenFolder,
        }
        self.dict_count_proc = {
            'notepad.exe': 0,
            'WINWORD.EXE': 0,
            #'WmiPrvSE.exe': 0,
            #'explorer.exe': 0,
        }
        #self.win = tkin.App()
        self.open_start_wind()
        #self.win.start_win()
        #self.detect_double_click()

    def minimize_lock_window(self):

        cmd = "tasklist"  # Здесь вместо date Ваша команда для git
        returned_output = subprocess.check_output(cmd)  # returned_output содержит вывод в виде строки байтов  subprocess.call(cmd)#
        string = returned_output.decode('cp1251')



        for key in self.dict_classes.keys():
            self.dict_count_proc[key] = string.count(key)
            if (self.dict_compare[key] < self.dict_count_proc[key]):
                #print(key,' : ', self.dict_compare[key])
                self.dict_compare[key] += 1
                file = self.dict_classes[key](returned_output, cmd)
                self.proc = file.proc
                self.open_check_wind()
            elif (self.dict_compare[key] > self.dict_count_proc[key]): # Если одно из окон закроется и потом откроют такое же приложение
                self.dict_compare[key] = self.dict_count_proc[key]



    def open_start_wind(self):
        win = tkin_App_start.AppStart()
        if (win.check_file()):
            win.start_win()
            win.mainloop()


    def open_check_wind(self):
        win_check = tkin.AppCheck()
        win_check.init_win()
        win_check.proc = self.proc
        #win_check.get_key_file()
        win_check.mainloop()



click = LockApp()
while True:
    click.minimize_lock_window()
    time.sleep(0.0001)

