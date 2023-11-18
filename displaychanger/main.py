import subprocess
import os
import json
from tkinter import messagebox


def switch_display_mode():
    flag = flag_manager()
    print(flag)

    if flag == 1:
        # シングルディスプレイモードに切り替え
        subprocess.run(['DisplaySwitch.exe', '/internal'])
    else:
        # デュアルディスプレイモードに切り替え
        subprocess.run(['DisplaySwitch.exe', '/extend'])


def flag_manager():
    if os.path.exists('flag.json'):
        with open('flag.json', 'r') as infile:
            flag = json.load(infile)
            f = flag['flag']
    else:
        return 0

    with open('flag.json', 'w') as outfile:
        if f == 1: wr = 0
        else: wr = 1
        s = {
            'flag': wr,
        }
        json.dump(s, outfile)

    return f


switch_display_mode()
# ディスプレイモードを切り替えるswitch_display_mode()