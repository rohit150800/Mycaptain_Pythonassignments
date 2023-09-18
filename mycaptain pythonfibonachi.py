n=int(input("Enter the number of terms to be displayed : "))
n1=0        #initalization
n2=1
count=0
for i in range(n):#execution
    sum=n1+n2 #modification
    print(n1)
    n1=n2       #replaceing the numbers to add
    n2=sum
    count +=1   #incrementing