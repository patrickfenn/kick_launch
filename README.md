Description:
Easily launch a kick stream in vlc along with an associated chatroom poput.

Usage:
[python3] kick_launch.py {channel name}

Reqs:
1. Streamlink is installed.
2. Streamlink is in default path or STREAMLINK_PATH defined in script.
3. BROWSER_PATH must be defined in script.

Notes:
1. Tested only on mac.
2. Recommend disabling auto resize in vlc / whatever player streamlink uses.
3. I did try to have a more fully functional program which fetched details from api given profile id.
    But kick is scuffed atm and doesn't have api public + wraps everything in cloudflare. So this is
    good enough for now.
4. For ease of use, I recommend appending .zshrc (or another shell's config) with function:
    kick () {
        {path of kick_chat.py} $1
    }
    Then can just use: `kick {channel}` in shell. Remember to source .zshrc or restart terminal.

Errors:
403: See https://github.com/streamlink/streamlink/issues/6018 . I typically can wait some time (~10 min) and it will work again.
