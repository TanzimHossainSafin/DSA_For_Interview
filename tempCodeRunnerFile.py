temp = array[:]
    # Shuffle in-place using static array indexing
    for i in range(n):
        array[2*i] = temp[i]        # Place first half elements at even indices
        array[2*i + 1] = temp[i + n] # Place second half elements at odd indices
    
    return array