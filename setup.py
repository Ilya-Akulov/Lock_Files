from cx_Freeze import setup, Executable

executables = [Executable('LockFile.py',
targetName='Lock_file.exe',
#base='Win32GUI',
icon='lock.ico')]


includes = ['WordFile', 'NotepadFile', 'tkin_App_start','tkin', 'subprocess', 'time' , 'tkinter', 'os', 'ctypes', 'psutil', 'abc' , 'AbstractOpener']

zip_include_packages = ['WordFile', 'NotepadFile', 'tkin_App_start','tkin', 'subprocess', 'time' , 'tkinter', 'os', 'ctypes', 'psutil', 'abc' , 'AbstractOpener']

include_files = ['LockFile.py',
'tkin_App_start.py',
'tkin.py',
'AbstractOpener.py',
'NotepadFile.py',
'WordFile.py'
]

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name='LockFile',
version='0.0.1',
description='Приложение для блокировки файлов',
executables=executables,
options=options)