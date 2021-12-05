class Row:
    def __init__(self, value_list):
        self.entries = {}
        for value in value_list:
            self.entries[value] = False

    def mark_entry(self, value):
        if value in self.entries.keys():
            self.entries[value] = True

    def is_complete(self):
        return all([mark for mark in self.entries.values()])


class Board:
    def __init__(self):
        self.rows = []
        self.has_won = False
        self.won_from_previous_value = False

    def add_row(self, row_list):
        self.rows.append(Row(row_list))

    def has_completed_rows(self):
        for row in self.rows:
            if row.is_complete():
                return True

    def mark_value(self, value):
        self.won_from_previous_value = False
        for row in self.rows:
            row.mark_entry(value)
        if not self.has_won and self.has_completed_rows():
            self.has_won = True
            self.won_from_previous_value = True

    def unmarked_values(self):
        values = []
        for row in self.rows:
            for key, value in row.entries.items():
                if not value and key not in values:
                    values.append(key)
        return values


class Game:
    def __init__(self, game_input):
        self.boards = []
        self.load_game_from_input(game_input)

    def mark_value(self, value):
        for board in self.boards:
            board.mark_value(value)

    def winning_boards(self):
        return [board for board in self.boards if board.has_won]

    def recent_winning_boards(self):
        return [board for board in self.boards if board.won_from_previous_value]

    def incomplete_boards(self):
        return [board for board in self.boards if not board.has_won]

    def play_game(self, input_number_list):
        winners = losers = None
        for value in input_number_list:
            self.mark_value(int(value))
            winning_boards = self.winning_boards()
            recent_winning_boards = self.recent_winning_boards()
            incomplete_boards = self.incomplete_boards()

            if not winners and winning_boards:
                sums = [sum(board.unmarked_values()) for board in winning_boards]
                winners = sums, int(value)

            if not losers and not incomplete_boards:
                sums = [sum(board.unmarked_values()) for board in recent_winning_boards]
                losers = sums, int(value)
        return winners, losers

    def load_game_from_input(self, game_input):
        for index in range(0, len(game_input), 6):
            new_board = Board()
            board_input = [
                [int(value) for value in row.split(" ") if value]
                for row in game_input[index : index + 5]
            ]

            for row in board_input:
                new_board.add_row(row)

            for column in range(0, len(board_input[0])):
                new_board.add_row([row[column] for row in board_input])

            self.boards.append(new_board)


def solve():
    file = open("aoc_12-4_input.txt", "r")
    file_lines = file.read().splitlines()
    file.close()

    game = Game(file_lines[2:])
    winner, loser = game.play_game(file_lines[0].split(","))
    print(
        f"WINNER --- raw: {winner} sum:{sum(winner[0])} value:{sum(winner[0]) * winner[1]}"
    )
    print(
        f"LOSER --- raw: {loser} sum:{sum(loser[0])} value:{sum(loser[0]) * loser[1]}"
    )


solve()
