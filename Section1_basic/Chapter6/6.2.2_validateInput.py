#coding = utf-8
while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please Enter a number for your age. ')
while True:
    print('Select a new password (letters and numbers only): ')
    passwd = input()
    if passwd.isalnum():
        break
    print('Passwords can only have letters and numbers.')









