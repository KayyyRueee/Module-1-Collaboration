secret = 3
import random
guess = random.randint(1, 10)
if guess < secret:
    print(guess)
    print("Too Low")
elif guess > secret :
    print(guess)
    print("Too High")
else:
    print(guess)
    print("Just Right")
