# House game project
import random
ticket = [12,45,78,90,46,14,77,85,34,98,37,97]
print(ticket)
player1 = [90,77, 98,37,45,14]
print(player1)
player2 = [12,78,46,85,34,97]
print(player2)
status = True
computer = 0
while status:
    print("press enter to Game start")
    input()
    computer=random.choice(ticket)
    print("Ticket number=",computer)
    if computer in player1:
        player1.remove(computer)
        print("Player 1 the number Removing it.")
        print(player1)
    if computer in player2:
        player2.remove(computer)
        print("Player 2 has the number Removing it.")
        print(player2)
    if not player1:
        print("player1 you win the game")
        choice = input("Do you want to play Game  write y for yes and n for No:")
        if choice == "y" or choice == "yes":
            status = True
        else:
            print("==================Game over=======================")
            status = False
    elif not player2:
        print("player2 you win the game")
        choice = input("Do you want to play Game  write y for yes and n for No:")
        if choice == "y" or choice == "yes":
            status = True
        else:
            print("==================Game over=======================")
            status = False
