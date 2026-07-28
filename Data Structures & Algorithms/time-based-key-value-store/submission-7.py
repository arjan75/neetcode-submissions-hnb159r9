class TimeMap:

    def __init__(self):
        self.timestampValues = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestampValues:
            self.timestampValues[key] = [(timestamp, value)]
        else:
            self.timestampValues[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestampValues:
            return ""
        
        values = self.timestampValues[key]
        left = 0
        right = len(values)-1

        result = ""

        while left <= right:
            middle = (left + right) // 2
            if values[middle][0] <= timestamp:
                result = values[middle][1]
                left = middle + 1
            else:
                right = middle - 1
        return result

        
