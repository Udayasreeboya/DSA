# a="dfa12312afg"
# l=[]
# for i in a:
#     if i.isdigit():
#         l.append(int(i))
# # l=list(sorted(set(l)))
# # print("max2:", l[-2])




# def sec_max(l):
#     max=-1
#     max2=-1
#     for i in l:
#         if int(i) > max and int(i) > max2:
#             max2=max
#             max=int(i)
#         if max>int(i)>max2:
#             max2=int(i)
#     return max2
# print(sec_max(l))


# l=[1,1,2]
# res=[]
# for i in l:
#     if i not in res:
#         res.append(i)
# print(len(res))



#revmove duplicated in a sorted list
def removeDuplicates(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            nums[i+1]=nums[j]
            i+=1
    return i+1
print(removeDuplicates([1,1,2,2,4,6,6]))



#find second max number if it is a digit
# s="abc12324fjh"
def secondmax(s):
    max=-1
    max2=-1
    for i in s:
        if i.isdigit():
            if max < int(i):
                max2=max
                max=int(i)
            elif max > int(i) > max2:
                max2=int(i)
    return max2
print(secondmax("abc12324fjh"))




    