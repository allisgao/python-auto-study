#! python3
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string. ')
    if width < 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Heigh must be greater than 2. ')
    print(symbol * width)   ##打印box的上边
    for i in range(height - 2):## 打印box的左右高
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)   ## 打印box的下边

for sym, w, h in (('*', 4, 4),('o', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

