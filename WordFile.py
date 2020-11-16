import ctypes
import psutil
import subprocess

from AbstractOpener import AbstractOpener


class OpenWordFile(AbstractOpener):

    def __init__(self, string, cmd):
        self.minimize_lock_window(returned_output=string, cmd=cmd)

    def minimize_lock_window(self, returned_output, cmd):
        index_string = returned_output.decode('cp1251').find('WINWORD.EXE')
        string_last_proc = returned_output[index_string:]
        pid_str = string_last_proc.decode('cp1251').find('Console')
        # print('Результат выполнения команды:', string)
        # print('Результат выполнения команды:', pid_str)

        notepad_handle = ctypes.windll.user32.FindWindowW(u"Word", None)
        ctypes.windll.user32.ShowWindow(notepad_handle, 6)

        pid_str = int(string_last_proc[len(cmd) + 4:pid_str].decode('cp1251'))
        # print('Результат выполнения команды:', pid_str)
        self.proc = psutil.Process(pid_str)

        self.proc.suspend()