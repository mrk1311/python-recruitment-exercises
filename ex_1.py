numbers = [4,0,5,0,3,0,0,5]

for number in numbers:
    if number == 0:
        numbers.append(number)
        numbers.remove(number)

print(numbers)