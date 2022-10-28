from this import d


def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return (sum)


arr = []
a=int(input("Enter the first element of the array"))
b=int(input("Enter the second element of the array"))
c=int(input("Enter the third element of the array"))
d=int(input("Enter the fourth element of the array"))
arr = [a,b,c,d]
n=len(arr)
ans=_sum(arr)
print('Sum of the array is',ans)