line = input()

index_of_first_h = line.find('h')
index_of_second_h = line.rfind('h')

line_between_h = line[index_of_first_h + 1:index_of_second_h]

print(line[0:index_of_first_h + 1] + 2 * line_between_h + line[index_of_second_h:])
