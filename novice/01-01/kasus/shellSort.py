def shellSort(list): 
    sublist = len(list)//2
    while sublist > 0: 
        for i in range(sublist): 
            temp = list[i] 
            j = i 
            while  j >= sublist and list[j-sublist] >temp: 
                list[j] = list[j-sublist] 
                j -= sublist 

            list[j] = temp 
        sublist //= 2