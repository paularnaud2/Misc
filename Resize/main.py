import json
import parutils as u
from typing import List
import pygetwindow as gw
from pygetwindow import Win32Window

TITLES = [
    'UBS Workspace',
    'Google Chrome',
    'Brave',
    'Visual Studio Code',
    'Accueil',
]


def test():
    print([w.title for w in gw.getAllWindows()])


def save_to_json(path):
    windows: List[Win32Window] = [w for w in gw.getAllWindows() if u.like_list(w.title, TITLES)]
    d = json.loads(u.load_txt(path, False))
    for w in windows:
        if w.left == -32000:
            print(f"A problem occured with window '{w.title}'")
            continue
        k = u.like_list(w.title, TITLES)
        d[k] = {
            'width': w.width,
            'height': w.height + 1,
            'left': w.left,
            'top': w.top - 1,
        }
    u.log_dict(d)
    u.save_list([json.dumps(d, indent=4)], path)


def restore_json(path):
    d = json.loads(u.load_txt(path, False))
    for title in d:
        move_and_resize(title, d[title])


def move_and_resize(title, d):
    print(f"Moving and resizing '{title}'")
    wl = gw.getWindowsWithTitle(title)
    if not wl:
        return

    window: Win32Window = wl[0]
    window.resizeTo(d['width'], d['height'])
    window.moveTo(d['left'], d['top'])


if __name__ == '__main__':
    # test()
    save_to_json()
    # restore_json()
