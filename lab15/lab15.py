def MergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        #dawtagdana
        MergeSort(left)
        MergeSort(right)

        # k-erembelsn jagsaalt index
        # i - left
        # j - right
        k,i,j = 0,0,0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i+=1
            else:
                myList[k] = right[j]
                j+=1

        while i < len(left):
            myList[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            myList[k] = right[j]
            j+=1
            k+=1

# run - python .\lab15.py
lst = [11,2,34,5,32,5,101,44,53,99]
print("Эрэмблээгүй жагсаалт:")        
print(lst)
MergeSort(lst)
print("Эрэмблэгдсэн жагсаалт:")
print(lst)