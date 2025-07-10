
# #rotate array
# def reverse(lst, i, j):
#     while i < j:
#         lst[i], lst[j] = lst[j], lst[i]
#         i += 1
#         j -= 1
# lst = [1, 2, 3, 4, 5, 6, 7]
# n = len(lst)
# k = 3 %n 
# reverse(lst, 0, n - 1)
# reverse(lst, 0, k - 1)
# reverse(lst, k, n - 1)
# print(lst)

# # check if array is sorted and rotated
# arr=[3,4,5,1,2,3,7]
# count=0
# n=len(arr)
# for i in range(0,n):
#     if arr[i]>arr[(i+1)%n]:
#         count+=1
# if count==1:
#     print(True)
# else:
#     print(False)


lst=[0,1,1,0,1,1,1,1,0,0,1]
n=len(lst)
count=0
max_count=0
for i in range(n):
    if lst[i]==1:
        count+=1
        if max_count < count:
            max_count=count
    else:
        count=0
print(max_count)

