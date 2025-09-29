class MyStack:

    def __init__(self):
        self._list = []

    def push(self, x: int) -> None:
        self._list.append(x)

    def pop(self) -> int:
        if len(self._list) > 0:
            return self._list.pop()
        else:
            return None

    def top(self) -> int:
        if len(self._list) > 0:
            return self._list[-1]
        else:
            return None

    def empty(self) -> bool:
        return len(self._list) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
