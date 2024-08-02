
def addtwonumber(l1,l2):
    num1 = ""
    num2 = "" 
    top = 0
    liste = []
    l1.reverse()
    l2.reverse()
    for i in range(len(l1)):
        num1 += str(l1[i])
    for i in range(len(l2)):
        num2 += str(l2[i])
    top = int(num1) + int(num2)
    for j in range(len(str(top))):
        liste.append(int(str(top)[j]))
    liste.reverse()
    return liste

print(addtwonumber([9,9,9,9,9,9,9],[9,9,9,9]))
print(addtwonumber([2,4,3],[5,6,4]))
print(addtwonumber([0],[0]))

#leetcode: https://leetcode.com/problems/add-two-numbers/description/ 

