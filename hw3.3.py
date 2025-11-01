#lst = [1, 2, 3, 4, 5, 6] #[[1, 2, 3], [4, 5, 6]]
#lst = [1, 2, 3] # [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5] # [[1, 2, 3], [4, 5]]
#lst = [1] # [[1], []]
lst = [] #[[], []]

if len(lst) <= 3:
    result = [lst[:2], lst[2:]]
    print(result)
else:
    result = [lst[:3], lst[3:]]
    print(result)