# https://www.codechef.com/problems/MINDSUM
# https://www.youtube.com/watch?v=vJ9LF0h-N1g



def digit_sum(n):
    s=0

    while(n>0):
        s+=n%10
        n=n//10

    return s


t=int(input())
for tt in range(t):
    n,d=map(int,input().split())

    dict={}
    queue=[]
    seq=0

    queue.append((n,seq))
    dict[n]=0

    while(len(queue)>0 and seq<1000):

        n,seq=queue.pop(0)
        seq+=1

        x=digit_sum(n)
        if not x in dict:
            dict[x]=seq
            queue.append((x,seq))
        
        queue.append((n+d,seq))


    ans=min(dict)
    print(ans,dict[ans])
