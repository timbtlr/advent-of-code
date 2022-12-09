from typing import List, Optional, Tuple


def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input

class Knot:
    def __init__(self, index="H", previous_knot=None):
        self.index = index
        self.previous_knot = previous_knot
        self.next_knot = None

        self.visited = [(0,0)]
        
        self.previous_position = None
        self.position = (0,0)

    def should_move(self):
        return abs(self.position[0] - self.previous_knot.position[0]) > 1 or abs(self.position[1] - self.previous_knot.position[1]) > 1

    def unique_positions(self):
        unique_positions = [len(set(self.visited))]
        if self.next_knot:
            unique_positions.extend(self.next_knot.unique_positions())
            return unique_positions
        return unique_positions

    def move(self, direction: str):
        self.previous_position = self.position
        match direction:
            case "U":
                self.position = (self.position[0], self.position[1]+1)
            case "R":
                self.position = (self.position[0]+1, self.position[1])
            case "D":
                self.position = (self.position[0], self.position[1]-1)
            case "L":
                self.position = (self.position[0]-1, self.position[1])

        self.visited.append(self.position)

        if self.next_knot:
            self.next_knot.follow()


    def follow(self):
        next_x = None
        next_y = None

        x_move = abs(self.previous_knot.position[0] - self.position[0]) > 1
        y_move = abs(self.previous_knot.position[1] - self.position[1]) > 1
        x_matches = self.previous_knot.position[0] == self.position[0]
        x_higher = self.previous_knot.position[0] > self.position[0]
        y_matches = self.previous_knot.position[1] == self.position[1]
        y_higher = self.previous_knot.position[1] > self.position[1]

        move_left = self.previous_knot.position[0] - self.position[0] < -1
        move_right = self.previous_knot.position[0] - self.position[0] > 1
        move_down = self.previous_knot.position[1] - self.position[1] < -1
        move_up = self.previous_knot.position[1] - self.position[1] > 1

        if x_matches:
            if move_up:   # Directly Up
                next_x = self.position[0]
                next_y = self.position[1] + 1 
            elif move_down:   # Directly Down
                next_x = self.position[0]
                next_y = self.position[1] - 1 

        elif y_matches:
            if move_right:   # Directly Right
                next_x = self.position[0] + 1
                next_y = self.position[1] 
            elif move_left:   # Directly Left
                next_x = self.position[0] - 1
                next_y = self.position[1] 

        elif x_move or y_move:
                if x_higher:
                    next_x = self.position[0] + 1
                else:
                    next_x = self.position[0] - 1

                if y_higher:
                    next_y = self.position[1] + 1
                else:
                    next_y = self.position[1] - 1

        if next_x is not None and next_y is not None:
            self.previous_position = self.position
            self.position = (next_x, next_y)
            self.visited.append(self.position)
            if self.next_knot:
                self.next_knot.follow()
                

class Rope:
    def __init__(self, knots=2):
        self.head_knot = Knot()
        previous_knot = None
        for i in range(1, knots):
            if not previous_knot:
                new_knot = Knot(index=i, previous_knot=self.head_knot)
                self.head_knot.next_knot = new_knot
            else:
                new_knot = Knot(index=i, previous_knot=previous_knot)
                previous_knot.next_knot = new_knot
            previous_knot=new_knot

    def move_head(self, direction:str, units:int):
        while units > 0:
            self.head_knot.move(direction)
            units -= 1

    def unique_positions(self):
        return self.head_knot.unique_positions()




def part_1():
    input = get_input("src/2022/12-9/input.txt")
    rope = Rope(knots=2)
    for line in input:
        line = line.split(" ")
        direction = line[0]
        units = int(line[1])
        rope.move_head(direction, units)
    return rope.unique_positions()[-1]


def part_2():
    input = get_input("src/2022/12-9/input.txt")
    rope = Rope(knots=10)
    for line in input:
        line = line.split(" ")
        direction = line[0]
        units = int(line[1])
        rope.move_head(direction, units)
    return rope.unique_positions()[-1]


print(part_1(), part_2())
