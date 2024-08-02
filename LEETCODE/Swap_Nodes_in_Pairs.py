
def swapPairs(Liste):
    for i in range(0,len(Liste)-1,2):
        tmp = Liste[i]
        Liste[i]=Liste[i+1]
        Liste[i+1]=tmp
    return Liste

print(swapPairs([1,2,3,4]))
print([])
print([1])
# leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/description/
