numbers = []
print("Sum numbers...")
num = int(input('Type a number'))
numbers.append(num)
while num != '':
    num = input('Type a number or press ENTER to calculate')
    if num != '' and int(num) : numbers.append(int(num))


print(f"The sum of the numbers {numbers} is: {sum(numbers)}")