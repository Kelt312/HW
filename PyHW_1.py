#1
print(sum(range(0,88888889)))
#2
x=[3,4,56,100,2,2,3]
from statistics import mean
print("Среднее=",mean(x))
#3
st=['a','s','d','x','f','g','h','y','x','y','x']
for i in range(0,len(st)):
	if st[i]=='x':
		st[i]='y'
print("".join(st))
#4
sp=[3,4,56,100,15,2,20,30]
#sp=(3,4,56,100,2,20) #проверочный список
p=1
for n in sp:
    if (n%3==0) and (n%5==0):
        p=p*n
if p!=1:
    print("Произведение чисел кратных 3 и 5 =", p)
else:
    print("Нет чисел кратных 3 и 5")
#5
string="asdxfghyxyx"
string=string.replace('x','y')
print(string)

