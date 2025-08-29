# def shuffle(array,n):
#     index=n
#     for i in range(1,n):
#         print(i)
#         array[i],array[index]=array[index],array[i]
#         index+=1
#     return array
# print(shuffle([1,2,3,4,4,3,2,1],4))



def shuffle(array, n):
    # Create a copy to avoid modifying during iteration
    temp = array[:]
    # Shuffle in-place using static array indexing
    for i in range(n):
        array[2*i] = temp[i]        # Place first half elements at even indices
        array[2*i + 1] = temp[i + n] # Place second half elements at odd indices
    return array

print(shuffle([2,5,1,3,4,7], 3))