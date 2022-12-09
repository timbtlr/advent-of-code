import math
from typing import List


def get_input(file_name: str):
    input = None
    with open(file_name) as f:
        input = f.readlines()
    input = [line.replace("\n", "") for line in input]
    return input


def build_matrix(input: List[str]):
    matrix = []
    for line in input:
        matrix.append([int(i) for i in list(line)])
    return matrix


def part_1():
    input = get_input("src/2022/12-8/input.txt")
    matrix = build_matrix(input)
    visible = (len(matrix) - 2) * 4 + 4
    for row_index, row in enumerate(matrix):
        if row_index in [0, len(matrix) - 1]:
            continue

        for column_index, tree_height in enumerate(row):
            if column_index in [0, len(matrix) - 1]:
                continue

            column = [m[column_index] for m in matrix]
            if any(
                [
                    all([tree_height > o for o in row[:column_index]]),
                    all([tree_height > o for o in row[column_index + 1 :]]),
                    all([tree_height > o for o in column[:row_index]]),
                    all([tree_height > o for o in column[row_index + 1 :]]),
                ]
            ):
                visible += 1
    return visible


def part_2():
    input = get_input("src/2022/12-8/input.txt")
    matrix = build_matrix(input)
    highest_score = 0
    for row_index, row in enumerate(matrix):
        for column_index, tree_height in enumerate(row):
            scores = []

            column = [m[column_index] for m in matrix]
            checks = [
                (row[:column_index], True),
                (row[column_index + 1 :], False),
                (column[:row_index], True),
                (column[row_index + 1 :], False),
            ]
            for check, reverse in checks:
                if reverse:
                    check.reverse()
                check_score = 0
                for other_tree_height in check:
                    check_score += 1
                    if other_tree_height >= tree_height:
                        break

                scores.append(check_score)
            highest_score = max(highest_score, math.prod(scores))
    return highest_score


print(part_1(), part_2())
