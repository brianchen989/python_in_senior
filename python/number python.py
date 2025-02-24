#如何使用數字,數字的用法
print(77)
print(77.2)
print(-77.2)
print(8+7)
print(8-7)
print(8*7)
#小數除法/
print(8/7)
#整數除法//
print(8//7)
#先乘除後加減
print(8+7*7)
print((8+7)*7)
#運用變數
num=5
print(num*8)
#取餘數
print(8%7)
#str字串80="80"
num=-70
print(str(num))
#字串相加
print("教練,我想印數字"+str(num))
#數字和字串不能相加，ex:8+7=15  ,"8"+"7"="87" ,8+"7"=error

#abs 取絕對值
print(abs(num))
#pow(,)次方(2,4)=2*2*2*2
print(pow(2,4))
#max 回傳最大min回傳最小
print(max(2,4,88,55))
print(min(2,4,88,55))
#round四捨五入
print(round(4.4))
#模組引入
from math import *
#floor無條件捨去
print(floor(4.4))
#ceil無條件進位
print(ceil(4.4))
#sqrt開根號
print(sqrt(64))