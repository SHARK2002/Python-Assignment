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



list=[1234,1426,146,134,235,12461]

print(bubble_sort(list))