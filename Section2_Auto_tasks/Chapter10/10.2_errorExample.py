#! pyton3
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')
#bacon()
spam()

