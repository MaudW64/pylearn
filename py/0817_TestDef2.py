def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n,m%n)

r=gcd(30,24)
if r==1:
    print('互質')
else:
    print('最大公因數：',r)
