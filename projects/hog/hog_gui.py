"""Web server for the hog GUI."""
import io
import os
from contextlib import redirect_stdout

from gui_files.common_server import route, start

import hog
import dice

PORT = 31415
DEFAULT_SERVER = "https://hog.cs61a.org"
GUI_FOLDER = "gui_files/"
PATHS = {}


class HogLoggingException(Exception):
    pass


@route
def take_turn(prev_rolls, move_history, goal, game_rules):
    """Simulate the whole game up to the current turn."""
    fair_dice = dice.make_fair_dice(6)
    dice_results = []

    swine_align = game_rules["Swine Align"]
    pig_pass = game_rules["Pig Pass"]

    try:
        if not swine_align:
            old_swine_align, hog.swine_align = hog.swine_align, lambda score0, score1: False

        if not pig_pass:
            old_pig_pass, hog.pig_pass = hog.pig_pass, lambda score0, score1: False

        def logged_dice():
            if len(dice_results) < len(prev_rolls):
                out = prev_rolls[len(dice_results)]
            else:
                out = fair_dice()
            dice_results.append(out)
            return out

        final_scores = None
        final_message = None
        who = 0

        commentary = hog.both(
            hog.announce_highest(0),
            hog.both(hog.announce_highest(1), hog.announce_lead_changes()),
        )

        def log(*logged_scores):
            nonlocal final_message, commentary
            f = io.StringIO()
            with redirect_stdout(f):
                commentary = commentary(*logged_scores)
            final_message = f.getvalue()
            return log

        move_cnt = 0

        def strategy_for(player):
            def strategy(*scores):
                nonlocal final_scores, move_cnt, who
                final_scores = scores
                if player:
                    final_scores = final_scores[::-1]
                who = player
                if move_cnt == len(move_history):
                    raise HogLoggingException()
                move = move_history[move_cnt]
                move_cnt += 1
                return move
            return strategy

        game_over = False

        try:
            final_scores = trace_play(hog.play, strategy_for(0), strategy_for(1),
                                      0, 0, dice=logged_dice, say=log, goal=goal)[:2]
        except HogLoggingException:
            pass
        else:
            game_over = True
    finally:
        if not swine_align:
            hog.swine_align = old_swine_align
        if not pig_pass:
            hog.pig_pass = old_pig_pass

    return {
        "rolls": dice_results,
        "finalScores": final_scores,
        "message": final_message,
        "gameOver": game_over,
        "who": who,
    }


@route
def strategy(name, scores):
    STRATEGIES = {
        "bacon_strategy": hog.bacon_strategy,
        "extra_turn_strategy": hog.extra_turn_strategy,
        "final_strategy": hog.final_strategy,
    }
    return STRATEGIES[name](*scores[::-1])

def safe(commentary):
    def new_commentary(*args, **kwargs):
        try:
            result = commentary(*args, **kwargs)
        except TypeError as e:
            print("Error in commentary function")
            result = commentary
        return safe(result)
    return new_commentary


def trace_play(play, strategy0, strategy1, score0, score1, dice, goal, say):
    """Wraps the user's play function and
        (1) ensures that strategy0 and strategy1 are called exactly once per turn
        (2) records the entire game, returning the result as a list of dictionaries,
            each with keys "s0_start", "s1_start", "who", "num_dice", "dice_values"
    Returns (s0, s1, trace) where s0, s1 are the return values from play and trace
        is the trace as specified above.
    This might seem a bit overcomplicated but it will also used to create the game
        traces for the fuzz test (when run against the staff solution).
    """
    game_trace = []

    def mod_strategy(who, my_score, opponent_score):
        if game_trace:
            prev_total_score = game_trace[-1]["s0_start"] + game_trace[-1]["s1_start"]
            if prev_total_score == my_score + opponent_score:
                # game is still on last turn since the total number of points
                # goes up every turn
                return game_trace[-1]["num_dice"]
        current_num_dice = (strategy0, strategy1)[who](my_score, opponent_score)
        current_turn = {
            "s0_start": [my_score, opponent_score][who],
            "s1_start": [my_score, opponent_score][1 - who],
            "who": who,
            "num_dice": current_num_dice,
            "dice_values": [],  # no dice rolled yet
        }
        game_trace.append(current_turn)
        return current_num_dice

    def mod_dice():
        roll = dice()
        if not game_trace:
            raise RuntimeError("roll_dice called before either strategy function")
        game_trace[-1]["dice_values"].append(roll)
        return roll

    s0, s1 = play(
        lambda a, b: mod_strategy(0, a, b),
        lambda a, b: mod_strategy(1, a, b),
        score0,
        score1,
        dice=mod_dice,
        goal=goal,
        say=safe(say),
    )
    return s0, s1, game_trace


if __name__ == "__main__" or os.environ.get("ENV") == "prod":
    app = start(PORT, DEFAULT_SERVER, GUI_FOLDER)