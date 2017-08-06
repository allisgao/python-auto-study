#coding = utf-8
def spam():
    global eggs
    eggs = 'spam'
    print('This is from function spam,   eggs = '+eggs)

eggs = 'global'
spam()
print(eggs)

'''
该示例中，
函数下面的语句顺序不同，输出结果也不同。
spam函数在这里重新定义了eggs，所以下面的print才会输出重新定义后的值。
'''