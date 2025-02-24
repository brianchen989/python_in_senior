#檔案讀取\寫入
#open("檔案路徑",mode="開啟模式")


#絕對路徑 ex:C/Users/brian_oxfujdl/OneDrive/桌面.txt("\"要改成"/"且最後加檔案種類")
#相對路徑(以程式路徑做延伸)  ex:123.txt 

#mode="r"讀取
#mode="w"複寫
#mode="a"加東西
#file = open("123.txt",mode="r")
#print( file.read() )
#print( file.readline() )
#readline讀一行
#for line in file:
   # print (line)
#file.close()
#記得關檔案，站電腦資源
#encoding="utf-8"中文模式
file = open("123.txt",mode="w",encoding="utf-8")
file.write("Hello") 
file.close()
file = open("123.txt",mode="a",encoding="utf-8")
file.write("  \n你好") 
file.close()
with open("123.txt",mode="a",encoding="utf-8") as file:
    file.write("  \n哈") 
