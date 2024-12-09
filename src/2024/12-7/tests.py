from part_one import get_operations, can_solve
from part_two import get_operations as get_operations_two, can_solve as can_solve_two


assert get_operations(1) == [
    []
]
assert get_operations(2) == [
    ["+"], 
    ["*"]
]
assert get_operations(3) == [
    ["+", "+"], 
    ["+", "*"], 
    ["*", "+"], 
    ["*", "*"]
]
assert get_operations(4) == [
    ["+", "+", "+"], 
    ["+", "+", "*"], 
    ["+", "*", "+"], 
    ["+", "*", "*"], 
    ["*", "+", "+"], 
    ["*", "+", "*"], 
    ["*", "*", "+"], 
    ["*", "*", "*"]
]
assert get_operations(5) == [
    ["+", "+", "+", "+"], 
    ["+", "+", "+", "*"], 
    ["+", "+", "*", "+"], 
    ["+", "+", "*", "*"], 
    ["+", "*", "+", "+"], 
    ["+", "*", "+", "*"], 
    ["+", "*", "*", "+"], 
    ["+", "*", "*", "*"], 
    ["*", "+", "+", "+"], 
    ["*", "+", "+", "*"], 
    ["*", "+", "*", "+"], 
    ["*", "+", "*", "*"], 
    ["*", "*", "+", "+"], 
    ["*", "*", "+", "*"], 
    ["*", "*", "*", "+"], 
    ["*", "*", "*", "*"]
]
assert get_operations(1) == [
    []
]

assert can_solve(10, [0]) == (False, None)
assert can_solve(10, [10]) == (True, None)
assert can_solve(10, [20]) == (False, None)

assert can_solve(10, [1, 1]) == (False, None)
assert can_solve(10, [5, 5]) == (True, ["+"])
assert can_solve(10, [5, 2]) == (True, ["*"])
assert can_solve(10, [10, 10]) == (False, None)

assert can_solve(100, [1, 1, 1]) == (False, None)
assert can_solve(100, [85, 10, 5]) == (True, ["+", "+"])
assert can_solve(100, [30, 20, 2]) == (True, ["+", "*"])
assert can_solve(100, [45, 2, 10]) == (True, ["*", "+"])
assert can_solve(100, [25, 2, 2]) == (True, ["*", "*"])
assert can_solve(100, [10, 10, 10]) == (False, None)

assert can_solve(100, [1, 1, 1, 1]) == (False, None)
assert can_solve(100, [10, 20, 30, 40]) == (True, ["+", "+", "+"])
assert can_solve(100, [5, 10, 35, 2]) == (True, ["+", "+", "*"])
assert can_solve(100, [10, 20, 3, 10]) == (True, ["+", "*", "+"])
assert can_solve(100, [10, 15, 2, 2]) == (True, ["+", "*", "*"])
assert can_solve(100, [20, 2, 10, 50]) == (True, ["*", "+", "+"])
assert can_solve(100, [20, 2, 10, 2]) == (True, ["*", "+", "*"])
assert can_solve(100, [10, 2, 3, 40]) == (True, ["*", "*", "+"])
assert can_solve(100, [5, 2, 2, 5]) == (True, ["*", "*", "*"])
assert can_solve(100, [10, 10, 10, 10]) == (False, None)

assert can_solve(911, [7, 6, 1, 868, 1]) == (True, ['*', '+', '+', '*'])


assert get_operations_two(2) == [
    ["+"], 
    ["*"],
    ["|"]
]

assert can_solve_two(10, [0]) == (False, None)
assert can_solve_two(10, [10]) == (True, None)
assert can_solve_two(10, [20]) == (False, None)

assert can_solve_two(10, [1, 1]) == (False, None)
assert can_solve_two(10, [5, 5]) == (True, ["+"])
assert can_solve_two(10, [5, 2]) == (True, ["*"])
assert can_solve_two(10, [10, 10]) == (False, None)

assert can_solve_two(100, [1, 1, 1]) == (False, None)
assert can_solve_two(100, [85, 10, 5]) == (True, ["+", "+"])
assert can_solve_two(100, [30, 20, 2]) == (True, ["+", "*"])
assert can_solve_two(100, [45, 2, 10]) == (True, ["*", "+"])
assert can_solve_two(100, [25, 2, 2]) == (True, ["*", "*"])
assert can_solve_two(100, [10, 10, 10]) == (False, None)


assert can_solve_two(100, [1, 1, 1, 1]) == (False, None)
assert can_solve_two(100, [10, 20, 30, 40]) == (True, ["+", "+", "+"])
assert can_solve_two(100, [5, 10, 35, 2]) == (True, ["+", "+", "*"])
assert can_solve_two(100, [10, 20, 3, 10]) == (True, ["+", "*", "+"])
assert can_solve_two(100, [10, 15, 2, 2]) == (True, ["+", "*", "*"])
assert can_solve_two(100, [20, 2, 10, 50]) == (True, ["*", "+", "+"])
assert can_solve_two(100, [20, 2, 10, 2]) == (True, ["*", "+", "*"])
assert can_solve_two(100, [10, 2, 3, 40]) == (True, ["*", "*", "+"])
assert can_solve_two(100, [5, 2, 2, 5]) == (True, ["*", "*", "*"])
assert can_solve_two(100, [10, 10, 10, 10]) == (False, None)

assert can_solve_two(911, [7, 6, 1, 868, 1]) == (True, ['*', '+', '+', '*'])


assert can_solve_two(156, [15, 6]) == (True, ["|"])
assert can_solve_two(7290, [6, 8, 6, 15]) == (True, ["*", "|", "*"])
assert can_solve_two(192, [17, 8, 14]) == (True, ["|", "+"])




    # 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    # 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
    # 192: 17 8 14 can be made true using 17 || 8 + 14.
