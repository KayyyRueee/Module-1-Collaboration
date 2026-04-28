def sum(arg): 
    total = 0
    for val in arg:
        total += val
    return total
def test_tuple(self):
    data = (1, 2, 3)
    result = sum(data)
    self.assertEqual(result, 6)
    