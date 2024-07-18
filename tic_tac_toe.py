import os


# clear screen every time a player won
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Design the Game Board
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# empty list to hold players
players = []

# empty list to store each player symbol
symbols = []


# Display the Initial Board
def display_grid():
    print("-------------")
    for i, c in enumerate(grid):
        print(f"| {c} ", end="")
        if (i + 1) % 3 == 0:
            print("|\n-------------")


# display score after each win and when players are done playing
def display_score(pls):
    for pl in pls:
        print(f"{pl['name']}'s Score Is {pl['score']}")


print("""
****************************

  Welcome To Tic Tac Game!
  
****************************
""")

display_grid()


# Create Players
def create_player():
    player = {}
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            player["name"] = name.capitalize()
            break
        else:
            print("Name must contain only letters!")
    while True:
        symbol = input("Enter your symbol: ").upper()
        if len(symbol) == 1 and not symbol.isdigit():
            player['symbol'] = symbol
            symbols.append(symbol)
            break
        else:
            print("Symbol must be one letter.")
    player['score'] = 0
    players.append(player)


# Play by entering the cell number you want to ocupy
def play(player):
    while True:
        cell = input("Enter the cell: ")
        if len(cell) != 1:
            print("Cell number must be between 1 and 9.")
            continue
        try:
            cell = int(cell) - 1
            if grid[cell] not in symbols:
                grid[cell] = player['symbol']
                display_grid()
                return
            else:
                print(f"{cell + 1} already taken. try again")
        except ValueError as err:
            print(err)


# Reset teh game when a win or a draw is occurred, and players want to continue playing
def reset_grid(board):
    clear_screen()
    print("""
****************************
  Welcome To Tic Tac Game!
****************************
    """)
    for i in range(0, 9):
        board[i] = i + 1
    display_grid()


# when a win or a draw is occurred, handle next step
def game_over():
    print("1. Restart game!")
    print("2. Quit Game!")
    while True:
        ch = input("Enter your choice (1 or 2): ")
        if ch in ["1", "2"]:
            return ch
        else:
            print("Invalid choice. Try again")


# check if a player won
def check_win(player):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                        [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if grid[combo[0]] == grid[combo[1]] == grid[combo[2]]:
            player['score'] += 1
            print(f"Game Over!\n{player['name']} wins!")
            display_score(players)
            return True
    return False


# check if it is a draw
def check_draw():
    for item in grid:
        if item in range(0, 9):
            return False
    print("Game Over!\nA draw!")
    return True


# Update game after each successful turn
def update_game(player):
    print(f"{player['name']} turn {player['symbol']}")
    play(player)
    p_win = check_win(player)
    if p_win or check_draw():
        ch = game_over()
        if ch == "1":
            reset_grid(grid)
            return True
        elif ch == "2":
            print("Final Scores:")
            display_score(players)
            return False
        else:
            print("Only 1 or 2 are allowed.")
    return True


# create player one
print("Player one information:")
create_player()
# create player two
print("Player two information:")
create_player()

# Show players information
print(f"Player one: {players[0]['name']}, Symbol: {players[0]['symbol']} And initial score is {players[0]['score']}")
print(f"Player two: {players[1]['name']}, Symbol: {players[1]['symbol']} And initial score is {players[1]['score']}")


# Game Loop
while True:
    p1 = update_game(players[0])
    if not p1:
        break
    p2 = update_game(players[1])
    if not p2:
        break
