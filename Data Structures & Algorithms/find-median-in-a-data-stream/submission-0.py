class MedianFinder:

    def __init__(self):
        self.max_heap =[]
        self.min_heap =[]

    def push_max_heap(self,num):
        heapq.heappush(self.max_heap,-num)

    def push_min_heap(self,num):
            heapq.heappush(self.min_heap,num)   

    def get_top_min_heap(self):
         return self.min_heap[0]

    def get_top_max_heap(self):
         return -self.max_heap[0]

    def extract_top_max_heap(self):
        return -heapq.heappop(self.max_heap)
   
    def extract_top_min_heap(self):
        return heapq.heappop(self.min_heap) 

    def check_balance(self):
         diff = len(self.min_heap) - len(self.max_heap)

         if abs(diff) > 1:
              return False
         
         return True

    def make_balance(self):
         if len(self.max_heap) > len(self.min_heap):
             self.push_min_heap(self.extract_top_max_heap())
         else:
              self.push_max_heap(self.extract_top_min_heap())     
                   
    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
             self.push_max_heap(num)
        elif num <= self.get_top_max_heap():
              self.push_max_heap(num)
        else :
            self.push_min_heap(num)   

        is_balance =  self.check_balance()    
        if not is_balance:
            self.make_balance()
               
    def findMedian(self) -> float:

        if len(self.min_heap) > len(self.max_heap):
             return self.get_top_min_heap()
        if len(self.max_heap) > len(self.min_heap):
             return self.get_top_max_heap()
  
        return (self.get_top_max_heap() + self.get_top_min_heap() )/ 2