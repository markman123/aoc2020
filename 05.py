import math

def read_input(is_test=True):
    if is_test:
        data =  open("inputs/05_test.txt","r").readlines()
    else:
        data = open("inputs/05.txt","r").readlines()
    
    return [d.strip() for d in data]

def read_ticket(ticket):
    return get_row(ticket[:7], 0, 127), get_row(ticket[-3:], 0, 7)


def get_row(ticket_section, lbound, rbound):
    mid = round((rbound + lbound) / 2)
    for letter in ticket_section:
        if letter == "F" or letter == "L":
            mid = math.floor((rbound + lbound) / 2)
            rbound = mid
        else:
            mid = math.ceil((rbound + lbound) / 2)
            lbound = mid 
    return mid

def calc_seat(row_col):
    row, col = row_col
    return row * 8 + col

def part1():
    inputs = read_input(False)
    output = []
    for input_ in inputs:
        row_col = read_ticket(input_)
        output.append(calc_seat(row_col))

    print(max(output))
def possible_values():
    output = []
    for r in range(128):
        for c in range(8):
            output.append(calc_seat((r,c)))
    return output
def part2():
    inputs = read_input(False)
    output = []
    for input_ in inputs:
        row_col = read_ticket(input_)
        output.append(calc_seat(row_col))

    possible = possible_values()
    left_over = [p for p in possible if p not in output]
    for l in left_over:
        if l-1 in output and l+1 in output:
            print(l)

part2()