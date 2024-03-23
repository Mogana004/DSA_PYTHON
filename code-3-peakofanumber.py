class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r= 0 ,len(nums)-1
        while l<r:
            mid = (l +r )//2
            if nums[mid]<nums[mid+1]:
                l=mid + 1
            else:
                r=mid
        return l



(OR)
N= int(input())
arr= list(map(int , input().split()))
peaks = []
for i in range(N):
    if i==0 and arr[i]> arr[i+1]:
        peaks.append(i)
    elif i==N-1 and arr[i] > arr[i-1]:
        peaks.append(i)
    elif arr[i]> arr[i-1] and arr[i]> arr[i+1]:
        peaks.append(i)
print(*peaks)
