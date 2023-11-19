# giving name(r and t) to functions 
from random import randrange as r 
from time import time as t

#asking user how many question and max number he wants by giving him input
no_question = int(input('How many questions do you want?: '))
max_num = int(input('Highest number used in practice?: '))

#creating a score variable which which will tell the score
score = 0
#creating answer list for checking how many answers are correct
answer_list = []

#creating a timer variable which will tell how much time it took to complete the test
start = t()

#creating for loop for the solution, giving no_question short name q 
for q in range(no_question):
#creating two numbers which will give questions to user according to q he asks
    num1,num2 = r (1,max_num+1),r(1,max_num+1)
#creating ans variable which will give num1 X num2, for ex(5 X 1 = )
    ans = num1 * num2
#creating u_ans which will multiply and give the ans
    u_ans = int(input(f'{num1} X {num2} = '))
#answer list which will check if the ans given by user is correct, along with the users ans this will show the correct ans
    answer_list.append(f'{num1} X {num2} = {ans} you: {u_ans}')
#creating if statement for checking if user ans is equal to computer ans then the score will increase by 1 
# in the end it will tell the amount of time taken by user to answer the question
    if u_ans == ans:
        score += 1
    end = t()
    
#creating a print which will calculate and show the user all the question he answered together with the percentage 
print(f'Thankyou for playing! \nYou got {score} out of {no_question}({round(score/no_question*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_question,1)}seconds/question)')

#giving answer_list name as a
for a in answer_list:
    print(a)