# ![Logo](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/robloxnotif.png)[robloxnotif](https://www.github.com/jackssrt/robloxnotif)

[![GitHub](https://img.shields.io/github/license/jackssrt/robloxnotif)](https://github.com/jackssrt/robloxnotif/blob/master/LICENSE) [![GitHub repo size](https://img.shields.io/github/repo-size/jackssrt/robloxnotif)](https://github.com/jackssrt/robloxnotif) [![GitHub top language](https://img.shields.io/github/languages/top/jackssrt/robloxnotif)](https://github.com/jackssrt/robloxnotif)
[![GitHub Repo stars](https://img.shields.io/github/stars/jackssrt/robloxnotif?style=social)](https://github.com/jackssrt/robloxnotif/stargazers) [![Discord Server](https://img.shields.io/discord/877936145378471987)](https://discord.gg/6EzzURCEkB)\
robloxnotif is an open source Roblox friend notifier made in python.

# Supported Operating Systems

| OS            | Support | Tested             | Notifier                                                                                             |
| ------------- | ------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| Windows 10    | ✅      | ✅                 | [win10toast-withsound](https://github.com/Tazmondo/Windows-10-Toast-Notifications-with-sound-option) |
| Other Windows | ❓      | ❌                 | [win10toast-withsound](https://github.com/Tazmondo/Windows-10-Toast-Notifications-with-sound-option) |
| Linux         | ✅      | ✅ (Linux mint 20) | [notify.py](https://pypi.org/project/notify-py/)                                                     |
| MacOS         | ❓      | ❌                 | [notify.py](https://pypi.org/project/notify-py/)                                                     |

Windows 10 and Linux are both automatically tested here on github.

# Features

- Prefix nickname with `!` or `[!]` for a different sound
- Select specific people to get notifications for
- Optional logged out mode

# How to use

Just run `main.py` with python in a terminal and you will get a desktop notification when someone:

- ![Playing icon](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/playing.png) Joins a game
- ![Online icon](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/online.png) Goes online
- ![Offline icon](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/offline.png) Goes offline
- ![In Studio icon](https://raw.githubusercontent.com/jackssrt/robloxnotif/master/icons/png/studio.png) Opens a game in studio

# Setup

If you need help setting up robloxnotif, feel free to [join the discord server!](https://discord.gg/6EzzURCEkB)

1. Download and install the latest version of [Python 3](https://www.python.org/downloads/).
1. Download the code from GitHub.
1. Install the dependencies using pip in a command prompt or terminal:
`python3 -m pip install -r requirements.txt`
1. Create a file named `config.jsonc` in the folder.
1. Paste this into the file you just created:

```jsonc
{
	"usernames": {
		//Hi i'm a comment! You can use me for organizing in here.
		"PERSON 1'S USERID": "PERSON 1'S NICKNAME",
		"PERSON 2'S USERID": "PERSON 2'S NICKNAME",
		"PERSON 3'S USERID": "PERSON 3'S NICKNAME"
	}
}
```

(You can add more than 3 people)\
(This is a JSONC file, so it can have comments)

6. Replace everything that's UPPERCASE with its value\
example:

```jsonc
{
	"usernames": {
		// Roblox admins
		"1": "!ROBLOX",
		"156": "real builderman",
		// Non roblox admins
		"261": "[!]cool dude"
	}
}
```

7. Run `main.py` with python in a terminal for the first time\
with `py main.py` or `python3 main.py` if py doesnt work

✅ You have now completed basic setup!

## [Optional] Login Setup

⚠ This section handles your .ROBLOSECURITY (Basically your password)\
Skip this section if you don't need to know _what_ game your friend is playing or making. ⚠

1. Create a new file and name it `roblosecurity.jsonc`
2. Paste this into it:

```jsonc
{
	// Do not leak your .ROBLOSECURITY!
	"roblosecurity": "YOUR ROBLOSECURITY"
	// Any one who has your roblosecurity can login as you
	// and steal everything you have on roblox!
}
```

(This is a JSONC file, so it can have comments)

3. Get your .ROBLOSECURITY
4. Replace `YOUR ROBLOSECURITY` with your roblosecurity that you got in Step 3

✅ You are now logged in!

## [Optional] [Windows-Only] Auto start

1. Assuming you are on Windows 10, Open task scheduler
2. From the sidebar to the right select `Create Basic Task`
3. Name it anything you want
4. Set it's trigger to `When I log on`
5. Set it's action to `Start a program`
6. Set the program to be `powershell.exe`
7. Set `Add arguments` to be `py PATH TO MAIN`
8. Replace `PATH TO MAIN` with the path to `main.py` _including_ the file extension.
9. Set `Start in` to be the path to the robloxnotif folder

✅ robloxnotif will now automatically start in a PowerShell window when you log on to Windows!

✅ You have now fully setup robloxnotif!
