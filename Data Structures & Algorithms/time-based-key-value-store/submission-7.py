class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.data.get(key):
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        
        if not self.data.get(key):
            return ""

        result = ""
        low, high = 0, len(self.data[key])

        while low < high:
            mid = low + (high - low) // 2
            prev_mid = mid

            if self.data[key][mid][1] == timestamp:
                return self.data[key][mid][0]
            elif self.data[key][mid][1] > timestamp:
                high = mid
            else:
                low = mid+1
                result = self.data[key][mid][0]

        return result


        

