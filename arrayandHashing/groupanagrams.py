def groupAnagrams(strs):
    """
        function to return a group of anagrams
        input: array of strings
        output: nested array of strings - [["x"]]
    """
        # loop through the arr
        # sort each word
        # check the ones that match
    data_storage = {}
    final_output = []

    for index, value in enumerate(strs):
        newvalue = tuple(sorted(value))
        if newvalue not in data_storage.keys():
            data_storage[newvalue] = [value]
        else:
            data_storage[newvalue].append(value)
        
    for values in data_storage.values():
        final_output.append(values)

    return final_output

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))