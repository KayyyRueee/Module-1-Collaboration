guess_me = 7
num = 1
while guess_me > num:
    num +=1
    print("Too low")
    if num == guess_me:
        print("Found it!")
    elif guess_me < num:
        print("Oops!")
        break