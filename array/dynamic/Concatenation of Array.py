def Concatenation_of_Array(array):
    for i in range(len(array)):
        array.append(array[i])
    return array
print(Concatenation_of_Array([1,2,3]))