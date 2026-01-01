import timeit

def BubbleSort(lst):
    swapped = True
    time = 0

    while(swapped):
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                swapped = True
                time = time + timeit.timeit()

        print(time)

lst = [11,2,34,5,32,5,101,44,53,99]
print("Эрэмблээгүй жагсаалт:")        
print(lst)
BubbleSort(lst)
print("Эрэмблэгдсэн жагсаалт:")
print(lst)