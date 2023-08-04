import random
rock = "✊"
paper = "✋"
scissor = "✌"
print("Welcome to Rock Paper Scissor Game!")
game = [rock, paper, scissor]
player = input("What do you choose?\n")
game_count = len(game)
game_count = random.randint(0, game_count - 1)
computer = game[game_count]
if player == '0' and computer == game[1]:
    print(f"Player: {game[0]}")
    print(f"Computer: {game[1]}")
    print("You Lose!!")
elif player == '0' and computer == game[0]:
    print(f"Player: {game[0]}")
    print(f"Computer: {game[0]}")
    print("It's a Draw!!")
elif player == '0' and computer == game[2]:
    print(f"Player: {game[0]}")
    print(f"Computer: {game[2]}")
    print("You Win!!")
elif player == '1' and computer == game[0]:
    print(f"Player: {game[1]}")
    print(f"Computer: {game[0]}")
    print("You Win!!")
elif player == '1' and computer == game[1]:
    print(f"Player: {game[1]}")
    print(f"Computer: {game[1]}")
    print("It's a Draw!!")
elif player == '1' and computer == game[2]:
    print(f"Player: {game[1]}")
    print(f"Computer: {game[2]}")
    print("You Lose!!")
elif player == '2' and computer == game[0]:
    print(f"Player: {game[2]}")
    print(f"Computer: {game[0]}")
    print("You Lose!!")
elif player == '2' and computer == game[1]:
    print(f"Player: {game[2]}")
    print(f"Computer: {game[1]}")
    print("You Win!!")
else:
    print(f"Player: {game[2]}")
    print(f"Computer: {game[2]}")
    print("It's a Draw!!")
