range(10)
def get_odds():
    for n in range(10):
        if n % 2 == 1:
            yield n