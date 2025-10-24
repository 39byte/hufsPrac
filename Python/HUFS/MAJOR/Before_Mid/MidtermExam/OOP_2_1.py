X = ["apple", "banana"]
Y = ["apple", "banana"]
K : list = ["apple", "banana", "mango"]
Z = X

print(X is Z)
print(X is Y)
print(X is not Y)

for i,k in enumerate(K):
    print(i,k)

# 2-24, 2-38
# 3-6~9

d = {1:1, 2:2, 3:3}

print(str(d))