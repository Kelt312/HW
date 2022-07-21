
def Levy(s,t):
    n,m = len(t), len(s)
    v0= [0]*(n+1)
    v1= [0]*(n+1)

    for i in range(n):
        v0[i] = i
    for i in range(m):
        v1[0] = i+1
        for j in range(n):
            delCost = v0[j+1]+1
            insCost = v1[j]+1
            if s[i] == t[j]:
                subCost = v0[j]
            else:
                subCost = v0[j]+1

            v1[j+1]=min(delCost, insCost, subCost)

        v0,v1=v1,v0

    return v0[n]

if __name__ == "__main__":
     pairs=[
        ('лена', 'лень'),
        ('satuday','sunday'),
        ('море','гора'),
        ('компьютер','компьютеризация'),
        ('компьютер','компьютеры'),
        ]
     from Levenshtein import distance
     for s,t in pairs:
        print(s, t, Levy(s,t), distance(s,t))
