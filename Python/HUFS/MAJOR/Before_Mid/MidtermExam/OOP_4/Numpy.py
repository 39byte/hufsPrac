import numpy as np

# # # # A = np.array([[1, 2, 3], [1, 2, 3]])
# # # # print(A)

# # # # A = np.arange(6)
# # # # print(A)

# # # lst = [[1, 2, 3], [4, 5, 6]]
# # # arr = np.array([[1, 2, 3], [4, 5, 6]])

# # # print(lst * 2)
# # # print(arr * 2)

# # # print(lst + [10])
# # # print(arr + [10])

# # A = np.array([[1, 2, 3], [4, 5, 6]])
# # print(A)

# # Af = np.array(A, dtype=float)
# # print(Af)

# # print(np.arange(0, 1, 0.2))
# # print(np.linspace(0, 2*np.pi, 4))

# a = np.arange(4)
# b = np.array([2, 3, 2, 4])

# print(a+b)
# print(a*b)

# b += a
# print(b)

# u = [1, 2, 3]
# v = [1, 1, 1]

# print(np.inner(u, v))
# print(np.outer(u, v))
# print(np.dot(u, v))

a = np.array([[1, 3, 6], [2, 4, 4]])
print(a)

print(a.sum(axis = 0))
print(a.sum(axis = 1))