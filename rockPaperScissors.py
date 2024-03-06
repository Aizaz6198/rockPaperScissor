# import random

# user_wins = 0
# comp_user = 0

# while  True:
#     user_choice = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors or 'q' to quit: ").lower()
    
#     if user_choice == 'q':
#        break
       
#     if user_choice not in [ 'r', 'p','s'] :
#          print('Invalid Input')
#          continue
               
#     comp_choice = random.choice(['r', 'p', 's'])
    
#     # Checking the outcomes  of each round
#     if (user_choice == 'r' and comp_choice == 's') or \
#        (user_choice == 's' and comp_choice == 'p') or \
#        (user_choice == 'p' and comp_choice == 'r'):
#         user_wins += 1
#         print("Congratulations! You win this round.")
#     else:
#         comp_user += 1
#         print("Oops! The computer won this round.")
    
#     print(f"\nComputer chose {comp_choice}.") 


import random

user_wins = 0
comp_wins = 0
choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

while True:
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit.")
    
    user_choice = input("Your choice: ").lower()
    
    if user_choice == 'q':
        break
    
    if user_choice not in choices:
        print('Invalid input. Please enter a valid choice.')
        continue
               
    comp_choice = random.choice(list(choices.keys()))
    
    print(f"\nYou chose {choices[user_choice]}")
    print(f"Computer chose {choices[comp_choice]}")
    
    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and comp_choice == 's') or \
         (user_choice == 's' and comp_choice == 'p') or \
         (user_choice == 'p' and comp_choice == 'r'):
        user_wins += 1
        print("Congratulations! You win this round.")
    else:
        comp_wins += 1
        print("Oops! The computer won this round.")
    
    print(f"Score - You: {user_wins} Computer: {comp_wins}")
