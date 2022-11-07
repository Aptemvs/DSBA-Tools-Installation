file = open("input.txt")

student_languages = [{file.readline().rstrip("\n") for number_of_languages in range(int(file.readline()))}
                     for number_of_students in range(int(file.readline()))]
everyone, one = set.intersection(*student_languages), set.union(*student_languages)
print(len(everyone), *sorted(everyone), sep='\n')
print(len(one), *sorted(one), sep='\n')
