def main():
    print("First question")
    win_condition = {}
    win_condition['X'] = {
        'A': 3, 'B': 0, 'C': 6
    }
    win_condition['Y'] = {
        'A': 6, 'B': 3, 'C': 0
    }
    win_condition['Z'] = {
        'A': 0, 'B': 6, 'C': 3
    }
    user_score = {
        'X': 1, 'Y': 2, 'Z': 3 
    }
    with open("day-two/input.txt", 'r') as game_file:
        user_current_score = 0
        for line in game_file:
            user_current_score += win_condition[line[-2]][line[0]] + user_score[line[-2]]
        print(user_current_score)

    print("Second question")
    VICTORY = 6
    DRAW = 3
    LOST = 0
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    letter_to_number = {
        'A': ROCK, 'B': PAPER, 'C': SCISSOR,
        'X': LOST, 'Y': DRAW, 'Z': VICTORY
    }
    win_condition = {}
    win_condition[ROCK] = {
        LOST: LOST+SCISSOR, 
        DRAW: DRAW+ROCK, 
        VICTORY: VICTORY+PAPER 
    }
    win_condition[PAPER] = {
        LOST: LOST+ROCK, 
        DRAW: DRAW+PAPER, 
        VICTORY: VICTORY+SCISSOR
    }
    win_condition[SCISSOR] = {
        LOST: LOST+PAPER,
        DRAW: DRAW+SCISSOR,
        VICTORY: VICTORY+ROCK
    }
    with open("day-two/input.txt", 'r') as game_file:
        user_current_score = 0
        for line in game_file:
            user_current_score += win_condition[
                letter_to_number[line[0]]
            ][
                letter_to_number[line[-2]]
            ]
        print(user_current_score)



if __name__ == "__main__":
    main()