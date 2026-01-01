import timeit

def bubbleSort(lst):
    time =0
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[i]:
                #swap
                lst[j],lst[i]=lst[i],lst[j]
                time = time +timeit.timeit()

        print(time)

lst = [11,2,34,5,32,5,101,44,53,99]
print("Эрэмблээгүй жагсаалт:")        
print(lst)
bubbleSort(lst)
print("Эрэмблэгдсэн жагсаалт:")
print(lst)