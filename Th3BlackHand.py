#By MOHAMMED ADEL 
import getpass
import os
import socket
import time
import ctypes

USER_NAME = getpass.getuser() 
file_path = "C:/Users/Laptop/AppData/Local/Programs/Python/Python37/python.exe C:/Users/Laptop/Desktop/OutForCoffe/OfC.py" # Modify the paths accordingly 
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME # i suppose this works for all windows users :) 
with open(bat_path + '\\' + "Th3BlackHand.bat", "w+") as bat_file:
    bat_file.write(r'start "" %s' % file_path)

CMD = ctypes.windll.kernel32.GetConsoleWindow()      
if CMD != 0:      
    ctypes.windll.user32.ShowWindow(CMD, 0)      
    ctypes.windll.kernel32.CloseHandle(CMD)

while True:
    time.sleep(2)
    try:
        socket.create_connection(("1.1.1.1", 53))
        print("Internet Connection -> OK")
        from firebase import firebase
        import json
        import ctypes
        firebase = firebase.FirebaseApplication("https://test-ed516.firebaseio.com/", None) # Change the firebase url to yours !
        Value = firebase.get('/status/what/', None) # Change the firebase realtime database paths accordingly !!
        if "True" == Value:
            print("You Are Allowed :)")
        elif "False" == Value:
            ctypes.windll.user32.LockWorkStation()
            print("Not Allowed! :(")
    except OSError:
        print("Internet Connection -> !OK")
    
