class TimeMap:

    def __init__(self):
        self.keyMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyMap:
            self.keyMap[key].append([timestamp, value])
        else:
            self.keyMap[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
        
        values = self.keyMap[key]
        start = 0
        end = len(values)-1

        print (values)
        while end >= 0:
            if timestamp >= values[end][0]:
                return values[end][1]
            end -= 1
        return ""


        
        
