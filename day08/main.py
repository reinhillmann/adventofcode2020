#!/usr/bin/python3
import re

def load_data(filename):
    with open(filename, 'r') as f:
        return [l.rstrip() for l in f.readlines()]

def load_instructions(data):
    instructions = []
    for row in data:
        op, val = re.match(r"^(jmp|acc|nop) ([\+|\-]?\d+)$", row).groups()
        val = int(val)
        instructions.append({"op": op, "val": val, "count": 0})
    return instructions

def find_cycle():
    instructions = load_instructions(data)
    acc = 0
    ip = 0
    while (ip < len(instructions)):
        instruction = instructions[ip]
        val = instruction["val"]
        op = instruction["op"]
        count = instruction["count"]
        if count > 0:
            return acc
        instruction["count"] += 1
        if op == "jmp":
            ip += val
            continue
        elif op == "acc":
            acc += val
        ip += 1

def fix_cycle(change_ip):
    instructions = load_instructions(data)
    acc = 0
    ip = 0
    while (ip < len(instructions)):
        instruction = instructions[ip]
        val = instruction["val"]
        op = instruction["op"]
        count = instruction["count"]
        if count > 0:
            # There's a cycle, return None.
            return None
        instruction["count"] += 1
        if op == "jmp":
            if ip == change_ip:
                instruction["op"] = "nop"
                ip += 1
            else:
                ip += val
            continue
        elif op == "acc":
            acc += val
        ip += 1
    return acc

if __name__ == "__main__":
    data = load_data('data.txt')
    instructions = load_instructions(data)

    # Part 1
    print(find_cycle())

    # Part 2
    # This is probably really, really suboptimal.
    # It just keeps rerunning the instructions from scratch, each time
    # modifying one jmp to nop.
    jmp_fix = 0
    result = fix_cycle(jmp_fix)
    while result == None:
        jmp_fix += 1
        result = fix_cycle(jmp_fix)
    print(result)
