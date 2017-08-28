#! python3
# phoneAndEmail.py - Finds phone number and email addresses on the clipboard.
## 为了方便，暂时不考虑分机
# 电话号码的正则表达式
import pyperclip, re
# 外国电话号码示例：415-555-9999
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?      # 区号，格式为(000)或000。“?”表示出现0次或1次
    (\s|-|\.)?              # 分隔符，空格/-/.，即区号与电话号码之间的连接
    (\d{3})                 # 号码前3位
    (\s|-|\.)               # 与后面几位的连接
    (\d{4})                 # 最后4位
    #(\s*(ext|x|ext.)\s*(\d{2,5}))?  # 扩展。分机？？
    ''', re.VERBOSE)        # re.VERBOSE -- 处理复杂表达式的参数。

# Create Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #用户名
    @                       #符号
    [a-zA-Z0-9.-]+          #域名
    (\.[a-zA-Z]{2,4})       #点后面的其他东西
    )''',re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    # 将检索到的电话号码格式化，格式：000-000-0000
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # groups[]:  1,区号；2，区号和号码见的连字符；3，号码前3位；4，号码间的连字符；5，号码后4位；678应该是后面的分机。这些旧不太明白了。
    # 考虑到还有分机的情况
    '''
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
     '''
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    # 邮箱就不用像电话号码那样格式化了
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
else:
    print('No phone numbers or email addresses found. ')
















