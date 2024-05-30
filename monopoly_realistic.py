import random
import matplotlib.pyplot as plt

def throw_two_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

# writing a function that returns the number of throws taken for the player to buy every property in the game
def simulate_monopoly(starting_money_p1, starting_money_p2):
    board_values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                    0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                    0, 320, 200, 0, 350, 0, 400]
    # create a list to keep track of positions and use a loop to fill it up with 40 empty values
    # this will make sure that the players don't buy the same property twice
    possessions = []
    for i in range(40):
        possessions.append(0)

    # create two variables to keep track of no. of possesions of each player
    possessions_count_p1 = 0
    possessions_count_p2 = 0

    # set values to keep track of the position and no. of properties that have been bought
    position_p1 = 0
    position_p2 = 0
    property = 0


    # create a loop to iterate over until all properties are bought
    while property < 28:
        # update the position according to the dice throw value
        position_p1 = (position_p1 + throw_two_dice())
        if position_p1 < 40:
            board_position_value = board_values[position_p1]
        elif position_p1 >= 40:
            position_p1 = position_p1 % 40
            board_position_value = board_values[position_p1] # go back to start if you cross 39
            starting_money_p1 += 200 # pass go and collect 200
        if board_position_value != 0 and starting_money_p1 >= board_position_value and possessions[position_p1] == 0:
            # subtract the value of the property from the starting_money
            starting_money_p1 = starting_money_p1 - board_position_value
            # update the positions list
            possessions_count_p1 += 1
            # update the possesions list
            possessions[position_p1] = 1
            # update the property by 1
            property += 1
        # repeat the same process for player 2
        position_p2 = position_p2 + throw_two_dice()
        if position_p2 < 40:
            board_position_value = board_values[position_p2]
        elif position_p2 >= 40:
            position_p2 = position_p2 % 40
            board_position_value = board_values[position_p2] # go back to start if you cross 39
            starting_money_p2 += 200 # pass go and collect 200
        if board_position_value != 0 and starting_money_p2 >= board_position_value and possessions[position_p2] == 0:
            # subtract the value of the property from the starting_money
            starting_money_p2 = starting_money_p2 - board_position_value
            # update the positions list
            possessions_count_p2 += 1
            # update the possesions list
            possessions[position_p2] = 1
            # update the property by 1
            property += 1
    return possessions_count_p1 - possessions_count_p2

def simulate_monopoly_games(total_games, starting_money_p1, starting_money_p2):
    # create empty lists to store the values of differences
    difference_list = []
    # simulate games according to the given input
    for game in range(0, total_games):
        difference = simulate_monopoly(starting_money_p1, starting_money_p2)
        difference_list.append(difference)
    return sum(difference_list)/ len(difference_list)

print(f"Monopoly simulator: two players, 1500 euro starting money, 10000 games\nOn average player 1 has {simulate_monopoly_games(10000, 1500, 1500)} more streets in their possession when all streets have been bought")

def equilibrium():
    starting_money_p1 = 1500
    starting_money_p2 = 1500
    # create lists to store all p2 starting values and corresponding difference_list
    p2_list = []
    delta_list = []
    # create a loop that iterates over increasing p2 starting values
    while starting_money_p2 < 1700:
        # increment starting money by 50 every time and add it to the list
        starting_money_p2 += 50
        p2_list.append(starting_money_p2)
        delta = simulate_monopoly_games(10000, starting_money_p1, starting_money_p2)
        delta_list.append(delta)
        print(f"Starting money  [{starting_money_p1},{starting_money_p2}]: player 1 on average {delta} more streets (player 2 {starting_money_p2 - starting_money_p1} euros extra)")
    # plot a graph to show player 2 advantage with different starting values
    plt.plot(p2_list, delta_list)
    plt.show()
def main():
    print(equilibrium())
    print(f"Monopoly simulator: 2 players\nOn average, if player 2 receives 100 euros more starting money, both players collect an equal number of streets")

if __name__ == "__main__":
    main()
