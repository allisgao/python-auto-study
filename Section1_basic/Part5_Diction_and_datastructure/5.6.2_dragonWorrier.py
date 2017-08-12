#coding = utf-8
#stuff = {'roup':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    # My codes here:
    ### 这里，先将列表“addedItems”进行统计，并将统计结果“项目： 个数”键值对写入newUpdate键值对中
    newUpdate = {}
    for i in addedItems:
        newUpdate[i] = addedItems.count(i)
    ###
    #将新生成的字典中的数据与原始数据放在一块统计
    for k,v in newUpdate.items():
        if k in inventory.keys():
            inventory[k] += v
        else:
            inventory[k] = v
    return inventory

#初始时候的装备
inv = {'gold coin':42, 'rope':1}
#怪龙掉落
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

