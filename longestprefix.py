def lp(str):
    a=" "
    for i in range(len(str[0])):
        for j in str:
            if  i==len(j) or j[i] != str[0][i]:
                return a
        a+=str[0][1]
    return a
l=["flower","flow","flight"]
wl=["dog","racecar","car"]
w1=["wb","a"]
output=lp(l)
print(output)

                