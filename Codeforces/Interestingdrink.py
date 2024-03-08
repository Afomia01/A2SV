def binarySearch(low, high, coins):
    while low<= high:
        mid= (low+ high)//2
        if coins >= prices[mid]:
            low= mid+1
        else:
            high= mid-1
    return low
 
n= int(input())
prices= list(map(int, input().split()))
prices.sort()
days= int(input())
 
for _ in range(days):
    coins= int(input())
    val= binarySearch(0, len(prices)-1, coins)
    print(val)