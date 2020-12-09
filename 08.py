from typing import Dict, List


class Console():
    def __init__(self, instr: str):
        self.accumulator = 0
        self.read_instr(instr)
        self.ptr = 0
        self.visited = [0]

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
        self.visited = []
        self.accumulator = 0
        self.ptr = 0
        while True:
            self.process_instr()
            if self.ptr in self.visited:
                return {"reason": "infinite", "acc": self.accumulator}
            
            if self.ptr >= self.program_length:
                return {"reason": "correct", "acc": self.accumulator}
            self.visited.append(self.ptr)

    def inscope(self):
        output = []
        for idx, instr in enumerate(self.instr):
            inp, _ = instr
            if inp in ["jmp","nop"]:
                output.append(idx)
        return output

    def chg(self):
        changes = self.inscope()
        output = {}
        for change in changes:
            self.new_instr = self.instr
            inp, val = self.new_instr[change]

            if inp == "jmp":
                inp = "nop"
            elif inp == "nop":
                inp = "jmp"
            
            self.new_instr[change] = (inp, val)
            output[change+1] = self.run()
        return output


instr = open("inputs/08.txt").read()
console = Console(instr)
last_output = console.run()
print(last_output)
outputs = console.chg()
print(outputs)