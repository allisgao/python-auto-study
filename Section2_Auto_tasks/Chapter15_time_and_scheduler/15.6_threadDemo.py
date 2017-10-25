# coding = utf-8

import threading, time, datetime

print('Start of program.')
startTime = time.time()
# time.sleep(1)

def takeANap():
    time.sleep(5)
    print('Wake up!')
    # 这两行用来计时
    totalTime = round(time.time() - startTime, 5)
    print('Total cost time: ' + str(totalTime))


threadObj = threading.Thread(target=takeANap)
threadObj.start()
# 这两行用来计时
totalTime = round(time.time() - startTime, 5)
print('Total cost time: ' + str(totalTime))

print('End of program.')
