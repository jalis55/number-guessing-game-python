import random

# define range
low,high=1,50

# set chances
chances=5

# set correct answer
correct_answer=random.randrange(low,high)

# get user answer 5 times

for _ in range(chances):
    print(f'Guess the number between {low} to {high}:',end="")
    user_guess=int(input())
    # check answer
    if correct_answer==user_guess:
        print("You win")
        break
    else:
        status="Correct answer is greater! " if user_guess<correct_answer else "Correct answer is smaller !"
        print(status)
else:
    print("You lose")

