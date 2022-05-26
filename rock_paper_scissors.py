# ================================================================================================================================
                    # my function definitions
# ================================================================================================================================

def is_winner(p1_choice,p2_choice):
    if (p1_choice == 'rock' and p2_choice == 'scissors') or (p1_choice == 'paper' and p2_choice == 'rock') or (p1_choice == 'scissors' and p2_choice == 'paper'):
        return True
    else:
        return False

def is_tie(p1_choice,p2_choice):
    if p1_choice == p2_choice:
        return True
    else:
        return False

def message_winner(p1,p2,p1_choice,p2_choice):
    if is_winner(p1_choice,p2_choice):
        print(f'{p1} Won')
    else:
        print(f'{p2} Won')

def rock_paper_scissors(p1,p2,p1_choice,p2_choice):
    while is_tie(p1_choice, p2_choice):
        print('Its a Tie. play continues')
        player1_choice = input(f'{player1} make a choice: "rock", "paper","scissors": ').lower()
        player2_choice = input(f'{player2} make a choice: "rock", "paper","scissors": ').lower()

    message_winner(p1,p2,p1_choice,p2_choice)

# ================================================================================================================================
                    # main game
# ================================================================================================================================

print("Welcom to the Rock Paper and  Scissors Game")

player1 = input('Player1 please enter your preferred name: ').title()
player2 = input('Player2 please enter your preferred name: ').title()
player1_choice = input(f'{player1} make a choice: "rock", "paper","scissors": ').lower()
while player1_choice not in ['rock','paper','scissors']:
    player1_choice = input(f'Invalid choice. try again {player1} make a choice: "rock", "paper","scissors": ').lower()

player2_choice = input(f'{player2} make a choice: "rock", "paper","scissors": ').lower()
while player2_choice not in ['rock','paper','scissors']:
    player2_choice = input(f'Invalid choice. try again {player2} make a choice: "rock", "paper","scissors": ').lower()

rock_paper_scissors(player1,player2,player1_choice,player2_choice)



