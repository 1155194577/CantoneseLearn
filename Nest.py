def flatten(lst):
    ans = []
    for el in lst:
        if type(el) == list:
             for e in flatten(el):
                 ans.append(e)
        else:
            ans.append(el)
    return ans
