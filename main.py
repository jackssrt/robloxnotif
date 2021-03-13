print("--roblox notif started--")
from win10toast import ToastNotifier
toast = ToastNotifier()
from time import sleep
import requests
import json
from datetime import datetime
from colorama import Fore, Back, init, Style
from playsound import playsound
init(autoreset=True) #init colorama

#load usernames / nicknames
f = open("./config.json")
config = json.load(f)
f.close()
usernames = config["usernames"]
name = config["name"]

# generate users_data for sending to api
users_data = {"userIds": list(usernames.keys())}

def log(text,color): #log function
	now = datetime.now().strftime("%X")
	print(color + f"[{now}]: {text}")

# load ROBLOSECURITY if it exists
loggedOutMode = False
try:
	f2 = open("./ROBLOSECURITY.json")
	cookie = json.load(f2)["ROBLOSECURITY"]
	f2.close()
except FileNotFoundError:
	log("starting in logged out mode",Fore.YELLOW)
	loggedOutMode = True


def isChanged(new, last): #function for checking if presence has changed or not
	
	if not new or not last:
		
		return True
	else:
		return (last["lastLocation"] != new["lastLocation"]) or (last["userPresenceType"] != last["userPresenceType"])

def do(a,boot): #function responsible for showing notification and playing sound
	thestring = None
	theicon = "robloxnotif.ico"
	thecolor = Fore.WHITE
	if a["userPresenceType"] == 2:
		thestring = "playing: " + a["lastLocation"]
		if a["lastLocation"] == "":
			thestring = "playing something"
		theicon = "playing.ico"
		thecolor = Fore.GREEN
	elif a["userPresenceType"] == 1:
		thestring = "online"
		theicon = "online.ico"
		thecolor = Fore.CYAN
	elif a["userPresenceType"] == 3:
		thestring = "in studio: " + a["lastLocation"]
		if a["lastLocation"] == "":
			thestring = "in studio making something"
		theicon = "studio.ico"
		thecolor = Fore.YELLOW
	elif (a["userPresenceType"] == 0) and (not boot):
		thestring = "now offline"
		thecolor = Fore.WHITE
		theicon = "offline.ico"
	if thestring != None:
		log(usernames[str(a["userId"])] + " is " + thestring, thecolor)

		toast.show_toast(usernames[str(a["userId"])] + " is", thestring, duration=3, icon_path="./icons/" + theicon, threaded=True)
		playsound("./sounds/robloxnotif.wav")
		while toast.notification_active(): sleep(0.1)

#main loop
last = {}
log("Hello "+name,Fore.GREEN)
while True:
	try:
		if not loggedOutMode:
			x = requests.post('https://presence.roblox.com/v1/presence/users', data=users_data,cookies= {".ROBLOSECURITY":cookie})
		else:
			x = requests.post('https://presence.roblox.com/v1/presence/users', data=users_data)
		data = x.json()

		#write to log for debug
		f1 = open("./log.log", "w", encoding="utf-8")
		json.dump(data,f1,indent=4)
		f1.close()

		if last == {}:
			log("running boot notifications: ", Fore.CYAN)
		
		for a in range(len(data['userPresences'])):
			if last != {}:
				if isChanged(data['userPresences'][a], last['userPresences'][a]):
					do(data['userPresences'][a],False)
			else:
				# run boot notifications
				do(data['userPresences'][a],True)
		last = data
	except KeyError:
		log("Error: code " + str(data["errors"][0]["code"]) + ": " + data["errors"][0]["message"],Fore.RED)
		toast.show_toast("Error: code " + str(data["errors"][0]["code"]) + ": " + data["errors"][0]["message"])
	log("***---***",Fore.BLUE)
	sleep(10)
