even_counter = 0

number = int(input())
while number != 0:
    if number % 2 == 0:
        even_counter += 1
    number = int(input())

print(even_counter)
