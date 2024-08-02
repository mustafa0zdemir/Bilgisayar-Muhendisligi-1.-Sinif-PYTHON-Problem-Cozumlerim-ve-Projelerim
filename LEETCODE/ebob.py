
def ebob(x,y):
    if x%y == 0:
        return y
    if y%x == 0:
        return x
    if x < y:
        return ebob(int(y%x),y)
    else:
        return ebob(x,int(x%y))
    

