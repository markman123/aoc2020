
from ast import parse


def find_single_complement(numbers: str, target: int):
    numbers = parse_input(numbers)
    for number in numbers:
        complement = target - number
        if complement in numbers:
            return complement, number
    return None

def find_complements_brute(inputs, target):
    for x in range(len(inputs)):
        for y in range(1, len(inputs)):
            for z in range(2, len(inputs)):
                if inputs[x] + inputs[y] + inputs[z] == target:
                    return x, y, z
        
def find_complements(inputs, target):
    # Dict with key == sum of 2, value = list of 2 inputs
    inputs = parse_input(inputs)
    seen = build_dict(inputs)
    for x in range(len(inputs)):
        this_n = inputs[x]
        required = target - this_n
        if required in seen.keys():
            other_sum = seen[required]
            return this_n, other_sum[0], other_sum[1]

def build_dict(inputs):
    output = {}
    for x in range(len(inputs)):
        for y in range(1, len(inputs)):
            if x != y:
                xn = inputs[x]
                yn = inputs[y]
                output[xn+yn] = [xn,yn]
    return output

def parse_input(inputs: str):
    return [int(i) for i in inputs.splitlines()]

def part1(inputs: str):
    n, complement = find_single_complement(inputs, 2020)
    return n * complement

def part2(inputs: str):
    return find_complements(inputs, 2020)

if __name__ == "__main__":
    inputs = open("inputs/01.txt","r").read()

    ans = part1(inputs)
    print(ans)

    x,y,z = part2(inputs)
    print(f"{x}+{y}+{z} == {x+y+z} * == {x*y*z}")