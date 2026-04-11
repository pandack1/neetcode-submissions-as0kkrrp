# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs) - 1
        return self.qsort(pairs, s, e)

    def qsort(self, arr, s, e):
        if e-s+1 <=1:
            return arr
        
        left = s
        pivot = arr[e]
        
        for i in range(s, e):
            if arr[i].key < pivot.key:
                temp = arr[i]
                arr[i] = arr[left]
                arr[left] = temp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.qsort(arr, s, left-1)
        self.qsort(arr, left+1, e)

        return arr