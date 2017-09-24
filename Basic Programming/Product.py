N=int(raw_input())

numArray = map(int, raw_input().split())
prod=1
for i in range(0,N):
    prod=prod*numArray[i]

prod=prod % (pow(10,9)+7)

print prod