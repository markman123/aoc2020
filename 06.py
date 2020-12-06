
def process_input(n):
    file = open(n, "r").read()
    groups = file.split("\n\n")
    people_in_groups = [group.split("\n") for group in groups]
    return people_in_groups

def process_groups(groups):
    output = []
    for group in groups:
        questions = []
        for person in group:
            for question in person:
                questions.append(question)
        output.append(len(set(questions)))
    return output

def part2(groups):
    output = 0
    for group in groups:
        group_size = len(group)
        questions = []
        for person in group:
            questions += [question for question in person]
        for q in set(questions):
            people_answered = len([a for a in questions if a == q])
            if people_answered == group_size:
                output += 1
    return output

data = process_input("inputs/06.txt")
output = process_groups(data)
print(sum(output))
print(part2(data))