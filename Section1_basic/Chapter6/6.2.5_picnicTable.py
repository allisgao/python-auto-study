#coding = utf-8
def printPincic(itemsDict, leftWidth, rightWidth):
    #输出标题，居中，空余用“-”填充
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        #key左对齐，value右对齐，这样看起来很工整
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
printPincic(picnicItems,12,5)
printPincic(picnicItems,20,6)












