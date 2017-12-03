#! python3
# mouseNow.py - Displays the mouse cursor's current position.
# 在pycharm中没有成功，在cmd中成功。
import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        #print(len(positionStr))
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')


