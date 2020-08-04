# Th3BlackHand

<p align="center">
  <img src="https://media.giphy.com/media/LLxAlFgptpskFCxyor/giphy.gif" />
</p>

A python script that locks your laptop/pc screen if you forget to lock it .. using Firebase ! - useful if you work/live around nosy people :D



![Demo](https://media.giphy.com/media/TEcWMqTQqdBkKsbuZf/giphy.gif)

* As you can see in the above GIF, the tool keeps locking the screen, this happens because the value in the firebase realtime database is changed to False .. When you are not around your laptop/pc just change the value in the database to False using your mobile phone ;) 

--- 
![Alt text](https://i.imgur.com/UyF8a6W.jpg "Firebase Realtime Database from phone")

* Firebase Realtime Database from a mobile phone browser :)  
---

* Why should you use this tool?  
>> 1. Keep the nosy people away from your computer :D
>> 2. All you gotta do is just run the tool ONE time manually and it will configure itself in the startup applications and work in the background processes  
>> 3. You will not see any command prompt popping out of nowhere !  
>> 4. How to check if the tool is working or even kill it ?  

>>> ![Alt text](https://i.ibb.co/FmM0wHV/3.png "Check if the tool is working")

>>> 3.1 Go to Task manager > Background processes > Python  
>>> 3.2 Type the following command in the CMD/Terminal: tasklist /v | find "python"  

---

* Required Libraries ?
> getpass  
> os  
> socket  
> time  
> ctypes  

install the above libraries using the following command : pip.exe install [library name]  

!! If you face a problem installing Crypto Just install the following libaray instead: [pycryptodome] !!

NOTE: 

While trying to install the libraries: 

Please delete the following code block from Th3BlackHand.py

CMD = ctypes.windll.kernel32.GetConsoleWindow()      
if CMD != 0:      
    ctypes.windll.user32.ShowWindow(CMD, 0)      
    ctypes.windll.kernel32.CloseHandle(CMD)

----

* Python version?  

> Python 3.7.5  

---

* How to install the tool?    

> 1. Download Th3BlackHand.py   
> 2. Modify the code with your Laptop paths such as the python3 compiler path.  
> 3. Modify the link of firebase realtime database with yours !  
> 4. Import 'test-ed516-export.json' to your firebase realtime database .. just to save you some time :)  
> 5. Run Th3BlackHand.py using the Python3 Compiler!! <make sure to install the libraries above FIRST!>  

---

* Stuck on something? 

> open a new issue ;)


