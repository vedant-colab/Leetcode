def twosum(arr,target):
    ht = {}
    for i,val in enumerate(arr):
        r = target - val
        if r in ht:
            return[ht[r],i]
        
        ht[val] = i
