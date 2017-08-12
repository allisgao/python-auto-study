#coding = utf-8
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

#print(count)
print('pprint输出')
pprint.pprint(count)
print('----------------------')
print('pformat输出')
p_format = pprint.pformat(count)
print(p_format)





