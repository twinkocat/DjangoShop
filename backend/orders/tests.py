from django.test import TestCase

list_1 = [10000.00, 5000.00, 1000.00, 30000.00]
list_2 = [0.50, None, 0.50, None]
list_3 = [3, 1, 1, 1]


result = []
for x, y, z in zip(list_1, list_2, list_3):

    if y is not None:
        result.append((x - x * y) * z)
    else:
        result.append(x * z)

print(result)


