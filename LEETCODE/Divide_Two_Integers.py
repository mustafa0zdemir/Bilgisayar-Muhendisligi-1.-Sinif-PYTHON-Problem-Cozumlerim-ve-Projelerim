
def ikitamsayibol(bölünen , bölen):
    ilkbölünen = bölünen
    ilkbölen = bölen
    deger = 0
    while abs(bölünen) > abs(bölen):
        bölünen = abs(bölünen)
        bölünen -= abs(bölen)
        deger += 1
    
    if ilkbölünen > 0 and ilkbölen < 0 or ilkbölünen < 0 and ilkbölen > 0 :
        
        return -deger
    else:
        return deger
   

print(ikitamsayibol(7,-3))
print(ikitamsayibol(10,3))

# leetcode: https://leetcode.com/problems/divide-two-integers/description/

