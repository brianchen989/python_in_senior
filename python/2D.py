#二維列表(列表包列表)3維3層四維四層 巢狀迴圈(迴圈包迴圈)
#row行
#column列
nums =[
    [0,1,2,3,4,],
    [5,6,7,8,9],
    [10]
    ] 
#print (nums[0][1])
#print (nums[第幾列][第幾行])
for row in nums:
    for col in row:
        print(col)
#for row in nums:[
# [],[],[]
# ]變[][][]
    #for col in row:[a,b,c]變a,b,c
        #print(col)