
n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[(n - 1) // 2])


# min = 1000000
# num = 1000000
# sum = 0
# for i in array:
#     sum = 0
#     j = array[0]
#     sum += abs(i - j)
#     j = array[1]
#     sum += abs(i - j)
#     j = array[2]
#     sum += abs(i - j)
#     j = array[3]
#     sum += abs(i - j)
#     print(i,sum)
#     if sum < min:
#         min = sum
#         if num > i: #왜 안됨
#             num = i

# print(num)