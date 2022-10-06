class TimeMap:

    def __init__(self):
        self.value_dict = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[(key,timestamp)] = value
    def get(self, key: str, timestamp: int) -> str:
        while timestamp > 0:
            try:
                return self.value_dict[(key,timestamp)]
            except:
                timestamp -= 1
        return ""