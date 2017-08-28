#!python3
# coding = utf-8
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()  # text变量中的内容来自剪贴板
# Separate lines and adds stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = "\n".join(lines)


pyperclip.copy(text)



"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""