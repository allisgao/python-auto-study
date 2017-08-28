#coding = utf-8
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
#    return eggs
spam()

bacon()
'''
注意：
函数spam中有调用函数bacon，但bacon函数实际上没有任何输出。
另：调用函数的本质是调用函数的运算结果/或者说是逻辑，故被调用的函数
'''