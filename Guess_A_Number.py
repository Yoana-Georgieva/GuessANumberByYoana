import random
level=0
computer_number=random.randint(1, 100)
name=str(input())
print(f"Hello, {name}!")
while True:
    player_input=input("Guess the number 1-100:")
    if not player_input.isdigit():
        print("Please enter a digit input type")
        continue
    player_number=int(player_input)
    if player_number==computer_number:
        print("\033[32m You guessed it!\033[0m")
        level+=1
        print(f"Your level is {level}")
        computer_number = random.randint(1, 100)
    elif player_number>computer_number:
        print("'\033[31m Too high!\033[0m' Try a lower number.")
        level-=1
        print(f"Your level is {level}")
    elif player_number<computer_number:
        print("'\033[31m Too low!\033[0m' Try a higher number.")
        level-=1
        print(f"Your level is {level}")
    if level>=10:
        print("You won the game!")
        break
    elif level<=-10:
        print("You lost the game!")
        break