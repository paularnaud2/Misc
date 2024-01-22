import time
import json
import parutils as u
from typing import List
import pygetwindow as gw
from pygetwindow import Win32Window

TITLES = [
    'UBS Workspace',
    'Google Chrome',
    'Visual Studio Code',
    'C:\\',
]
DATA_PATH = 'Resize/data.json'


def get_infos():
    while True:
        print(gw.getActiveWindow())
        print(gw.getActiveWindowTitle())
        time.sleep(5)


def resize(title, width, hight, left, top):

    wl = gw.getWindowsWithTitle(title)
    if not wl:
        return

    window = wl[0]
    window.resizeTo(width, hight)
    window.moveTo(left, top)


def save_to_json():
    windows: List[Win32Window] = [w for w in gw.getAllWindows() if u.like_list(w.title, TITLES)]
    d = {}
    for w in windows:
        d[w.title] = {
            'width': w.width,
            'height': w.height,
            'left': w.left,
            'top': w.top,
        }
    u.log_dict(d)
    u.save_list([json.dumps(d)], DATA_PATH)


def restore_json():
    d = json.loads(u.load_txt(DATA_PATH, False))
    for title in d:
        t = u.like_list(title, TITLES)
        move_and_resize(t, d[title])


def move_and_resize(title, d):
    print(f"Moving and resizing '{title}'")
    wl = gw.getWindowsWithTitle(title)
    if not wl:
        return

    window: Win32Window = wl[0]
    window.resizeTo(d['width'], d['height'])
    window.moveTo(d['left'], d['top'])


def resize_all():
    resize('UBS Workspace', 2488, 1399, 2737, 0)
    resize('Word', 2391, 1399, 362, 0)
    resize('Excel', 2391, 1399, 362, 0)
    resize('Google Chrome', 2391, 1400, 362, 0)
    resize('Visual Studio Code', 2376, 1392, 369, 0)

    # window = gw.getWindowsWithTitle('- Visual Studio Code')[0]
    # window.minimize()

    # window = gw.getWindowsWithTitle('- Word')[0]
    # window = gw.getWindowsWithTitle('- Google Chrome')[0]
    # window.activate()

    print("All windows resized")


def show_workspace():
    title = 'UBS Workspace - Desktop Viewer'
    resize(title, 2488, 1040, 80, 0)
    gw.getWindowsWithTitle(title)[0].activate()


if __name__ == '__main__':
    # get_infos()
    # resize_all()
    # show_workspace()
    # save_to_json()
    restore_json()
