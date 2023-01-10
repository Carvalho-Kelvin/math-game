from models.calc import Calculate


def main() -> None:
    points: int = 0
    difficulty: int = int(input('Choose the difficulty of the game: (1 - Easy, 2 - Medium, 3 - Hard): '))
    play(points, difficulty)


def play(points: int, difficulty: int) -> None:
    while True:
        if difficulty == 1 or difficulty == 2 or difficulty == 3:
            calc: Calculate = Calculate(difficulty)
            break
        else:
            print('Choose a valid difficulty!')

    print('Solve the following operation: ')
    calc.show_operation()

    answer: int = int(input())

    if calc.check_result(answer):
        points += 1
        print(f'Congratulations! You won one point. You have {points} point(s)')
    else:
        print('Too bad, you missed!')

    while True:
        proceed: int = int(input('Do you want to continue the game? [1 - Yes, 2 - No] '))

        if proceed == 1:
            play(points, difficulty)
            break
        elif proceed == 2:
            print(f'You finished with {points} point(s)!')
            break
        else:
            print('Choose a valid option!')


if __name__ == '__main__':
    main()
