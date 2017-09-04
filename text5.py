import random
i=0

while(i<=100):
    n=input("press r to roll a dice:")
    if(n=='r'):
        r=random.randint(1,6)
        i=i+r
        print("u got r",r)
        print("ur position is" ,i) 
