#for迴圈


#for變數in字串或列表
#要重複執行的程式碼
#for letter in "你好":
    #print(letter)
#for num  in [1,2,3,4,5,6,7,8]:
    #print(num)
#for num  in range(5):
    #print(num)
def power(base_num,power_num):
    result = base_num
    for index in range(power_num-1):
        result = result * base_num
    return result


print(pow(2,5))