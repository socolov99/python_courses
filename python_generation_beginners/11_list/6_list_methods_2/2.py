# put your python code here
arr = [int(i) for i in input().split()]
index_of_max_el = arr.index(max(arr))
index_of_min_el = arr.index(min(arr))
arr[index_of_max_el], arr[index_of_min_el] = arr[index_of_min_el], arr[index_of_max_el]

print(*arr)
