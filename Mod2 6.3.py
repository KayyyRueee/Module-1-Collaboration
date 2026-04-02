guess_me = 5
for num in range(10):
    if num < guess_me:
        print("Too Low")
    elif num == guess_me:
        print("Found It!")
    elif num > guess_me:
        print("Ooops")
        break