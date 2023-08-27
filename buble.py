import random

n = 500

arr = list()
for i in range(n):

   number = random.randint(1, 100)
   arr.append(number)

print("Not sorted:")
print(arr)
print("------")


#####################################################################################

for i in range(n):
    for j in range(n - 1 - i):
        left = arr[j]
        right = arr[j + 1]
        if left > right:
            arr[j] = right
            arr[j + 1] = left




####################################################################################



print("Sorted:")
print(arr)