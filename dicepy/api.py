from .dice import DiceRoll, Die


def roll_dice(n, sides):
    dice = []
    for i in range(n):
        d = Die(sides)
        d.roll()
        dice.append(d)
    return DiceRoll(dice)