from math import sqrt, fsum

points = [
]

a = fsum([ele[1] * sqrt(ele[0]) for ele in points]) / fsum(ele[0] for ele in points)
print(a)

# 1.0586894736008359