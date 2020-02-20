import random
import time
print('welcome to math O python version!')
time.sleep(5)
print('you will answer 12 random multiplication questions.')
time.sleep(5)
print('have fun!')
time.sleep(5)
print('*do not use letters to answer*')
time.sleep(5)
correct = (0)
num1 = (0)
num2 = (0)
for math in range(12):
    num1 = (random.randint(1, 12))
    num2 = (random.randint(1, 12))
    print('what is ' + str(num1) + ' times ' + str(num2) + '?') 
    anserright = num1 * num2
    guess = int(input())
    if anserright == guess:
        print ('correct!')
        correct = (correct + 1)
    else:
        print('nope')
    time.sleep(3)
print(correct)
if correct == 12:
    print('perfect!')
elif correct <=12 and correct >=9:
    print('very good!')
elif correct <=10 and correct >=5:
    print('ok.')
elif correct <=6:
    print('you can do better.')
