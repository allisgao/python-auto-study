#coding=utf-8
passwordFile = open('SecretPasswordFile.txt')
SecretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == SecretPassword:
    print('Access granted.')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on therir luggate.')
else:
    print('Access denied!')