from random import seed, randint
seed()
count = 0
for n in range(1, 11):
    first = randint(1, 10)
    second = randint(1, 10)
    result = first * second
    print(f"Question {n}: {first}*{second} = ?", end='')
    answer = input(' your answer is: ')
    try:
        int(answer)
    except ValueError:
        print('wrong!')
    else:
        if int(answer) != result:
            print('wrong!')
        else:
            count += 1
            print('correct')
if count >= 7:
    print('Good! The test is passed!')
else:
    print('The test is failed. U\'re able to do it better!')
    print('The quantity of right answers is: ', count)
