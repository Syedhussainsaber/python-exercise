print("Enter the number")
num = []
i = 0
while i < 7:
    nums = int(input())
    num.append(nums)
    i = i+1
uniqueNum = set()
j = 0
for Num in num:
    uniqueNum.add(num[j])
    j=j+1
print(uniqueNum)
# print(num)
set={18,"18",18.1}
print(set)
print(type(set))