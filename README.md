# GPS Coordinate Teleport
Script that allows you to teleport your GPS Joystick from TheAppNinjas instance into any GPS coordinates directly from your computer.

Necessary apps/files:
GPS Joystick by TheAppNinjas 
ADB (Android Debug Bridge)
Python

You'll need to introduce your adb.exe path & your phone IP into the variables path and phone_ip respectively.

To find your path:
1. Go to the folder with adb.exe is. Copy the path (something like C:\Users\UserName\Documents\platform-tools)

To find your phone ip:
1. Connect your phone to the computer via USB.
2. Open cmd, you can do it by pressing Windows Key + R and typing cmd in the box.
3. Type "cd " and paste your path for adb, so something like this "cd C:\Users\UserName\Documents\platform-tools"
4. Type "adb tcpip 5555"
5. Type "adb shell ip -f inet addr show wlan0" and copy your phone's IP.
6. Disconnect your phone from the computer via USB.

Then edit the file:
1. Open coordspc.py with any text editor like Notepad++.
2. On the 3rd line (path = "") insert your adb.exe path that we previously copied and double the \s. It should look like this: path = "C:\\Users\\UserName\\Documents\\platform-tools".
3. On the 4th line (phone_ip = "") insert your phone ip followed by :5555. It should look like this: phone_ip = "192.168.1.34:5555".
4. Save the changes (CTRL+S) and exit. 

You're ready to run.
