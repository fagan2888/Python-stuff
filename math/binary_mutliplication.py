def multiply(a, b):
    t = 0
    while a != 0:
        if a & 1 == 1:
            t += b
        a = a>>1 
        b = b<<1
    return t

def divise(a, b):
    m = 0
    t = 0
    while t <=  a:
        m += 1
        t = multiply(b, m)
    return m-1

def remainder(a, b):
    m = 0
    t = 0
    while t <= a:
        m += 1
        t = multiply(b, m)
    t = t - b
    return a - t

def convert(num, degree, new_num=[0]):
    if num <= 1:
        return new_num
    pos = 0
    print(num, degree)
    new_num[pos] = int(remainder(num, degree))
    new_num.insert(0, int((num - new_num[pos])/degree))
    return convert(new_num[pos], degree, new_num)

