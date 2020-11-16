import ctypes
import psutil

from AbstractOpener import AbstractOpener


class OpenNotePadFile(AbstractOpener):
    def __init__(self,string,cmd):
        self.minimize_lock_window(returned_output=string,cmd = cmd)


    def minimize_lock_window(self,returned_output,cmd):
        #Поиск в строке списка процессов pid нужного нам процесса
        index_string = returned_output.decode('cp1251').find('notepad.exe')
        string_last_proc = returned_output[index_string:]
        pid_str = string_last_proc.decode('cp1251').find('Console')
        # print('Результат выполнения команды:', string)
        # print('Результат выполнения команды:', pid_str)
        #Обнаружение окна приложения
        notepad_handle = ctypes.windll.user32.FindWindowW(u"Notepad", None)
        ctypes.windll.user32.ShowWindow(notepad_handle, 6)# Для того что бы свернуть окно

        pid_str = int(string_last_proc[len(cmd) + 4:pid_str].decode('cp1251'))
        # print('Результат выполнения команды:', pid_str)
        self.proc = psutil.Process(pid_str)

        self.proc.suspend()
