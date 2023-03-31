"""
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def containsDuplicate(list) -> bool:

    nums.sort()
    for i in range(len(nums) - 1):
        if(nums[i] == nums[i+1]):
            return True

    return False


if __name__ == "__main__" :

    nums = [1,2,3,1]

    print(containsDuplicate(nums))