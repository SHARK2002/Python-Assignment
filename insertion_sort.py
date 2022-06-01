class Sort:

    def __init__(self,arr):

        self.array = arr
    
    def insertion_sort(self,n):

        if n<=1:
            return

        self.insertion_sort(n-1)

        last = self.array[n-1]

        i = n-2

        while i>=0 and self.array[i]>last:

            self.array[i+1]=self.array[i]

            i-=1
        
        self.array[i+1]=last

        return self.array

        



list=[1,234,4,1325]


obj1=Sort(list);



print(obj1.insertion_sort(len(list)))

        



