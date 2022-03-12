#q1 Largest among 3
a,b,c= map(int, input('enter numbers space seperated').split())
if a >= b and a >= c:
    print(a,'is maximum')
elif b >= a and b >= c:
    print(b,'is maximum')
elif c >= a and c >= b:
    print(c,'is maximum')
