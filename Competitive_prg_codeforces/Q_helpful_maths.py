s=input()
if len(s)==1:
    print(s)
else:
    lt=list(map(int,s.split("+")))#splits the input by + and map them as integers
    lt.sort()
    print("+".join(map(str,lt))) #maps the each element in lt as string and joins them using +