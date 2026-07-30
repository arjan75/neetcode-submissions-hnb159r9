class TimeMap:

    def __init__(self):
        self.timestamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = [(timestamp, value)]
        else:
            self.timestamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timestamps:
            return ""

        timestamps = self.timestamps[key]
        left = 0
        right = len(timestamps)-1
        result = ""

        while left <= right:
            middle = (left+right)//2
            if timestamps[middle][0] <= timestamp:
                result = timestamps[middle][1]
                left = middle+1
            else:
                right = middle-1
        return result




        
