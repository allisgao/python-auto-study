#!python3
#pw.py - an insecure password locker program.

PASSWORDS = {
	'email':'23rtye44rfre',
	'blog':'2434rt54yyered',
	'luggage':'12345'
}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit

account = sys.argv[1]  #first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)






