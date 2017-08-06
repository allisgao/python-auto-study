#coding = utf-8
#定义函数
'''
#一个成功的案例
import sys
def collatz(number):
    print(number)
    if number == 1:
        sys.exit()
    elif number % 2 == 1:
        t = number * 3 + 1
        collatz(t)
    else:
        t = number // 2
        collatz(t)


if __name__ == '__main__':
    n = input('Enter number: ')
    try:
        n = int(n)
        collatz(n)
    except ValueError as verror:
        print('ValueError: You need input digital.')
'''

'''


'''



def collatz(number):
    result = int(number) % 2
    if result == 0:
        print(str(int(number//2)))
    else:
        print(str( 3 * int(number) + 1))
## 开始调用
print('Enter number:')
num = int(input())

