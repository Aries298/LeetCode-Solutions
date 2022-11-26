class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        arr = self.getRow(rowIndex-1)
        new_arr = [arr[i]+arr[i+1] for i in range(len(arr)-1)]
        new_arr.insert(0,arr[0])
        new_arr.append(arr[-1])
        return new_arr