"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times. Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    i, total, pigout = 0, 0, False
    while i < num_rolls:
        k = dice()
        if k == 1:
            pigout = True
        else:
            total = k + total
        i = i + 1
    return (pigout and 1) or total

roll1 = roll_dice(1)

roll2 = roll_dice(2)

roll3 = droll_dice(5)


# wrong implementations and studies

"""    k = 0
    while k < num_rolls:
		return dice """
		
# the below is correct but i dont like the use of "sum" for var name	
"""	 i, sum, pigout = 0, 0, False
    while i < num_rolls:
        k = dice()
        if k == 1:
            pigout = True
        else:
            sum += k 
        i += 1
    return (pigout and 1) or sum""" 
    
# missing total the function cant work properly
      
"""     i, pigout = 0, False
     while i < num_rolls:
		 k = dice()
		 if k == 1:
			 pigout = True
		else:
			k = k + 1
		i = i + 1
	 return (pigout and 1) or k"""
	 
	 
""" This works

from random import seed
from random import random



def test(num_rolls):
    i, pigout = 0, False
    while i < num_rolls:
        k = random()
        if k == 1:
            pigout = True
        else:
            k = k + 1
        i = i + 1
    return (pigout and 1) or k

test1 = test(1)

test2 = test(2)

test5 = test(5)



**
Try

def dice_roll(num_rolls):
    i, pigout = 0, False
    while i < num_rolls:
        k = dice()
        if k == 1:
            pigout = True
        else:
            k = k + 1
        i = i + 1
    return (pigout and 1) or k

roll1 = dice_roll(1)

roll2 = test(2)

roll3 = test(5)
"""
		 
		    
# https://www.reddit.com/r/learnprogramming/comments/9chon4/help_me_understand_this_higher_order_function/

"""def take_turn(num_rolls, opponent_score, dice=six_sided):
   Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"
    i, player_score, freebacon = 0, 0, False
    opponent_digits = [int(x) for x in str(opponent_score)]
    while num_rolls >= i:
        if num_rolls == 0:
			freebacon == True
			player_score = 1 + max(opponent_digits)
		else:
			player score = player_score + roll_dice(num_rolls)
		i = i + 1
	return player_score"""


def take_turn(num_rolls, opponent_score, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'    
    i, player_score, freebacon = 0, 0, False
    opponent_digits = [int(x) for x in str(opponent_score)]
    while num_rolls >= i:
        if num_rolls == 0:
			freebacon = True
            print("Freebacon!")
            player_score = 1 + max(opponent_digits)
        else:
            player_score = player_score + roll_dice(num_rolls)
        i = i + 1
    return player_score
    

turn1 = take_turn(0, 21)

turn2 = take_turn(2, 13)
    

    
    

""" Free bacon. A player who chooses to roll zero dice scores one more than 
the largest digit in the opponent's score.

Examples: if Player 1 has 42 points, 
Player 0 gains 1 + max(4, 2) = 5 points by rolling zero dice. 
If Player 1 has 48 points, Player 0 gains 1 + max(4, 8) = 9 points."""

""" f you want to change your number into a list of those numbers, 
I would first cast it to a string, then casting it to a list will naturally 
break on each character:

[int(x) for x in str(n)]"""


# tries

"""   i, player_score, freebacon = 0, 0, False
    opponent_digits = [int(x) for x in str(opponent_score)]
    while num_rolls >= i:
		if num_rolls == 0:
			freebacon == True
			player_score = 1 + max(opponent_digits)
		else:
			roll_dice()
			player_score = roll_dice() + total 
		i = i + 1
		return player_score """
		
# alternative

"""
def take_turn(num_rolls, opponent_score, dice=six_sided):
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'    
    i, player_score, freebacon = 0, 0, False
    opponent_digits = [int(x) for x in str(opponent_score)]
    while num_rolls >= i:
        if num_rolls == 0:
            freebacon = True
            print("Freebacon!")
            player_score = 1 + max(opponent_digits)
            return player_score
        else:
            player_score = player_score + roll_dice(num_rolls)
        i = i + 1
    return player_score"""
    

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    "*** YOUR CODE HERE ***"

def is_prime(n):
    """Return True if a non-negative number N is prime, otherwise return
    False. 1 is not a prime number!
    """
    assert type(n) == int, 'n must be an integer.'
    assert n >= 0, 'n must be non-negative.'
    k = 1
    while k < n:
        if n % k == 0:
            return False
    return True


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    return score0, score1  # You may want to change this line.

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Assume that dice always
    return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    "*** YOUR CODE HERE ***"

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test prime_strategy
        print('prime_strategy win rate:', average_win_rate(prime_strategy))

    if False: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    "*** YOUR CODE HERE ***"
    return None # Replace this statement

def prime_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and
    rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    "*** YOUR CODE HERE ***"
    return None # Replace this statement


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    "*** YOUR CODE HERE ***"
    return 5 # Replace this statement


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
