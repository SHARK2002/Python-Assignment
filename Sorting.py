class Sort:


    def __init__(self,arr):
        self.array = arr;

    def bubble_sort(self):

        length=len(self.array)

        for i in range(length-1):

            flag = False

            for j in range (length-1-i):

                if self.array[j]>self.array[j+1]:
                
                    temp = self.array[j]
                    self.array[j]= self.array[j+1]
                    self.array[j+1]=temp
                    flag = True

            if not flag:
                break
    
        print(*self.array)


        
list=[1,234,4,1325]


obj1=Sort(list);


obj1.bubble_sort()











