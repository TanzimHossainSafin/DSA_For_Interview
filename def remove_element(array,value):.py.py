def remove_element(array,value):
        count=len(array)
        for i in range(len(array)):
                 if(array[i]==value):
                         array[i]='_'
                         count-=1
        first=0
        last=len(array)-1
        while(first<last):
                if(array[first]!='_'):
                        first+=1
                elif(array[last]=='_'):
                        last-=1
                else:
                        temp=array[first]
                        array[first]=array[last]
                        array[last]=temp
                        first+=1
                        last-=1
     
        return (array,count)
        
print(remove_element([0,1,2,2,3,0,4,2],2))