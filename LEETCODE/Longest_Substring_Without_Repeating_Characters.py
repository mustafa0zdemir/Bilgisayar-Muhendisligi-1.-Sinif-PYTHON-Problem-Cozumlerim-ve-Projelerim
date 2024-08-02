
def longsub(kelime):
    liste1=""
    liste2=""
    for i in range(len(kelime)):
        if kelime[i] not in liste1:
            liste1+=kelime[i]
        else:
            if len(liste1)>len(liste2):
                liste2 = liste1
                liste1 = ""
                liste1 += kelime[i]
            else:
                liste1=""
    
    return len(liste2)

print(longsub("bbbbb"))
print(longsub("abcabcbb"))
print(longsub("pwwkew"))



# leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
