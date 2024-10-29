from heapq import heappush, heappop
class DualHeap:
    def __init__(self):
        self.Left = []
        self.Right = []
        self.__initialBuffer = []
    def __len__(self):
        return len(self.Left)+len(self.Right)
    def insert(self,v):
        if self.__initialBuffer is not None:#until the first two insertions
            if len(self.__initialBuffer) == 0:
                self.__initialBuffer.append(v)
            elif len(self.__initialBuffer) == 1:
                w = self.__initialBuffer[0]
                self.__initialBuffer = None
                self.Left.append(min(v,w)*-1)
                self.Right.append(max(v,w))
        else:#normal operation
            (L,R) = abs(self.Left[0]),self.Right[0]
            if L < v:
                self.__insertL(v)
            else:
                self.__insertR(v)
    def __insertL(self,v):
        heappush(self.Left, v*-1)
        self.__balance()
    def __insertR(self,v):
        heappush(self.Right, abs(v))
        self.__balance()
    def __balance(self):
        L,R = len(self.Left),len(self.Right)
        if L-1>R:
            self.__insertR(heappop(self.Left))
        elif R-1>L:
            self.__insertL(heappop(self.Right))
                
    def roots(self):
        return (abs(self.Left[0]),abs(self.Right[0]))
    def median(self):
        L,R = len(self.Left),len(self.Right)
        roots = self.roots()
        if(L>R):return roots[0]
        elif(R>L):return roots[1]
        else: return roots
    def __str__(self):
        val = ""
        for x in self.