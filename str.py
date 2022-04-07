def lenth_of_srtings(string1,string2):
    if len(string1)>len(string2):
        print(string1)
    elif len(string2)>len(string1):
        print(string2)
    elif len(string1)==len(string2):
        print(string1,string2)
lenth_of_srtings("hello","welcome")
lenth_of_srtings("sonu","monu")

b_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
c1 = 0
while c1 < len(b_list):
    c2 = 0
    while c2 < len(b_list[c1]):
        
        print (b_list[c1][c2])
        c2 = c2 + 1
    c1 = c1 + 1