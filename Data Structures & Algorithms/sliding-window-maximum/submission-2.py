class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from q if q is not empty
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # add current value to q
            q.append(r)

            # if left most value is out of bounds, pop it
            if l > q[0]:
                q.popleft()

            # only if window size is >= k
            if (r + 1) >= k:
                # add the largest number to the output
                output.append(nums[q[0]])
                l += 1
            
            # r is incremented every iteration
            r += 1

        return output