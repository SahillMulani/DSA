from sys import maxsize

nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = 0 
maxSum = -maxsize - 1


for i in range(len(nums)):
    
    sum = sum + nums[i]
    if (maxSum < sum):
        maxSum = sum
    if sum < 0 :
        sum = 0
    

print(maxSum)