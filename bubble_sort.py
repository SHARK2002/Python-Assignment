def bubble_sort(array):

    length=len(array)

    for i in range(length-1):

        flag = False

        for j in range (length-1-i):

            if array[j]>array[j+1]:
                
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                flag = True

        if not flag:
            break
    
    return array



list=[1,2,3,4,5,6,7]

print(bubble_sort(list))