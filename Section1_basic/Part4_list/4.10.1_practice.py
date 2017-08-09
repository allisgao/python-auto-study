#coding = utf-8
#定义函数
def myFunc(mytest):
    long_str = ''
    my_length = int(len(mytest))
    for i in range(0,my_length - 1):
        long_str = long_str  + mytest[i]+ ' '
    print(long_str + 'and ' + mytest[-1])

#调用函数
spam = ['apples', 'bananas', 'tofu', 'cats', 'good']
myFunc(spam)





