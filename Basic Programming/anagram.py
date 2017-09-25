
N=int(raw_input())
for x in range(0,N):
 A=list(raw_input())
 B=list(raw_input())
 countA=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 countB=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



 for i in range(0,len(A)):
    countA[ord(A[i])-ord('a')]=countA[ord(A[i])-ord('a')]+1

 for i in range(0,len(B)):
    countB[ord(B[i])-ord('a')]=countB[ord(B[i])-ord('a')]+1

 res=0
 for i in range(0,26):
    res=res+ abs(countA[i]-countB[i])

 print res