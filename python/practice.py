from question import Question

test = [
    "1+3=?\n(a) 2 \n(b) 3 \n(c) 4 \n\n ",
    "1+5=?\n(a) 6 \n(b) 3 \n(c) 4 \n\n",
    "1+4=?\n(a) 2 \n(b) 3 \n(c) 5 \n\n"
]


questions = [
    Question(test[0],"c"),
    Question(test[1],"a"),
    Question(test[2],"c")
]
def run_test(questions):
    score = 0
    for qquestion in questions :
        answer = input(qquestion.description)
        if answer ==  qquestion.answer:
            score+=1
    print("你得到"+str(score)+"分")

run_test(questions)
