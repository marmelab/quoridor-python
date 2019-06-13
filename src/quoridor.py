import game


def main():
    pawn = game.init_game()
    board = game.get_board(pawn)
    game.display_board(board)


if __name__ == "__main__":
    main()
