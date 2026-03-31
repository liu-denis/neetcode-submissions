class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > max:
                temp = arr[i]
                arr[i] = max
                max = temp
            else:
                arr[i] = max
        arr[0] = max
        arr[-1] = -1
        return arr
        