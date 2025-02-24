
#if
#1
hungry=True
if hungry:
    print("餓")
#2
virus=True
if virus :
    print("線上上課")
else:
    print("學校上課")
#如果...就
#否則如果...就
#否則如果...就
#否則如果...就
#否則
score=100
if score==100:
    print("獎賞1000元")
elif score>=80:
    print("獎賞800元")
elif score>=60:
    print("獎賞100元")
else:
    print("懲罰")
 #如果...且...就  if ...and...:
 #如果...或...就  if ...or...:
 #不相等!=
#num=1
#abc=True
 #if  num==1 or not(abc):
    #print("獎賞100元")
#else:
    #print("懲罰")
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif  num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(10,11,12) )
