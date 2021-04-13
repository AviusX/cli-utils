#!/usr/bin/env python3

import random
import os
import sys
from colorama import Fore, Style

choice_list = ['#', 'Rock', 'Paper', 'Scissors']

rock = list(open(f'{sys.path[0]}/Rock.txt').read().rstrip())
paper = list(open(f'{sys.path[0]}/Paper.txt').read().rstrip())
scissors = list(open(f'{sys.path[0]}/Scissors.txt').read().rstrip())

def menu_print():
    '''
    Prints the menu to assist the player.
    '''
    print(Style.BRIGHT)
    print(f'\t\t{Fore.LIGHTRED_EX}Rock Paper Scissors by Avius')
    print(Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX)
    print('Enter your choice-')
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print(Style.RESET_ALL)
    print()

def player_move_prompt():
    '''
    Takes input for player's move (Rock, Paper or Scissors) and returns it as a string.
    '''
    while True:
        while True:
            try:
                player_choice = int(input("Choice: "))

            except ValueError:
                print("Please enter 1, 2 or 3 only")

            else:
                break

        if(player_choice == 1 or player_choice == 2 or player_choice == 3):
            player_move = choice_list[player_choice]
            return player_move

        else:
            print('Please enter a valid choice!')
            continue

def determine_win(move1, move2):
    '''
    Returns 1 if move1 wins, 0 if tie, -1 if move1 loses.
    '''
    if move1 == 'Paper' and move2 == 'Rock':
        return 1
    elif move1 == 'Rock' and move2 == 'Scissors':
        return 1
    elif move1 == 'Scissors' and move2 == 'Paper':
        return 1
    elif move1 == move2:
        return 0

    return -1

def play_again_prompt():
    '''
    Asks the player if they would like to play again. Returns a boolean.
    '''
    play_again = False

    print(Fore.BLUE)
    print("Would you like to play again?")
    print("1. Yes")
    print("2. No")
    print(Style.RESET_ALL)

    while True:
        while True:
            try:
                player_choice = int(input("Answer: "))

            except ValueError:
                print("Please enter 1 or 2 only")

            else:
                break

        if(player_choice == 1):
            play_again = True 

        elif(player_choice == 2):
            play_again = False 

        else:
            print("Please enter 1 or 2 only")
            continue

        return play_again 

def print_move_ascii(move):
    '''
    Prints ASCII art for the move in the argument.
    '''
    if(move == 'Rock'):
        print(''.join(rock))

    elif(move == 'Paper'):
        print(''.join(paper))

    elif(move == 'Scissors'):
        print(''.join(scissors))

def game():
    '''
    The main function for the game.
    '''
    quit = False
    

    while not quit:
        os.system("clear")
        menu_print()
        player_move = player_move_prompt()
        computer_move = random.choice(choice_list[1:])

        print()
        print(Fore.BLUE)
        print(f'You chose: {Fore.MAGENTA}{Style.BRIGHT}{player_move}{Style.RESET_ALL}')
        print_move_ascii(player_move)
        print()

        print(Fore.BLUE)
        print(f'Computer chose: {Fore.MAGENTA}{Style.BRIGHT}{computer_move}{Style.RESET_ALL}')
        print_move_ascii(computer_move)
        print()

        win_or_lose = determine_win(player_move, computer_move)

        if(win_or_lose == 1):
            print(Fore.GREEN)
            print("Congratulations! You have won!")

        elif(win_or_lose == 0):
            print(Fore.YELLOW)
            print("Oof, it's a tie. Good luck next time!")

        else:
            print(Fore.RED)
            print("Damn, you lost. Better luck next time!")

        print(Style.RESET_ALL)
        quit = not play_again_prompt() # If player wants to play again (True) then quit = !True --> False

if __name__ == '__main__':
    try:
        game()
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}Thank you for playing!\n")
        quit()
