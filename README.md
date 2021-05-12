# ![Logo](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/pngs/robloxnotif.png)[robloxnotif](https://www.github.com/jackssrt/robloxnotif)

![GitHub](https://img.shields.io/github/license/jackssrt/robloxnotif) ![GitHub repo size](https://img.shields.io/github/repo-size/jackssrt/robloxnotif) ![GitHub top language](https://img.shields.io/github/languages/top/jackssrt/robloxnotif)
![GitHub Repo stars](https://img.shields.io/github/stars/jackssrt/robloxnotif?style=social)\
robloxnotif is an open source Roblox friend notifier made in python.\
**I have only tested this on Windows 10, but it might work on other operating systems.**

# Features

- Prefix nickname with `!` or `[!]` for a different sound
- Select specific people to get notifications for
- Optional logged out mode

# How to use

Just run `main.py` with python and you will get a desktop notification when someone:

- Joins a game
- Goes online
- Goes offline
- Opens a game in studio

# Setup

Step 0: Download and install [Python](https://www.python.org/downloads/).\
Step 1: Download the code from GitHub.\
Step 2: Install the dependencies using pip in a command prompt:\
`pip install -r requirements.txt`\
Step 3: Create a file named config.json in the folder.\
Step 4: Paste this into the file you just created:

```json
{
	"usernames": {
		"PERSON 1'S USERID": "PERSON 1'S NICKNAME",
		"PERSON 2'S USERID": "PERSON 2'S NICKNAME",
		"PERSON 3'S USERID": "PERSON 3'S NICKNAME"
	}
}
```

(You can add more than 3 people)\
Step 5: Replace everything that's UPPERCASE with its value\
example:

```json
{
	"usernames": {
		"1": "!ROBLOX",
		"156": "real builderman",
		"261": "[!]cool dude"
	}
}
```

## [Optional] Login Setup

⚠ This section handles your ROBLOSECURITY (Basically your password)\
Skip this section if you don't need to know _what_ game your friend is playing or making. ⚠

Step 1: Create a new file and name it `roblosecurity.json`\
Step 2: Paste this into it:

```
{
	"roblosecurity": "YOUR ROBLOSECURITY"
}
```

Step 3: Get your roblosecurity\
Step 4: Replace `YOUR ROBLOSECURITY` with your roblosecurity that you got in Step 3\
✅ You are now logged in!

## [Optional] Auto start

Step 1: Assuming you are on Windows 10, Open task scheduler\
Step 2: From the sidebar to the right select `Create Basic Task`\
Step 3: Name it anything you want\
Step 4: Set it's trigger to `When I log on`\
Step 5: Set it's action to `Start a program`\
Step 6: Set the program to be `powershell.exe`\
Step 7: Set `Add arguments` to be `py PATH TO MAIN`\
Step 8: Replace `PATH TO MAIN` with the path to `main.py` _including_ the file extension.\
Step 9: Set `Start in` to be the path to the robloxnotif folder

✅ robloxnotif will now automatically start in a PowerShell window when you log on to Windows!

✅ You have now fully setup robloxnotif!
