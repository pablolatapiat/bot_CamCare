import pyautogui as pag
from colorthief import ColorThief
from math import sqrt
import datetime

pag.FAILSAFE = True
# pag.PAUSE = 1

finalRes = []
grids = {
    36: {
        'w': 318,
        'h': 158
    },
    49: {
        'w': 272,
        'h': 132
    },
    64: {
        'w': 238,
        'h': 113
    },
}

def get_screeshots(grid):
    x = 1
    y = 21
    j = 2
    k = 6

    for i in range(grid):
        if grid == 49 and (i == j or i == k):
            pag.screenshot(f'python/cams/cam_{i+1}.png', region=(x + 1, y, grids[grid]['w'], grids[grid]['h']))
            x += grids[grid]['w'] + 3
            j += 7
            k += 7

        else:
            pag.screenshot(f'python/cams/cam_{i+1}.png', region=(x, y, grids[grid]['w'], grids[grid]['h']))
            x += grids[grid]['w'] + 2

        if (i+1) % sqrt(grid) == 0:
            x = 1
            y += grids[grid]['h'] + 22

def get_report(grid):
    cam_def = (20, 20, 20)
    no_cam = (92, 100, 116)
    for i in range(1, grid):
        color_thief = ColorThief(f'python/cams/cam_{i}.png')

        if color_thief.get_color(quality=1) <= cam_def:
            print(f'\033[31mCamera \033[33mCAM_{i}\033[31m com defeito!\033[m')
            finalRes.append(f'Camera CAM_{i} com defeito!')
        elif color_thief.get_color(quality=1) == no_cam:
            print(f'\033[36mCamera \033[33mCAM_{i}\033[36m nao conectada!\033[m')
            finalRes.append(f'Camera CAM_{i} nao conectada!')
        else:
            print(f'\033[32mCamera \033[33mCAM_{i}\033[32m em funcionamento!\033[m')
            finalRes.append(f'Camera CAM_{i} em funcionamento!')
    print(finalRes)
# get_screeshots(49)
get_report(49)
while True:
    if str(datetime.datetime.now().strftime('%H:%M')) == '23:20':
        get_screeshots(49)
        get_report(49)
# pag.screenshot(f'python/teste.png')