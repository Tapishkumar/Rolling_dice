import random

def main():
    player_1 = 0
    player_2= 0
    rounds = 1
    while rounds !=4:
        print("rounds "+ str(rounds))
        player_1= dice_roll()
        player_2 = dice_roll()
        print("player 1 dice :"+str(player_1))
        print("player 2 dice :"+str(player_2))
        if player_1== player_2:
            print("Draw")
        elif player_1>player_2:
            print(f"player 1 wins with {player_1}")
        else:
            print(f"player 2 wins with {player_2}")




        rounds = rounds+1




def dice_roll():
    Diceroll= random.randint(1,6)
    return  Diceroll

main()