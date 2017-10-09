from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048')
elem = browser.find_element_by_class_name('container')
i = 0 # counter

'''
# 这里，设想的是随机按上下左右。
myUp = elem.send_keys(Keys.UP)
myDown = elem.send_keys(Keys.DOWN)
myLeft = elem.send_keys(Keys.LEFT)
myRight = elem.send_keys(Keys.RIGHT)
for myAction in random(myUp, myDown, myLeft, myRight):
    while True:
        try:
            myAction
            i = i + 1
        except:
            print('Game Over.')


'''
# 这里是按照上下左右的顺序操作的。
while True:
    elem.send_keys(Keys.UP)
    # i = i + 1
    # print('total: ' + str(i) + 'times option')
    elem.send_keys(Keys.RIGHT)
    # i = i + 1
    # print('total: ' + str(i) + 'times option')
    elem.send_keys(Keys.DOWN)
    # i = i + 1
    # print('total: ' + str(i) + 'times option')
    elem.send_keys(Keys.LEFT)
    # i = i + 1
# print('total: ' + str(i) + 'times option')
