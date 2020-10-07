import random


class Die:

    def __init__(self, sides):
        if sides <= 0 :
            raise ValueError('Die cannot be created with 0 or fewer sides.')
        self.sides = sides
        self.past_rolls = []
        self.val = None


    def roll(self):
        self.past_rolls.append(self.val)
        self.val = random.randint(1, self.sides)


class DiceRoll:

    def __repr__(self):
        return 'Dice Roll - Total {} ({})'.format(
            sum([d.val for d in self.dice]), 
            ', '.join([str(d.val) for d in self.dice])
        )

    
    def __init__(self, dice):
        self.dice = dice

    
    def re_roll_lowest(self, n):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        re_roll = sort_dice[:n]
        map(lambda d: d.roll(), re_roll)


    def re_roll_highest(self, n: int):
        if n <= 0:
            raise ValueError('n must be higher than 0 to re-roll')
        sort_dice = sorted(self.dice, key=lambda d: d.val)
        i = len
        re_roll = sort_dice[len(self.dice)]

    