import numpy as np

# nums = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
# print(nums)
# print(nums)
#
# print(nums.shape)
# print(nums.dtype)


# nums = np.array(
#     [[1,2,4],
#      [5,6,7],
#      [8,9,10]]
# )
# print(nums)
# print(nums.shape)

# Створіть масив з числами від 1 до 10. Виведіть його, його
# розмір, тип даних.
# Змініть розмір масиву на (5, 2). Знову виведіть масив,
# розмір та тип даних

# nums = np.arange(1,10+1)
# print(nums)
# print(nums.shape)
# print(nums.dtype)
#
# new_nums =nums.reshape(5,2)
# print(new_nums)
# print(new_nums.shape)
# print(new_nums.dtype)


# авдання 2
# Створіть масив:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Використовуючи індекси виведіть:
# ● число 7
# ● другий рядок
# ● останній стовпчик
# ● праву половину
# ● жовту область
# ● замініть жовту область на -1
# ● зробіть перший стовпчик таким самим як і другий

# nums = np.array(
#     [
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12]
#     ]
# )
# print(nums)

# print(nums[1,2])
# print(nums[1])
# print(nums[:,-1])
# print(nums[:,2:4])
# print(nums[1:3:,1:3])
# nums[1:3,1:3] = -1
# print(nums)
# print(nums[:,0])
# nums[:,0] = nums[:,1]
# print(nums)


# У масиві з попереднього завдання створіть маску для
# чисел які більші за 6. З її допомогою
# ● виведіть кількість чисел більших за 6
# ● виведіть самі числа
# ● до кожного числа яке відповідає масці додайте 10
# ● кожне число що не відповідає масці помножте на -1
# ● замініть ці числа які відповідають масці на відповідні
# їм з масиву
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0


# mask = nums >6
# print(mask.sum())
#
# nums = nums[mask]
# print(nums)
#
# nums[mask] += 10
# print(nums)
#
# new_mask = ~mask
# nums[new_mask] *= -1
# print(nums)
#
# new_nums = np.array(
#     [
#         [1, 0, 1, 0],
#         [0, 1, 0, 1],
#         [1, 0, 1, 0]
#     ]
# )
#
# nums[new_nums] = new_nums[new_mask]
# print(nums)







# Завдання 6
# Створіть масив типу uint8
# 10 4 25 40 200
# |Помножте всі значення на 2. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255
# Помножте всі значення на 1.5. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255

#
# nums = np.array([10,4,25,40,200])
# # nums = nums.astype(np.uint8)
# #
# # nums = nums.astype(np.uint64)
# #
# # nums *= 2
# mask = nums > 255
# # nums[mask] = 255
#
# nums = nums.astype(np.float64)
# nums = nums * 1.5
# nums[mask] = 255
# nums = nums.astype(np.uint8)
#
# print(nums)
# print(nums.dtype)
