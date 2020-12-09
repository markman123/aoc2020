from typing import Dict, List


class Console():
    def __init__(self, instr: str):
        self.read_instr(instr)
        self.reset()

    def read_instr(self, instr: str):
        lines = instr.splitlines()
        output = []
        for line in lines:
            inp, val = tuple(line.split(" "))
            val = int(val)
            output.append((inp, val))
        self.instr = output
        self.new_instr = output
        self.program_length = len(self.instr)
        return output

    def process_instr(self):
        inp, val = self.new_instr[self.ptr]
        if inp == "nop":
            self.ptr += 1
        elif inp == "acc":
            self.accumulator += val
            self.ptr += 1
        elif inp == "jmp":
            self.ptr += val
        
    
    def run(self):

        while True:
            self.process_instr()
            if self.ptr in self.visited:
                return {"reason": "infinite", "acc": self.accumulator}
            
            if self.ptr >= self.program_length:
                return {"reason": "correct", "acc": self.accumulator}
            self.visited.append(self.ptr)


    def reset(self):
        self.visited = [0]
        self.accumulator = 0
        self.new_instr = [i for i in self.instr]
        self.ptr = 0
        
    def chg(self):
        output = {}
        
        for i in range(self.program_length):
            self.reset()
            inp, val = self.new_instr[i]
            if inp == "acc":
                continue
            if inp == "jmp":
                inp = "nop"
            elif inp == "nop":
                inp = "jmp"

            self.new_instr[i] = (inp, val)
            output[i+1] = self.run()
        return output


instr = open("inputs/08.txt").read()
console = Console(instr)
last_output = console.run()
print(last_output)
outputs = console.chg()
print(outputs)