#! python3
# 正方形螺旋图案。
# 带有计时器。
# 需要在cmd中运行。
# 在画图或其他类似作图软件中绘画
import pyautogui, time
time.sleep(5)

pyautogui.click()   # click to put drawing program in focus
distance = 200
stime=time.time()

while distance > 0:

    pyautogui.dragRel(distance, 0, duration=0.2)    # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)    # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)   # move left
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=0.2)   # move up
    time2 = time.time()
    dtime = time2 - stime
    print(str(dtime), end='')
    print('\b' * len(str(dtime)), end='', flush=True)
etime = time.time()
print('\nIt costs ' + str(etime - stime) + ' seconds.')