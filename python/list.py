#list列表,以及用法(可放數字\字串\布林值)
scores=[90,70,60,50,80]
print(scores)
friends =["小黑","小白","小黃","小紅"]
print(friends)
things=[90,"小黑",True]
print(things)
#print(things[?])  ?=提取第幾位
print(things[2])
print(things[0])
#倒數用負的
print(things[-1])
print(scores[0:2])
#第0個到第2個之前(不包括第2位)
print(scores[1:4])
print(scores[1:])
print(scores[:4])
phrase="Hello Mr.MRC"
#       0123456789
print(phrase[:5])
scores[0] = 30
#改數字
print(scores)
scores.extend(friends)
#.extend延伸
print(scores)
scores.append(3)
#.append加值
print(scores)
scores.insert(3,30)
#.insert(x,y)在x插入y
print(scores)
scores.remove(70)
#.remove消除
print(scores)
scores.clear()
#.clear清空列表
print(scores)
friends.pop()
#.pop消除最後一位
print(friends)
#sort作排列(小到大)
#reverse列表反轉
#print(scores.index(70))會抓出70位置給你
#count數有幾個值
