#猜數字遊戲
from tkinter.messagebox import NO


secret_num = 79
guess_num = None
guess_count = 0
guess_limit = 3
out_of_limit =False
while guess_num != secret_num and not (out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess_num = int(input("輸入數字"))
        if secret_num > guess_num:
            print("大一點")
        elif secret_num < guess_num:
            print("小一點")
    else:
        out_of_limit =True
if out_of_limit :
    print("失敗")
else:
    print("猜對了")
