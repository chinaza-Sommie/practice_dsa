"""
            function the index positions of then numbers that sum up to the target provided
            input: array of numbers
            output: array (indices)
        """
        #  ------- BRUTE FORCE APPROACH -------
        # if nums == []:
        #     return "invalid input"

        # for num in range(len(nums)):
        #     for inner_num in range(num + 1,len(nums)):
        #         if (nums[num] + nums[inner_num]) == target:
        #             return [num, inner_num]
        # return "not valid"

        # loop through once.
        # use hashmap
        # subtract current value in array and check if it exists in the hashmap
        # if not add the current value and its index to the hasmap
        # if it does, return the array of the index of both numbers

        # O(1)
        if nums == []:
            return "invalid input"

        index_storage = {}

        # O(n)
        for index, value in enumerate(nums):
            secondvalue = target - value

            if secondvalue in index_storage:
                return [index_storage[secondvalue], index]

            index_storage[value] = index

        return "invalid input"