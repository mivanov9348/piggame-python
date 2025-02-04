from game import PigGame


def main():
    game = PigGame()

    print(f'Welcome to Pig Game!')

    while True:
        print(f'--------------------------------------')
        print(f'Player {game.current_player + 1} turn.')
        print(f'Player {game.scores}')
        print(f'Current Round Points: {game.current_score}')

        choice = input(f'Roll(r) Or Hold(h)?').strip().lower()

        if choice == 'r':
            game.roll_dice()
        elif choice == 'h':
            game.hold()
        else:
            print('Invalid Choice. R or H?')

        if game.check_winner():
            break

    print(f'\n End of the game! 🏁')


if __name__ == '__main__':
    main()
