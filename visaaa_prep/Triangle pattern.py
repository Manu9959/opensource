N = int(input())
current_number = 1
for i in range(1, N + 1):
    row = []
    for j in range(i):
        row.append(str(current_number))
        current_number += 1
    print(" ".join(row))
