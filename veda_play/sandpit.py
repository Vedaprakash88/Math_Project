import re

exp = input("Please enter the expression: ")
letters = re.findall(r'[a-zA-Z]', exp)
nums = re.findall(r'\d+', exp)
result = []
for le, nu in zip(letters, nums):
    result.append(le * int(nu))
print(''.join(result))




