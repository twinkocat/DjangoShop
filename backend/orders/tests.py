from django.test import TestCase

list_1 = [10000.00, 5000.00, 1000.00, 30000.00]
list_2 = [0.50, None, 0.50, None]

result = []
for x, y in zip(list_1, list_2):

    if y is not None:
        result.append(x - x * y)
    elif y is None:
        result.append(x)

print(result)


