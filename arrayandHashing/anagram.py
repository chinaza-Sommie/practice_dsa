def isAnagram(s,t):
    """
        function to check for anagrams
        input: string
        output: boolean
    """
    s = sorted(s)
    t = sorted(t)

    return s == t