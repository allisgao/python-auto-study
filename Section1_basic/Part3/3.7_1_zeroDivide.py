#coding = utf-8
def spam(divideBy):
#    return 42 / divideBy
    try:
        return  42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))