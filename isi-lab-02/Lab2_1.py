import random
import math
import json


def show_menu():
    print("************************************")
    print("*          NUMBER GUESSER          *")
    print("************************************")
    print("1) Play game.")
    print("2) Show score board.")
    print("3) Exit.")
    print("")


def get_start_game_input():
    while True:
        name = input("Please, enter your name: ")
        if len(name) > 0:
            break
        else:
            print("Invalid name, you need at least one character. Try again...")

    while True:
        number = input("Please, enter an integer (> 0): ")
        if number.isnumeric() and int(number) > 0:
            number = int(number)
            break
        else:
            print("Invalid number, try again...")

    return name, number


def game(name: str, top: int, solution: int, trials: int, cheats: bool = False):
    points = 0
    fails = 0
    record = get_record_from_score_board(name)

    if record != -1.0:
        # The player has a record
        print(f"{name}, your current record is {record} points!")

    # Show solution if cheats are on
    if cheats:
        print(f"Psst! The number you are trying to guess is: {solution}")

    while trials > 0:
        print(f"Number of trials left: {trials}")

        # Get this round's number
        while True:
            number = input(f"{name}, enter a number between 1 and {top}: ")
            if number.isdigit() and int(number) > 0 and int(number) <= top:
                number = int(number)
                break
            else:
                print("Invalid number (does not affect left trials), try again...")

        if number == solution:
            print(f"You guessed the number! It was {solution}!\n")
            break
        elif number < solution:
            print(f"{number} is too low, try again...\n")
            trials -= 1
            fails += 1
        elif number > solution:
            print(f"{number} is too high, try again...\n")
            trials -= 1
            fails += 1

    if trials == 0:
        print(f"Too bad, {name} won't receive any points!")
    else:
        points = round(top / (1 if fails == 0 else (2 * fails)), 2)
        add_score_to_board(name, points)
        print(f"{name} has received {points} points!")


def show_score_board():
    try:
        file = open("score-board.json", "r")
        file.close()
    except FileNotFoundError:
        with open("score-board.json", "w") as f:
            f.write(
                json.dumps(
                    [],
                    indent=4,
                )
            )
    finally:
        file = open("score-board.json", "r")
        score_board = json.load(file)
        print("")
        for score in score_board:
            name = score["player"]
            points = score["points"]
            print(f"Name: {name}")
            print(f"Points: {points}")
            print("------------------------------------")
        print("")
        file.close()


def add_score_to_board(name: str, points: float):
    try:
        file = open("score-board.json", "r")
        file.close()
    except FileNotFoundError:
        with open("score-board.json", "w") as f:
            f.write(
                json.dumps(
                    [],
                    indent=4,
                )
            )
    finally:
        with open("score-board.json", "r+") as f:
            score_board = json.load(f)

            # Check if the player is already in the score board and if its new score is higher
            already = False
            change = True
            index = -1
            for i, score in enumerate(score_board):
                if score["player"] == name:
                    already = True
                    if score["points"] >= points:
                        change = False
                        index = i
                    break

            if already and change:
                # Player is present and has set a new PR
                score_board[index]["points"] = points
                f.seek(0)
                json.dump(score_board, f, indent=4)
            elif already:
                # Player is present but hasn't set a new PR
                pass
            else:
                # Player is not present in the score board
                score_board.append({"player": name, "points": points})
                f.seek(0)
                json.dump(score_board, f, indent=4)


def get_record_from_score_board(name: str) -> float:
    try:
        file = open("score-board.json", "r")
        file.close()
    except FileNotFoundError:
        with open("score-board.json", "w") as f:
            f.write(
                json.dumps(
                    [],
                    indent=4,
                )
            )
    finally:
        file = open("score-board.json", "r")
        score_board = json.load(file)

        for score in score_board:
            if score["player"] == name:
                file.close()
                return score["points"]

        file.close()
        return -1.0


if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Please, select an option: ")

        if option == "1":
            name, number = get_start_game_input()
            solution = random.randint(1, number)
            trials = math.ceil(math.log2(number))
            print("")
            game(name, number, solution, trials, True)
        elif option == "2":
            show_score_board()
        elif option == "3":
            break
