#coding = utf-8
def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)