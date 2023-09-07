class Screw:
    def __init__(self, Name, Weight):
        self.Name = Name
        self.Weight = Weight
    def __str__(self):
        return("(" + self.Name + ", " + str(self.Weight) + ")")
    def __repr__(self):
        return("(" + self.Name + ", " + str(self.Weight) + ")")
    
class ScrewList:
    def __init__(self):
        self.arr = []

    def add(self, Screw):
        self.arr.append(Screw)
        self.insertion_sort()
        index = self.binarysearch(self.arr, 0, len(self.arr), Screw.Weight)
        print("_______________________________________________________________________________")
        print(self)
        print("Placement Index: " + str(index))
        print("Placed Between " + str(self.get(index - 1)) + " and " + str(self.get(index + 1)))
        print("_______________________________________________________________________________")

    def get(self, index):
        if index<0 or index >= len(self.arr):
            return None
        return self.arr[index]
    
    def binarysearch(self, arr, low, high, x):
        try:
            x = x.Weight
        except:
            pass
        if high >= low:
            mid = (high + low) // 2
            if arr[mid].Weight == x:
                return mid
            elif arr[mid].Weight > x:
                return self.binarysearch(arr, low, mid - 1, x)
            else:
                return self.binarysearch(arr, mid + 1, high, x)
        else:
            return -1
  
    def insertion_sort(self):
        i = len(self.arr) - 1
        val = self.arr[i]
        j = self.binarysearch(self.arr, 0, i-1, val)
        self.arr = self.arr[:j] + [val] + self.arr[j:i] + self.arr[i+1:]
        
    def __str__(self):
        return str(self.arr)
    
Screws= ScrewList()
while True:
    Screws.add(Screw(input("Name: "), float(input("Weight: "))))