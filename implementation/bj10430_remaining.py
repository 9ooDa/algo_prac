i, j, k = map(int, input().split())

print((i + j) % k)
print(((i % k) + (j % k)) % k)
print((i * j) % k)
print(((i % k) * j % k) % k)