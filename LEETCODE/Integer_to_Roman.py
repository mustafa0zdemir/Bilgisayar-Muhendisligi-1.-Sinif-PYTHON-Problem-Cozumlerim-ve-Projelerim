
def intToRoman(sayi):
    degerler = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    semboller = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roma = ''
    if sayi <= 0:
        return roma
    for i in range(len(degerler)):
        while sayi >= degerler[i]:
            roma += semboller[i]
            sayi -= degerler[i]
    
    return roma

print(intToRoman(1994)) 
print(intToRoman(58))

# leetcode: https://leetcode.com/problems/integer-to-roman/description/