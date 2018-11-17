# https://www.codechef.com/problems/PRDRG
# https://en.wikipedia.org/wiki/Jacobsthal_number

# numerator series follows jacobsthal number series



def jacobsthal_no(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return (jacobsthal_no(n-1)+ 2*jacobsthal_no(n-2))



t=list(map(int,input().strip().split()))

for n in t[1:]:
   print(jacobsthal_no(n),pow(2,n),end=" ")

