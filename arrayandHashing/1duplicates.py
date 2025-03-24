def findDuplicates(nums):
    """
            input: array nums
            output: boolean

        """
    if nums == []:
        return "list is empty"
            
    newSet = set(nums)

    if len(newSet) == len(nums):
        return False
    else:
        return True


print(findDuplicates([1,2,3,3]))
print(findDuplicates([1,2,3,4]))
print(findDuplicates([]))