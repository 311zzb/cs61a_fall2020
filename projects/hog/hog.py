"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    sum, rolls, is_one = 0, num_rolls, False

    while rolls > 0:
        point = dice()
        sum += point
        if point == 1:
            is_one = True
        rolls -= 1

    if is_one:
        return 1
    else:
        return sum
    # END PROBLEM 1


def ini_roll_prob(dice=six_sided, trials_count=10000):
    print("Initializing...")
    roll_prob = [[0 for x in range(61)] for y in range(11)] # Declare a 2D list
    for num_rolls in range(1, 11):
            roll_prob[num_rolls][:] = test_dice(num_rolls, dice, trials_count)

    print("Successed.")
    return roll_prob


def test_dice(num_rolls, dice=six_sided, trials_count=1000):
    """A function that simulate NUM_ROLLS dices for TRIALS_COUNT times and
    print the probabilities of associated with possible points gained. Return a
    list in which the N th int stand fo the probability of getting N point(s).

    """
    # Simulates the dices
    limit = 61
    results, k = [0] * limit, trials_count
    while(k > 0):
        results[roll_dice(num_rolls, dice)] += 1
        k -= 1

    # Print the results
    n, sum = 0, 0
    while(n < limit):
        # sum += results[n]
        output = round((results[n]/trials_count)*100, 2)
        if results[n] != 0:
            # print("DEBUG: The probability of getting", n, "points is:", output, "%.")
            results[n] = output
        n += 1
    # print("DEBUG: The total entries recorded:", sum)

    return results


ROLL_PROB = ini_roll_prob()


def curry2_swap(f):
    """A currying function. Notice that the two arguments are swaped.

    """
    return lambda x: lambda y: f(y, x) # f(y, x) instead of f(x, y)


def multi_search(f, min, max):
    """Search all the K that make F(K) TRUE, where K is from MIN to MAX.
    Return a list containing those K.
    """
    results, k = [], min
    while(k <= max):
        if(f(k)):
            results.append(k)
        k += 1
    return results


def list_subtract_by(l, n):
    """Subtract N from every element of L, return L
    """
    for i in range(len(l)):
        l[i] -= n
    return l


def points_to_extra_turn(score, opponent_score):
    """Calculate all possible points that could trigger an extra turn
    """
    have_extra_turn = curry2_swap(extra_turn)(opponent_score)
    extra_turn_points = multi_search(have_extra_turn, score+1, score+60)
    points_list = list_subtract_by(extra_turn_points, score)
    return points_list


def extra_turn_efficiency(num_rolls, score, opponent_score):
    """Return the efficiency of NUM_ROLLS dice(s) in terms of triggering an extra turn (probability)
    """
    efficiency = 0
    points_prob = ROLL_PROB[num_rolls][:]
    desired_points = points_to_extra_turn(score, opponent_score)
    for point in desired_points:
        efficiency += points_prob[point]
    return efficiency


def sprint_efficiency(num_rolls, score):
    efficiency = 0
    points_prob = ROLL_PROB[num_rolls][:]
    point = 60
    while(point >= GOAL_SCORE - score):
        efficiency += points_prob[point]
        point -= 1
    return efficiency


def free_bacon_extra_turn_efficiency(score, opponent_score):
    """Return the probability of a free bacon triggering an extra turn
    """
    efficiency = 0
    desired_points = points_to_extra_turn(score, opponent_score)
    if free_bacon(opponent_score) in desired_points:
        efficiency = 100
    return efficiency


def free_bacon_sprint_efficiency(score, opponent_score):
    """Return the probability of a free bacon bring you to the goal line (100 points)
    """
    efficiency = 0
    if free_bacon(opponent_score) >= GOAL_SCORE - score:
        efficiency = 100
    return efficiency


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    pi = pi // pow(10, 100 - score)
    # END PROBLEM 2

    return pi % 10 + 3


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if not num_rolls:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn."""
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))


def gcd(x, y):
    """Return the greatest common divisor (GCD) of two positive integers.

    >>> gcd(2, 4) # The GCD is 2
    2
    >>> gcd(11, 22) # The GCD is 11
    11
    >>> gcd(17, 67) # The GCD is 1
    1
    """
    assert x > 0 and y > 0, 'Cannot find GCD for non-positives.'
    assert type(x) == int and type(y) == int, 'Invalid datatype to finding GCD.'

    k = min(x, y)
    while(k > 0):
        if x % k == 0 and y % k == 0:
            return k
        k -= 1


def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    if not player_score * opponent_score:
        return False    # Return False if any score is 0

    return gcd(player_score, opponent_score) >= 10
    # END PROBLEM 4a


def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    if player_score < opponent_score and opponent_score - player_score < 3:
        return True
    else:
        return False
    # END PROBLEM 4b


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    def play_extra_turn(strategy, player, player_score, opponent_score, say=silence):
        if player_score >= goal:
            return player_score, say
        new_player_score = player_score # Use this variable during extra turns

        while(extra_turn(new_player_score, opponent_score)):
            new_player_score += take_turn(strategy(new_player_score, opponent_score), opponent_score, dice)
            # print("DEBUG: extra turn activated.")

            if player == 0: # Get the score0, score1, new_player_score, and opponent_score inserted right
                say = say(new_player_score, opponent_score) # Announce
            elif player == 1:
                say = say(opponent_score, new_player_score) # Announce

            if new_player_score >= goal:
                return new_player_score, say
        return new_player_score, say # Return the score after extra turns and the say function

    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, dice)
            say = say(score0, score1) # Announce
            score0, say = play_extra_turn(strategy0, 0, score0, score1, say)
        else:
            score1 += take_turn(strategy1(score1, score0), score0, dice)
            say = say(score0, score1) # Announce
            score1, say = play_extra_turn(strategy1, 1, score1, score0, say)

        who = other(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 8)
    Player 0 now has 10 and Player 1 now has 8
    >>> h3 = h2(10, 17)
    Player 0 now has 10 and Player 1 now has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    def say(score0, score1):
        # Calculate the gain for the right Player and record the score for the next turn
        if who == 0:
            gain, last_score_update = score0 - last_score, score0
        elif who == 1:
            gain, last_score_update = score1 - last_score, score1

        # Announce and update the running high if achieved a highest gain
        if gain > running_high:
            print(gain, "point(s)! The most yet for Player", who)
            running_high_update = gain
        else:
            running_high_update = running_high

        return announce_highest(who, last_score_update, running_high_update)
    return say
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=10000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    def experiments(*args):
        n, sum = trials_count, 0
        while n > 0:
            sum += original_function(*args)
            n -= 1
        return sum / trials_count
    return experiments
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, trials_count=10000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    averaged_roll_dice = make_averaged(roll_dice)
    n, high_score, high_dice = 1, 0, None
    while(n <= 10):
        score = averaged_roll_dice(n, dice)
        if(score > high_score): # Only update if new high is achieved
            high_score, high_dice = score, n
        n += 1
    return high_dice
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(6) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test extra_turn_strategy
        print('extra_turn_strategy win rate:', average_win_rate(extra_turn_strategy))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    bacon_point = free_bacon(opponent_score)
    if(bacon_point >= cutoff):
        num_rolls = 0

    return num_rolls
    # END PROBLEM 10


def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    bacon_point = free_bacon(opponent_score)
    with_free_bacon = score + bacon_point
    if (bacon_point >= cutoff or extra_turn(with_free_bacon, opponent_score)):
        num_rolls = 0

    return num_rolls
    # END PROBLEM 11


def best_to_extra_turn(score, opponent_score):
    """Calculate the best num of roll(s) and its probability to trigger an extra turn
    """
    num_rolls, best_num_rolls, best_efficiency = 1, None, 0
    while(num_rolls <= 10):
        efficiency = extra_turn_efficiency(num_rolls, score, opponent_score)
        if(efficiency > best_efficiency):
            best_num_rolls, best_efficiency = num_rolls, efficiency
        num_rolls += 1
    # print("The best num of roll(s) to trigger extra turn is", best_num_rolls, ", with a success probability of", best_efficiency)
    return best_num_rolls, best_efficiency


def best_sprint(score):
    """
    """
    if score == 99:
        return 0
    num_rolls, best_num_rolls, best_efficiency = 1, None, 0
    while(num_rolls <= 10):
        efficiency = sprint_efficiency(num_rolls, score)
        if(efficiency > best_efficiency):
            best_num_rolls, best_efficiency = num_rolls, efficiency
        num_rolls += 1
    return best_num_rolls


def final_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """Write a brief description of your final strategy.

    """
    # BEGIN PROBLEM 12
    sprint_threshold = GOAL_SCORE - 12 # The socre that we begin to sprint to the goal
    extra_turn_threshold = 75 # The probability that worth to trust on RNG for an extra turn
    extra_turn_rolls, extra_turn_rolls_efficiency = best_to_extra_turn(score, opponent_score)

    if score >= sprint_threshold: # Last moments strategy
        if free_bacon_sprint_efficiency(score, opponent_score):
            num_rolls = 0
        else:
            num_rolls = best_sprint(score)
    elif score <= opponent_score: # Force extra turn when we are behind our opponent
        if free_bacon_extra_turn_efficiency(score, opponent_score): # If free bacon could bring an extra turn
            num_rolls = 0
        elif free_bacon(opponent_score) >= cutoff: # If free bacon is worth for the points
            num_rolls = 0
        elif extra_turn_rolls_efficiency >= extra_turn_threshold: # If an extra turn is worth trying
            num_rolls = extra_turn_rolls # Rolls some dice(s) and hope the best
        else:
            num_rolls = 6 # Default
    # elif score == opponent_score: # If the scores are the same
    #     num_rolls = 10 # Pray for pure luck, or we can follow the back of our opponent
    else: # If we are in the lead
        if free_bacon_extra_turn_efficiency(score, opponent_score): # If free bacon could bring an extra turn
            num_rolls = 0
        elif free_bacon(opponent_score) >= cutoff - 1: # If free bacon is worth for the points
            num_rolls = 0
        elif extra_turn_rolls_efficiency >= extra_turn_threshold: # If an extra turn is worth trying
            num_rolls = extra_turn_rolls # Rolls some dice(s) and hope the best
        else:
            num_rolls = 4 # Less rolls than default to reduce risk

    # print("Player score:", score, "Opponent score:", opponent_score, "Choose to roll:", num_rolls)
    # print(" ")
    return num_rolls


def final_strategy_submit(score, opponent_score, cutoff=8, num_rolls=6):
    """
    """
    bacon_point = free_bacon(opponent_score)
    with_free_bacon = score + bacon_point
    if (bacon_point >= cutoff or extra_turn(with_free_bacon, opponent_score)):
        num_rolls = 0

    return num_rolls

    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
