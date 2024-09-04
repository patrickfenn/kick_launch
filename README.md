Description:
Easily launch a kick stream in vlc along with an associated chatroom poput.

Usage:
[python3] kick_launch.py {channel name}

Reqs:
1.  Streamlink is installed.
1a. Streamlink is in default path or STREAMLINK_PATH defined in script.
2.  BROWSER_PATH must be defined in script.

Notes:
1. Tested only on mac.
2. Recommend disabling auto resize in vlc / whatever player streamlink uses.
3. I did try to have a more fully functional program which fetched details from api given profile id.
    But kick is scuffed atm and doesn't have api public + wraps everything in cloudflare. So this is
    good enough for now.

Errors:
403: Happens when cloudflare gets too many requests in a period of time. Will need to wait ~10 minutes.
