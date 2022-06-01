class Sort:


    def __init__(self,arr):
        self.array = arr

    def selection_sort(self):

        length=len(self.array)

        for i in range(length-1):


            j=i+1

            min_index = i
            while(j<length):
                

                if self.array[min_index]>self.array[j]:

                    min_index=j

                j+=1


            temp = self.array[i]
            self.array[i]= self.array[min_index]
            self.array[min_index]=temp

            
        return self.array
    


        
list=[1,234,4,1325]


obj1=Sort(list);




print(obj1.selection_sort())











