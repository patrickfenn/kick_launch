#!/opt/homebrew/bin/python3

"""
Usage:
[python3] kick_launch.py {channel name}

Reqs:
1.  Streamlink is installed.
1a. Streamlink is in default path or STREAMLINK_PATH defined below.
2.  BROWSER_PATH must be defined below.

Notes:
1. Tested only on mac.
2. Recommend disabling auto resize in vlc / whatever player streamlink uses.
3. I did try to have a more fully functional program which fetched details from api given profile id.
    But kick is scuffed atm and doesn't have api public + wraps everything in cloudflare. So this is
    good enough for now.

Errors:
403: Happens when cloudflare gets too many requests in a period of time. Will need to wait ~10 minutes.
"""

import os
import webbrowser
import shutil
import sys

# Best if you choose something other than main browser
BROWSER_PATH = "/Applications/Firefox.app"
STREAMLINK_PATH = None

def main():
    streamlink_path = ""
    if not STREAMLINK_PATH:
        streamlink_path = shutil.which("streamlink")
        if not streamlink_path:
            print("Could not find streamlink path in PATH")
            return 1
    else:
        streamlink_path = STREAMLINK_PATH

    channel_name = sys.argv[-1]
    base_url = f"https://www.kick.com/{channel_name}"

    streamlink_pid = os.fork()
    if streamlink_pid == 0:
        args = [streamlink_path,
                "-a", "--play-and-exit",
                base_url, "best"]
        env = os.environ.copy()
        os.execve(streamlink_path, args, env)
    elif streamlink_pid < 0:
        print ("Issue with forking streamlink")
        return 2
    else:
        chat_url = f"{base_url}/chatroom"
        browser = webbrowser.get(f"open -a {BROWSER_PATH} %s")
        if not browser.open_new(chat_url):
            print("Failed to open browser")
        os.waitpid(streamlink_pid, 0)

    return 0

if __name__ == "__main__":
    main()