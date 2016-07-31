def search(a,b,c):
    for i in range(int(a)-int(b),int(a)+int(b)+1):
        if i in c:
            return True
    return False
