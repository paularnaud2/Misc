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
    resize('UBS Workspace - Desktop Viewer', 2488, 1399, 2737, 0)
    resize('Word', 2391, 1399, 362, 0)
    resize('Excel', 2391, 1399, 362, 0)
    resize('- Google Chrome', 2391, 1400, 362, 0)
    resize('- Visual Studio Code', 2376, 1392, 369, 0)

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
    get_infos()
    # resize_all()
    # show_workspace()
