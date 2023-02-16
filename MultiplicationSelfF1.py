

from random import seed, randint
seed()
import pprint as pp
count = 0
summary = []
correct_ans = 'correct'
wrong_ans = 'wrong!'
for n in range(1, 11):
    first = randint(1, 10)
    second = randint(1, 10)
    result = first * second
    question = (f"Question {n}: {first}*{second} = ?")
    print(question, end='')
    answer = input(' your answer is: ')
    try:
        int(answer)
    except ValueError:
        print('wrong!')
    else:
        if int(answer) != result:
            ans_status = wrong_ans
            print(ans_status)
        else:
            count += 1
            ans_status = correct_ans
            print(ans_status)
    summary.append(f'{question}; Student Answer: {answer} Answer: {first * second}; Status: {ans_status}')

if count >= 7:
    print('Good! The test is passed!')
else:
    print('The test is failed. U\'re able to do it better!')
    print('The quantity of right answers is: ', count)

summary = tuple(summary)
pp.pprint(summary)