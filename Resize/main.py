import time
import pygetwindow as gw


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


def resize_all():
    resize('UBS Workspace - Desktop Viewer', 2021, 1040, 2065, 0)
    resize('- Word', 1790, 1040, 290, 0)
    resize('- Google Chrome', 1790, 1040, 290, 0)
    resize('- Visual Studio Code', 1677, 1033, 398, 0)

    print("All windows resized")
