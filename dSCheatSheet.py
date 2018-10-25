import array

# Remeber range does not execute the last number
# range (0,3) = 0,1,2
def printArray(arr):
    lastIndex = len(arr);
    for i in range(0,lastIndex):
        print(arr[i],end = " ")
    print("\r")


arr = array.array('i',(1,2,3))
printArray(arr)
# using append() to insert new value at end
arr.append(4)
printArray(arr)
arr.pop(-1)
printArray(arr)
# using index() to print index of 1st occurrenece of 2
print ("The index of 1st occurrence of 2 is : ",end="")
print (arr.index(2))

#using reverse() to reverse the array
arr.reverse()
printArray(arr)
