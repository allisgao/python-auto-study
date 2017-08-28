#coding = utf-8
#定义函数
def collatz(number):
    if number == 1:
        return number
    elif number % 2 ==0:
        return number // 2
    else:
        return 3 * number + 1

#开始调用
print('Enter number:')
''''''
try:
    num = int(input())
except ValueError:
    print('Please input an integer.')
    exit()

while True:
    if num != 1:
        num = collatz(num)
    else:
        break
    print(str(num))

