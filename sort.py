def sort(arr):
    if len(arr)>1:
        l_arr=arr[:len(arr)//2]
        r_arr=arr[len(arr)//2:]
        #recursion
        sort(l_arr)
        sort(r_arr)
        print(r_arr)
        #merge
        i=0  #leftarr
        j=0  #rightarr
        k=0  #merged array index
        while i<len(l_arr) and j<len(r_arr):
            if l_arr[i]<r_arr[j]:
                arr[k]=l_arr[i]
                i+=1
            else:
                arr[k]=r_arr[j]
                j+=1
            k+=1
        while i<len(l_arr):
            arr[k]=l_arr[i]
            i+=1
            k+=1
        while j<len(r_arr):
            arr[k]=r_arr[j]
            j+=1
            k+=1
arr_test=[5,1,6,6,6,0,2,8]
sort(arr_test)