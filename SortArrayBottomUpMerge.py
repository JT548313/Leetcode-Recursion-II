class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = [[n] for n in nums]
        while len(prev) > 1:
            cur = []
            for i in range(0, len(prev), 2):
                cur.append(self.merge(prev[i], prev[i + 1] if i + 1 < len(prev) else []))
            prev = cur
        return prev[0]

    def merge(self, l1, l2):
        merged = []
        i1 = i2 = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] < l2[i2]:
                merged.append(l1[i1])
                i1 += 1
            else:
                merged.append(l2[i2])
                i2 += 1
        merged.extend(l1[i1:])
        merged.extend(l2[i2:])
        return merged

nums = [5,2,3,1]
s= Solution()
print(s.sortArray(nums))