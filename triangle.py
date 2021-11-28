triangle = open('triangle.txt').readlines()

array = []

for i in range(0, len(triangle)):
    item = triangle[i].split(' ')
    to_int = []
    for j in item:
        to_int.append(int(j))
    array.append(to_int)

basis = array[0]
for i in range(1, len(array)):
    row = array[i]
    for j in range(0, len(row)):
        max_ = max(basis[j], basis[j - 1]) if 0 < j < len(row) - 1 else (basis[0] if j == 0 else basis[-1])
        row[j] += max_
    basis = row


print(max(basis))



