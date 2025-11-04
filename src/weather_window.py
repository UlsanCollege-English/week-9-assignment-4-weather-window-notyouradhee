"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""
import heapq
def sliding_window_max(nums, k):
    # TODO:
    # Use a max-heap via (-value, index).
    # Push current item; pop while top index <= i - k (out of window).
    # When i >= k-1, record current window max as -heap[0][0].
    # Handle k <= 0, empty list, and k > len(nums).
    if k <= 0 or not nums:
        return []
    if k > len(nums):
        return [max(nums)]
    if k == 1:
        return nums[:]

    heap = []
    result = []

    for i, num in enumerate(nums):
        heapq.heappush(heap, (-num, i))

        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            result.append(-heap[0][0])

    return result
