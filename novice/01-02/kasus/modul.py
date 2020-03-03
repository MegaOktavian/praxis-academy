import bubbleSort
import selectionSort
import insertSort
import shellSort
import mergeSort


list = [2,5,60,43,27,10,89,17]
print('\nData yang akan di sort :\n', list )
print('\nBubble Sort :\n')
bubbleSort.bubbleSort(list)
print("\n==================================================\n")

print('\nSelection Sort :\n')
selectionSort.selectionSort(list)
print("\n==================================================\n")

print('\nInsert Sort :\n')
insertSort.insertionSort(list)
print("\n==================================================\n")

sublist = len(list)
shellSort.shellSort(list) 
print ("\nShell Sort :\n") 
for i in range(sublist): 
    print(list[i])
print("\n==================================================\n")

print('\nMerge Sort :\n')
mergeSort.mergeSort(list)
print("\n==================================================\n")