import sys

#print(sys.argv)

n = sys.argv[1]

count = len(n)
mid = count//2
pal = 0

for i in range(0,mid):
    if(n[i] == n[count-1-i]):
        pal += 1
        

#print(mid,pal)
if(pal==mid):
    print("Palindrome")
else:
    print("Not Palindrome")