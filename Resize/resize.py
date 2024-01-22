import os
import main
import os.path as p

if __name__ == '__main__':
    cwd = p.dirname(p.dirname(p.realpath(__file__)))
    print(cwd)
    os.chdir(cwd)
    main.restore_json()
