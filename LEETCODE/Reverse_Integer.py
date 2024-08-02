
def reverse(x):
    y = x
    if x < 0:
        x = - x
    sayi = 0
    index = 10**(len(str(x))-1)
    liste = []
    while x > 0:
        son = x % 10
        liste.append(son)
        x = x // 10
    for deger in liste:
        sayi += deger * index
        index = index // 10
    if y < 0:
        sayi = -sayi
    return sayi


print(reverse(123))
print(reverse(-123))
print(reverse(120))


# leetcode: https://leetcode.com/problems/reverse-integer/