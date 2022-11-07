storage_value_count = {}

for number in input().split():
    if number in storage_value_count:
        storage_value_count[number] += 1
    else:
        storage_value_count[number] = 1

print(max(storage_value_count, key=storage_value_count.get))
