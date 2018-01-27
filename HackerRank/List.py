
a = input()
l = []
for _ in range(int(a)):
    s=input().split()
    c=s[0]
    d=s[1:]
    if c != ("print"):
        c += "("+",".join(d) +")"
        eval("l."+c)
    else:
        print(l)
    