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
    resize('UBS Workspace - Desktop Viewer', 2021, 1047, 2065, 0)
    resize('- Word', 1677, 1040, 398, 0)
    resize('- Google Chrome', 1693, 1047, 390, 0)
    resize('- Visual Studio Code', 1677, 1040, 398, 0)

    print("All windows resized")


if __name__ == '__main__':
    # get_infos()
    resize_all()
