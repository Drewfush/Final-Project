import random


def main():
    print('The goal of this game is to see if you roll 5 dice from 1 to 100 higher or lower than the computer!')
    print('At the end of the game, you will see if you beat the computer! \n')
    # above this line is the prompt explaining the first game ^
    score = 0  # setting score to 0 before rolls
    dice1 = random.randint(1, 100)  # this rolls the random number from the random library
    print('You rolled', dice1, '!')  # outputs the number rolled this turn
    score += dice1  # adds the dice number to the total

    dice2 = random.randint(1, 100)
    print('You rolled', dice2, '!')
    score += dice2  # running total that is added on to with each iteration

    dice3 = random.randint(1, 100)
    print('You rolled', dice3, '!')
    score += dice3

    dice4 = random.randint(1, 100)
    print('You rolled', dice4, '!')
    score += dice4

    dice5 = random.randint(1, 100)
    print('You rolled', dice5, '!')
    score += dice5
    print('Your final score is', score)  # printing the total score before comparison to see who won
    cputotal = random.randint(5, 500)  # setting the cpu total score
    if score > cputotal:  # determining who is the win with an if else setup
        print('You won! Your score of', score, 'was higher than', cputotal, '\n')  # win prompt
    else:
        print('You lost! Your score of', score, 'was lower than', cputotal, '\n')  # loss prompt


main()  # calling the main function to run the above game


def main2():
    print('The goal of this game is to get as close to 21 without going over! You will have 5 cards to do it!')
    print('Just like before, you are competing against the computer! \n')
    # The prompt above is explaining the objective of the second game ^
    blackjack = 0  # setting the total variable in this game to 0

    card1 = random.randint(1, 10)  # using random once again to generate our first card
    print('Your first card is', card1, 'it will be your starting amount!')  # first card added to total
    blackjack += card1  # because we start at zero, no need to confirm adding this card
    nextcard = "go"  # setting the while loop variable to ensure the loop begins
    while nextcard == "go":  # the continuation parameter being set with the comparison
        card = random.randint(1, 10)  # drawing a new card after continuing
        print("You drew", card)  # telling the user there new card
        nextcard = input('Type go to add it or pass to stop')  # giving the option to add to the total or stop
        if nextcard == "go":  # the addition parameter within the while loop
            blackjack += card  # adding the new card to the total
            print('Your new total is:', blackjack)  # printing the new total
        if nextcard == "pass":  # setting the quit condition
            print('Your final total is:', blackjack)  # printing the final score
            # the win conditions come at this part, as the end of this if scenario has the exit line
            cbj = random.randint(5, 21)  # setting the computer's value greater than five, assuming minimum roll is 5
            if blackjack > cbj and blackjack < 22:  # and comparison so that bust scores don't trigger win prompt
                print('You won!', blackjack, 'was higher than', cbj)
            if blackjack < cbj:  # comparison to see if player lost to computer
                print('You lost!', blackjack, 'was lower than', cbj)
            if blackjack > 21:  # comparison to see if user went over and busted
                print('Bust! You went over 21 with', blackjack)
            exit(0)  # forcing the exit of the game


main2()  # calling the function to run the second game
