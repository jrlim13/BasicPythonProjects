'''
Number Guessing
Make a program which randomly chooses a number to guess and then the user will have a few chances to guess the number correctly. 
In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.
'''
from random import randint

rand_num = randint(1, 10)
print(rand_num)

for i in range(0, 3):
    print("Guess the number from 1-10 (You have {} attempt/s): ".format(3-i), end="")
    guess_num = int(input())

    if guess_num != rand_num:
        print("Wrong Number.", end=" ")
        if guess_num > rand_num:
            print("(Hint: Less than guessed number)")
        else:
            print("(Hint: Greater than guessed number)")

        if i == 2:
            print("You used all your attempts.")
    else:
        print("You guessed the right number!")
        break
