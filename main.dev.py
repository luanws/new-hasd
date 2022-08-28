import sys

from scripts.update_windows import update_windows


def except_hook(cls, exception, traceback):
    traceback.print_exc()


if __name__ == '__main__':
    sys.excepthook = except_hook

    update_windows()

    from main import main
    main()
