class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [""]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.arr[idKey-1] = value
        if idKey-1 == self.ptr:
            res = []
            while self.ptr<self.n and self.arr[self.ptr] != "":
                res.append(self.arr[self.ptr])
                self.ptr += 1
            return res
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)