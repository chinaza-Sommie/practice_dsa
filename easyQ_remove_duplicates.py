def removeDuplicates(nums):
    # step 1 -> go through the array nums
    # step 2 -> get the number of items in array
    # step 3 -> get elements in the array (without duplicates)
    # return -> number of unique elements, the elements in the array (_ for dup.)

    newArray = []
    # inputLength = len(nums)
    for i in nums:

        if i not in newArray:
            newArray.append(i)
            # print(type(i))

    return type(newArray),newArray

print(removeDuplicates([1,1,2]))
