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

f = open(bat_path + '\\' + "status.txt", "w")
f.write("")
f.close()

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
            f = open(bat_path + '\\' + "status.txt", "w")
            f.write("True")
            f.close()
            print("You Are Allowed :)")
        elif "False" == Value:
            f = open(bat_path + '\\' + "status.txt", "w")
            f.write("False")
            f.close()
            ctypes.windll.user32.LockWorkStation()
            print("Not Allowed! :(")
    except OSError:
        print("Internet Connection -> !OK")
        f = open(bat_path + '\\' + "status.txt", "r")
        Status = f.read()
        if "True" == Status:
            print("allowed")
        elif "False" == Status:
            ctypes.windll.user32.LockWorkStation()
            print("Not Allowed! :(")
        f.close()
