class Node:
    current_x: int
    current_y: int
    vel_x: int
    vel_y: int
    max_x: int
    max_y: int

    def __init__(self, current_x, current_y, vel_x, vel_y, max_x, max_y):
        self.current_x = current_x
        self.current_y = current_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.max_x = max_x
        self.max_y = max_y

    def __str__(self):
        return f"{self.current_x},{self.current_y} -> {self.vel_x}, {self.vel_y}"
    
    def move(self, count=1):
        self.current_x = (self.current_x + (self.vel_x * count)) % self.max_x
        self.current_y = (self.current_y + (self.vel_y * count)) % self.max_y

def make_grid(x_height, y_height):
    grid = []
    for _ in range(y_height):
        grid += [[0] * x_height]
    return grid

def print_grid(grid):
    for row in grid:
        s = ""
        for i in row:
            if i == 0:
                s += "."
            else:   
                s += str(i)
        print(s)

def solve(file_location, x_height, y_height):
    file_input = None
    with open(file_location) as f:
        file_input = f.readlines()

    nodes = []
    for line in file_input:
        line = line.replace("\n", "").split(" ")
        locs = line[0].replace("p=", "").split(",")
        vels = line[1].replace("v=", "").split(",")
        nodes += [
            Node(
                current_x=int(locs[0]), 
                current_y=int(locs[1]),
                vel_x=int(vels[0]),
                vel_y=int(vels[1]),
                max_x=int(x_height),
                max_y=int(y_height),
            )
        ]
    
    for index in range(100000):
        grid = make_grid(x_height, y_height)    
        for n in nodes:
            n.move(1)
            grid[n.current_y][n.current_x] += 1

        long_found = False
        for row in grid:
            if len([i for i in row if i > 0]) > 20:
                long_found = True
                print("long")

        if long_found:
            print_grid(grid)
            print("index", index + 1)
            input()

    return 

#print("Single Example", solve("example_single.txt", 11, 7))   
#print("Example", solve("example.txt", 11, 7))   
print("Puzzle", solve("input.txt", 101, 103))