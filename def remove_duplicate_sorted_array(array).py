def remove_duplicate_sorted_array(array):
    for i in range(len(array)):#O(n^2)
        for j in range(i+1,len(array)):
            if array[j] is not '_':
                if array[i] in array[j:len(array)]:
                    array[j]='_'
    k=0
    for i in range(len(array)):#O(n)
        if(array[i]!='_'):
            array[k]=array[i]
            k+=1    
    for i in range(k,len(array)): #O(n)
        array[i]='_'
    return k,array
a,b=remove_duplicate_sorted_array([0,1,1,1,2,2])
print(a)
print(b)
'''
total time complexity O(n^2)+O(n)+o(n)~O(n^2)

'''