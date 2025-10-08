def euclid(a, b):
    r = a % b
    if(r == 0):
        print(b)
        return b
    euclid(b , r)


euclid(35, 15)
euclid(100, 25)
euclid(81, 27)
euclid(56, 42)
euclid(17, 13)