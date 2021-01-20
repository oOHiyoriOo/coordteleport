import os

path = ""
phone_ip = ""

os.chdir(path)
connect = os.popen("adb connect {}".format(phone_ip)).read()
print(connect)
coords = ""

while coords != "quit":
    coords = input("Insert coords or type ""quit"" to disconnect: ")
    if coords == "quit":
        os.system("adb disconnect")
    else:
        x, y = coords.split(",", 1)
        os.system("adb shell am startservice -a theappninjas.gpsjoystick.TELEPORT --ef lat {} --ef lng {}".format(x,y))