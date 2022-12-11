import math
import operator


def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


ops = {
    "+": operator.add,
    "*": operator.mul,
}


class Monkey:
    def __init__(self, name, items, op, test, if_true, if_false):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = 0

    def catch_item(self, item):
        self.items.append(item)

    def inspect_item(self, item, div, mod):
        self.inspected_items += 1
        a = item
        b = item if self.op[2] == "old" else int(self.op[2])
        new_worry = ops[self.op[1]](a, b)

        if div:
            new_worry = math.floor(new_worry / div)
        elif mod:
            new_worry = new_worry % mod

        if new_worry % self.test == 0:
            return True, new_worry

        return False, new_worry

    def throw_items(self, div=None, mod=None):
        throws = []
        for item in self.items:
            passes, new_worry = self.inspect_item(item, div, mod)
            if passes:
                throws.append((new_worry, self.if_true))
            else:
                throws.append((new_worry, self.if_false))
        self.items = []
        return throws

    def __str__(self):
        return f"{self.name} | {self.items} | {self.inspected_items}"


def make_monkey(input_group):
    name = input_group[0]
    items = [int(i) for i in input_group[1].split(": ")[1].split(",")]
    op = input_group[2].split("= ")[1].split(" ")
    test = int(input_group[3].split("by ")[1])
    if_true = int(input_group[4].split("monkey ")[1])
    if_false = int(input_group[5].split("monkey ")[1])
    return Monkey(name, items, op, test, if_true, if_false)


def make_monkeys():
    input = get_input("src/2022/12-11/input.txt")
    input_groups = [input[i : i + 7] for i in range(0, len(input), 7)]
    monkeys = []
    for group in input_groups:
        monkeys.append(make_monkey(group))
    return monkeys


def part_1():
    monkeys = make_monkeys()

    rounds = 20
    for _ in range(0, rounds):
        for monkey in monkeys:
            thrown_items = monkey.throw_items(div=3)
            for item, catching_monkey in thrown_items:
                monkeys[catching_monkey].catch_item(item)

    top_2 = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)[:2]
    return top_2[0].inspected_items * top_2[1].inspected_items


def part_2():
    monkeys = make_monkeys()
    modifier = math.prod(m.test for m in monkeys)

    rounds = 10_000
    for _ in range(0, rounds):
        for monkey in monkeys:
            thrown_items = monkey.throw_items(mod=modifier)
            for item, catching_monkey in thrown_items:
                monkeys[catching_monkey].catch_item(item)

    top_2 = sorted(monkeys, key=lambda x: x.inspected_items, reverse=True)[:2]
    return top_2[0].inspected_items * top_2[1].inspected_items


print(part_1(), part_2())
