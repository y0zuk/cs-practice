
tc=float(input())
n=int(input())
count_input=0
count_errors=0
count_upper=0
s=0
maxm=0

for i in range(n):
    a = input()
    if a=='error':
        count_errors+=1
    else:
        a=float(a)
        s += a
        if a>tc:
            count_upper+=1
            maxm=max(maxm,a)
print(n)
print(count_errors)
print(count_upper)
print(f"{maxm:.1f}")
print(f"{s/(n-count_errors):.1f}")

