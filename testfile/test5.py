a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([ [row[col] for row in a] for col in range(len(a[0]))])

print(list(zip(*a)))
print(list(map(list,zip(*a))))
