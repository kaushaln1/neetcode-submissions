class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()
        

    def findMedian(self) -> float:
        n = len(self.array)
        print(self.array, n)
        if n%2 == 0:
            return (self.array[n//2]+ self.array[(n//2)-1])/2
        
        index =(n//2)+1
        return self.array[index-1]
        
        